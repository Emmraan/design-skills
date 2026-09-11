# BUILD.md — Master Build Document (Future Plan)

> **READ THIS FIRST.** The **initial release (v0.1.0) is complete and shipped** on `main`
> (commit history: docs, 10 site analyses, scripts, CI-ready layout). This file is the
> **detailed future work plan** — small, executable tasks grouped into phases. All builds
> follow this file; its `## Progress Tracker` is maintained on `main` after every phase.
>
> Status of this plan lives in `## Progress Tracker`. When a phase is finished, mark its
> checkboxes `[x]` and merge the completed work to `main`.

---

## 0. Current state (baseline)

- ✅ Initial build complete, committed, pushed to `main` (`https://github.com/Emmraan/design-skills`).
- ✅ 10 analyzed sites; 60+ knowledge files; 7 maintenance scripts; validate.py PASS.
- ⬜ No CI, no script tests, no `v0.1.0` git tag yet, `gh` CLI not installed.
- Plan branch: `docs-build-plan` (renamed from `build-plan` per `docs-<thing>` convention).

---

## Workflow (locked for all phases — agreed 2026-09-11)

- **One phase = one branch off `main`** (branch names listed per phase below). Never commit
  directly to `main`.
- **No `gh` CLI, no GitHub PRs — merges are LOCAL.** Per-phase flow:
  ```bash
  git checkout -b <phase-branch> main
  # ... implement chunk-by-chunk, verifying after every chunk ...
  git checkout main; git pull --ff-only origin main
  git merge --squash <phase-branch>; git commit -m "<type>: <msg>"
  python scripts/rebuild.py; python scripts/validate.py   # + pytest once Phase B lands
  git push origin main        # triggers validate.yml + release.yml on main
  git branch -D <phase-branch>   # -D because squash-merge is not an ancestor
  ```
- **Conventional Commits on `main` (required — CI tagging reads them).**
  `feat:` / `fix:` cut a release; `docs:` / `chore:` / `add <slug>:` do not.
