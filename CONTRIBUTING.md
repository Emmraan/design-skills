# CONTRIBUTING.md — Adding & Maintaining Websites

This repo is a **design intelligence** knowledge base, not a template collection. Every
website we add is stored as *analyzed design knowledge* (metadata + prose analysis), not
screenshots or copied HTML. The goal is **inspiration and synthesis, never copying**.

This document is for **humans** (or agents acting for them) maintaining the knowledge base.
It mirrors exactly what the scripts do. The one thing to always remember:

> `references/websites/` is the **single source of truth**. `INDEX.md` and
> `references/retrieval/*.json` are **auto-generated** by `scripts/rebuild.py` — never
> hand-edit them.

---

## 0. Setup (first time)

```bash
pip install -r requirements.txt        # pyyaml for validate.py
npx dembrandt install-browser           # Chromium, when first needed
```

You run all Dembrandt commands yourself, one at a time (this machine is low-spec; never run
two extractions in parallel). The scripts only *print* the commands for you to run.

---

## 1. Add a site (automatic path — Dembrandt)

Adds a site by URL using Dembrandt extraction.

**Step 1 — Scaffold.** Creates `references/websites/<slug>/` with a `metadata.json` (filled
from the URL, `fingerprint: pending`) and a draft `analysis.md`, then prints the Dembrandt
command to run:

```bash
python scripts/add.py https://example.com
# prints: npx dembrandt https://example.com --save-output --design-md --wcag --crawl 5
```

**Step 2 — Run extraction (you).** Copy-paste the printed command and run it. Output lands
in `output/<domain>/<timestamp>_v0.28.0.json`. If the site is huge or slow, you can lower the
crawl depth: `python scripts/add.py https://example.com --crawl 2` (Mobbin was done with
`--crawl 1`).

**Step 3 — Complete the analysis.** Read the Dembrandt `DESIGN.md` draft + token JSON and fill
every section of `references/websites/<slug>/analysis.md`. Follow
`scripts/analyze-agent.md` — write **design decisions, not pixel values**, and always finish
with **sections 10–12** (component map, pattern position, synthesis notes) — they drive the
original-design goal. You may edit the scaffolded `metadata.json` (industry, style, layout,
theme, complexity, cta) as needed.

**Step 4 — Finalize.** Point `add.py` at the produced JSON (omit the path to auto-pick the
newest snapshot in `output/<domain>/`):

```bash
python scripts/add.py https://example.com --finalize output/<domain>/<timestamp>_v0.28.0.json
# or: python scripts/add.py https://example.com --finalize
```

This stores `baseline.json`, computes the fingerprint (SHA1 hex-12 of the baseline), fills
`metadata.json`, and runs `rebuild.py` + `validate.py`.

**Step 5 — Check.** `validate.py` should print `PASS`. Commit.

---

## 2. Update a site (drift detection)

Use when the original site changed and the analysis may be stale.

```bash
python scripts/update.py <slug>
# prints: npx dembrandt <url> --save-output --design-md --wcag --crawl 5 --compare references/websites/<slug>/baseline.json
```

Run the printed command. If drift is detected, Dembrandt exits non-zero. **Revise the
affected parts of `references/websites/<slug>/analysis.md` first**, then accept the new
snapshot:

```bash
python scripts/update.py <slug> --finalize <new-json>
```

This replaces `baseline.json`, refreshes the fingerprint and `collected-at`, then runs
`rebuild.py` + `validate.py`.

> Tip: keep `analysis.md` changes in sync with what the new extraction actually shows —
> the fingerprint only tracks the *baseline*, not your prose.

---

## 3. Update all sites (bulk freshness check)

```bash
python scripts/update-all.py
```

Prints the drift-check command for every site that has a `baseline.json`. Run them **one at a
time**, in order. It also lists any sites still stuck on `fingerprint: pending` (finish those
with `--finalize`). Sites with no baseline are skipped.

---

## 4. Delete a site

```bash
python scripts/delete.py <slug>
```

Removes `references/websites/<slug>/`, then runs `rebuild.py` + `validate.py` so INDEX.md and
the retrieval indexes drop the site. Reserved folders (`_template`) are protected.

---

## 5. Manual / deep-analysis path (Woblo + import.py)

For sites where you want the **most accurate analysis**, analyze the real source instead of
an automated draft. Two ways to import:

### 5a. Structured folder
Prepare a folder with `metadata.json` + `analysis.md` (copy from
`references/websites/_template/`) and import it:

```bash
python scripts/import.py ./my-folder [--slug <slug>]
```

Copies `metadata.json`, `analysis.md`, and optionally `baseline.json` into
`references/websites/<slug>/`, then rebuilds + validates.

### 5b. Woblo export (recommended for deep dives)
The [Woblo](https://chromewebstore.google.com/detail/woblo/gpamgcimpfifhcbelkmhlnienpppklcn)
Chrome extension downloads any site as `index.html` + `css/` + `assets/`.

1. Open the site in Chrome → download it with Woblo.
2. Drop the export folder anywhere and import it:

```bash
python scripts/import.py ./path/to/woblo-export [--slug <slug>]
```

3. `import.py` detects a Woblo export (`index.html` + `css/`), derives name/slug from the
   `<title>` and `og:url`, copies the real source to `references/websites/<slug>/source/`,
   and scaffolds a draft `analysis.md` telling the agent to analyze the real HTML/CSS.
4. Complete `analysis.md` **from the real source** — exact components, class names, real
   breakpoints and values (see `scripts/analyze-agent.md`).
5. `rebuild.py` + `validate.py` run automatically. If you also have a Dembrandt baseline for
   the site, drop it in as `baseline.json` (or add it via the automatic path).

> Why both paths? Dembrandt = fast auto-tokens + drift detection (great for many sites and
> updates). Woblo = exact source for high-quality deep analysis of the sites that matter most.

---

## 6. Regenerate indexes & validate (after any manual edit)

```bash
python scripts/rebuild.py     # regenerates INDEX.md + retrieval/*.json from websites/
python scripts/validate.py    # SKILL.md spec + links + index consistency
```

Run both after any change to `references/websites/`. `rebuild.py` preserves curated prose
from the existing indexes (borrow / signature / take notes) while keeping structure in sync;
`knowledge-map.json` and `references/collections/*.md` are editorial and untouched.

---

## 7. Rules & conventions

- **User runs Dembrandt** commands himself, one at a time. Scripts only print them.
- `references/websites/` is the source of truth; indexes are generated, never hand-edited.
- **Every analysis ends with synthesis notes** (section 12): what's unique, what to combine,
  what to avoid. This drives the "original design" goal.
- Describe **design decisions**, not pixels (color roles not just hex; pairing logic not just
  family names).
- **Never copy a site's design verbatim** — the point is inspiration and synthesis.
- Content in **English**. Text-only — no screenshots.
- After a successful `validate.py` PASS, commit with a clear message (e.g.
  `add <slug>`, `update <slug>`).
