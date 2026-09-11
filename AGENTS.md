# AGENTS.md — Guidance for AI Agents Working in This Repo

> **READ THIS FIRST.** This file is the entry point for any AI agent (and any human)
> working in `design-skills`. All build phases are complete — the repo is in **maintenance
> mode**: the operational docs are `CONTRIBUTING.md` (maintenance workflow) and this file
> (operating rules). There is no more phased build plan.

---

## 1. What this repo is

A **UI/UX Design Knowledge Base** shipped as a portable Agent Skill. It gives AI coding
agents (Claude Code, OpenCode, Codex, Cursor, Cline, Roo Code, MCP clients) the design
intelligence to build **original, high-quality websites of any category** — never a copy.

- Purpose: **inspiration and synthesis, not copying.**
- Content: analyzed design knowledge (text) — no screenshots.
- Skill format: standard `SKILL.md`; repo root = skill folder (install via
  `npx skills add https://github.com/Emmraan/design-skills`).

## 2. Locked decisions (do not change without the user)

| # | Decision |
|---|---|
| D6 | Extraction engine is **Dembrandt** (`npx dembrandt <url> --save-output --design-md --wcag --crawl 5`). Never build a custom extractor. |
| D9 | Indexes are **auto-generated** by `scripts/rebuild.py` from `references/websites/`. Never hand-edit `INDEX.md` or `references/retrieval/*.json` (except editorial `knowledge-map.json`, which rebuild skips). |
| D10 | Content language: English. |
| D13 | Woblo = optional **manual** deep-analysis enrichment (real HTML/CSS source), complementary to Dembrandt. Fits `import.py`. |

## 3. Repo structure

```
SKILL.md                 Skill instructions (design brain)
INDEX.md                 Master map — auto-generated, do not edit
CONTRIBUTING.md          Add/Update/Delete/Manual process (humans + agents)
AGENTS.md                This file — operating rules
scripts/                 add/update/update-all/delete/import/rebuild/validate + _common.py + analyze-agent.md
references/
  collections/           Editorial category guides (curated, not overwritten)
  websites/<slug>/       Per-site: metadata.json + analysis.md + baseline.json  (SOURCE OF TRUTH)
  components/ patterns/ design-tokens/ interaction-patterns/ accessibility/ prompts/
  retrieval/             knowledge-map.json (editorial) + industry/style/component-index.json (generated)
```

## 4. Operating rules

- `references/websites/` is the **single source of truth**. `rebuild.py` regenerates
  `INDEX.md` + retrieval indexes from it; `validate.py` enforces consistency.
- Every `analysis.md` ends with **synthesis notes** (sections 10–12: component map, pattern
  position, synthesis). These drive the originality goal — never omit them.
- Describe **design decisions, not pixels** (color roles, pairing logic, spacing philosophy).
- Never copy a site's design verbatim. Analyze 3+ references and synthesize.
- Do not edit `_template/` files unless changing the template itself.
- User runs all Dembrandt commands himself, **one at a time** (low-spec machine). Scripts
  only print the commands — do not auto-execute them.

## 5. Maintenance commands (after any change to `references/websites/`)

```bash
python scripts/rebuild.py     # regenerate INDEX.md + retrieval/*.json
python scripts/validate.py    # SKILL.md spec + links + index consistency (expect PASS)
```

Full add/update/delete/import workflows: **`CONTRIBUTING.md`**.

## 6. Environment

- Python 3.10+ (`pip install -r requirements.txt` — pyyaml for validate.py).
- Node 18+ for Dembrandt; Chromium via `npx dembrandt install-browser` when first needed.
- Tested matrix: **Python 3.13 + Node 22 + Dembrandt 0.28.0**.
- This project is not the opencode config project — do not apply the `customize-opencode`
  skill here.