- **Tags via CI** — `.github/workflows/release.yml` + `python-semantic-release`, same pattern
  as [`awesome-saas-alternatives`](https://github.com/Emmraan/awesome-saas-alternatives)
  (`release.yml` on push-to-main, `contents: write`). One exception: the `v0.1.0` bootstrap
  tag is created manually once (CI cannot retro-tag an already-shipped commit); every tag
  after that is created by CI.
- **Chunk-by-chunk verification** — implement a small chunk, run `validate.py` (must PASS)
  and `pytest` (must be green), then commit on the phase branch. Never merge with failing
  checks. Zero-bug rule.
- **Merge + delete rule** — merge to `main` ONLY when the phase exit criteria are complete;
  delete the branch immediately after merging.
- **After every phase merge**, update the checkboxes + `## Progress Tracker` in this file
  (commit on `docs-build-plan`).

---

## Phase A — Release polish + tag automation → branch `feat-release`

**Goal:** professional GitHub repo, working CHANGELOG links, and automatic tags for all
future releases.

- [x] **A1. One-time `v0.1.0` bootstrap tag** at the shipped commit (`78c3116`):
      `git tag -a v0.1.0 78c3116 -m "v0.1.0" && git push origin v0.1.0` — DONE, tag live.
      Fixes the dead CHANGELOG links (`releases/tag/v0.1.0`, `compare/v0.1.0...HEAD`).
- [x] **A2. Release automation** (files on `feat-release`, merged with a `chore:` prefix so
      the bootstrap merge itself does not mint `v0.2.0`) — DONE, merged to `main`:
      - `pyproject.toml` — `version = "0.1.0"` + `[tool.semantic_release]` config
        (PyPI upload off; same role as `npmPublish: false` in the reference repo).
        Verified via temp-repo rehearsal: `feat:` → `v0.2.0` + changelog insert +
        pyproject bump (`allow_zero_version = true` required, else PSR jumps to `v1.0.0`).
      - `.github/workflows/release.yml` — on push to `main`: setup-python →
        `pip install` → `validate.py` gate (broken code must never get tagged) →
        release step (`GITHUB_TOKEN`, `contents: write`).
- [ ] **A3. GitHub repo description + topics** (web UI, manual — no token/`gh` available):
      description: `UI/UX design knowledge base as a portable agent skill — analyzed
      website references for AI agents to synthesize original designs`;
      topics: `design`, `ui-ux`, `agent-skills`, `ai-agents`, `design-system`.
- [ ] **A4. Branch protection on `main`** (optional; do after B1). ⚠️ Must NOT require pull
      requests — merges are local and CI pushes tags/changelog back; a PR requirement
      would block both. PR-less protection (or skip) only.

**Exit criteria A:** `v0.1.0` tag live on origin; `release.yml` on `main`; description +
topics set; (A4 optional).

---

## Phase B — Quality guardrails → branch `feat-ci-tests`

**Goal:** no broken merge can ever land; scripts become safe to refactor.

Chunks (verify `pytest` + `validate.py` after each):

- [x] **B3. `requirements-dev.txt`** — `pytest` (runtime `requirements.txt` untouched).
- [x] **B1. GitHub Actions CI** — `.github/workflows/validate.yml` (push + PR on `main`:
      checkout → setup-python 3.13 → install → `validate.py` + rebuild-sync
      `git diff --exit-code`, enforces D9). CI run green.
- [x] **B2a. `tests/conftest.py` + `test_common.py`** — DONE.
- [x] **B2b. `test_rebuild.py`** — DONE.
- [x] **B2c. `test_validate.py`** — DONE. Suite: **31 passed**.
- [x] **B4. CI badge in `README.md`** — DONE.

Merged with **`feat:`** → CI green + auto-tags **`v0.2.0`** (tag only — first release run
failed at GitHub-Release creation: workflow set `GITHUB_TOKEN` but PSR reads `GH_TOKEN`)
→ fixed on `fix-release-token` (`GH_TOKEN`, merged as `fix:`) → CI green + **`v0.2.1`
tag + GitHub Release** (automation proven end-to-end).

**Exit criteria B:** ✅ `pytest` green (31); `validate.py` PASS; rebuild-sync clean; CI green
on `main`; auto-tags + Release exist; badge present.

---

## Phase C — Content growth (ongoing mission) → per-site `add-<slug>` branches

**Goal:** expand category coverage so the skill answers more industries. Indexes regenerate
automatically — no hand-editing. One site = one `add-<slug>` branch (CONTRIBUTING.md
convention); merge each site independently when its own exit criteria complete.

- [ ] **C1. New site additions** — one Dembrandt run at a time (low-spec machine, user runs
      it; agent scaffolds via `add.py` and completes `analysis.md` after extraction):
      1. Pick a target industry with <2 references (candidates: healthcare, education,
         travel, developer-tools, hospitality, crypto/web3).
      2. `python scripts/add.py <url>` → run printed Dembrandt command → complete
         `analysis.md` (sections 1–12) → `--finalize` → rebuild + validate.
      3. Add the site slug to the matching `references/collections/*.md`.
      Note: `add <slug>:` commits are not `feat:` → site merges do not cut release tags.
- [ ] **C2. New editorial content** as new sites reveal patterns:
      - New `references/components/*.md`, `references/patterns/*.md`,
        `references/design-tokens/*.md` only if genuinely new.
      - Keep `INDEX.md` auto-generated; never hand-edit (D9).
- [ ] **C3. Curate `knowledge-map.json`** (editorial, manual) — add a `map` entry per new
      design-need discovered while adding sites.
- [ ] **C4. Woblo deep-analysis pass** (optional, manual): re-analyze the 10 existing sites
      from real HTML/CSS via `import.py` for exact components/breakpoints/values.

**Exit criteria C (per site):** `analysis.md` sections 1–12 complete; rebuild + validate
PASS; slug listed in the matching collection.

---

## Phase D — Skill ecosystem (next milestone; deferred as D11)

**Goal:** the knowledge base starts being *used* by real agents. Mostly verification —
open a `docs-spec-audit` branch only if a fix is needed.

- [ ] **D1. agentskills.io spec audit** — confirm SKILL.md passes: name matches repo,
      description ≤1024 (currently 666), body <500 lines (currently ~150).
- [ ] **D2. End-to-end install test** — `npx skills add https://github.com/Emmraan/design-skills`
      then trigger the skill in a sandbox agent and confirm `INDEX.md` retrieval flow works.
- [ ] **D3. agent-skills consumer** (in `github.com/Emmraan/agent-skills`, separate repo —
      no branch here):
      - `skills/design-ux/create-website` — consumes this KB when building a site.
      - `skills/design-ux/top-design` — synthesizes references into original designs.
      - Wire them to load `references/retrieval/*.json` before generating.

**Exit criteria D:** audit numbers confirmed; install test documented; consumer wired in the
other repo.

---

## Phase E — Hygiene → branch `docs-hygiene`

- [ ] **E1. Pin Dembrandt version** so extractions are reproducible across machines:
      document `npx dembrandt@0.28.0 …` in README (keep D6 command shape unchanged).
- [ ] **E2. Environment note** in AGENTS.md: record Python 3.13 + Node 22 + Dembrandt
      0.28.0 as the tested matrix.
- [ ] **E3. `output/` note** — extraction cache is gitignored local state; document that it
      stays outside version control (shared-drive move only if Dembrandt runs move to CI).

Merge with `docs:`/`chore:` (no release cut). **Exit criteria E:** validate PASS on `main`.

---

## Progress Tracker (update after every phase)

| Phase | Branch | Status | Notes |
|---|---|---|---|
| A — Release polish + tag automation | `feat-release` (merged, deleted) | 🟡 in progress | A1+A2 done; A3 manual (user web UI), A4 optional |
| B — Quality guardrails | `feat-ci-tests` (merged, deleted) | ✅ complete | 31 tests green, CI green, v0.2.0 tag + v0.2.1 tag+Release |
| C — Content growth | `add-<slug>` per site | 🟡 in progress | gap: agency/ecommerce=1, healthcare/education/travel/devtools/hospitality/web3=0; `add-linear` scaffolded+pushed, Dembrandt run pending (user) |
| D — Skill ecosystem | (verify; branch only if needed) | ⬜ pending | spec audit, install test, agent-skills consumer |
| E — Hygiene | `docs-hygiene` | ⬜ pending | version pin, env notes |

---

## Session continuation

1. Read this file.
2. Read `## Progress Tracker` → start the first `pending` phase on its listed branch
   (branched off `main`).
3. Build chunk-by-chunk on that branch; verify (`validate.py` PASS, `pytest` green) after
   every chunk and commit.
4. Merge to `main` ONLY when the phase exit criteria are complete — local squash-merge,
   push `main` (CI runs), then delete the branch.
5. Update this file + tracker and commit on `main` (BUILD.md lives on `main` now).
