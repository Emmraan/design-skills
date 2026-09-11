# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- version list -->

## v0.2.2 (2026-09-11)

### Bug Fixes

- Run CI only when relevant files change (ignore BUILD.md-only pushes)
  ([`a4df815`](https://github.com/Emmraan/design-skills/commit/a4df8156ea8320a74fa215a4fa1562e65b16d81b))

### Documentation

- Hygiene pass (Dembrandt pin, env matrix, output cache note)
  ([`5cb5808`](https://github.com/Emmraan/design-skills/commit/5cb58080611cc165d4a33baec5e7dd1118338263))

- Mark Phase B complete in BUILD.md tracker (CI green, v0.2.1 released)
  ([`e2aacc4`](https://github.com/Emmraan/design-skills/commit/e2aacc48a171e4d6205a131d1fe70ad72c1fda4e))

- Mark Phase C in progress in BUILD.md tracker (add-linear scaffolded)
  ([`e81e543`](https://github.com/Emmraan/design-skills/commit/e81e543b8f6868c0f25efe0fa462d2ee49fbee91))

- Mark Phase D1+E complete in BUILD.md tracker
  ([`1d65a2a`](https://github.com/Emmraan/design-skills/commit/1d65a2ab4050d5e5f6e33092f9cfd7555b68e40f))

- Sync BUILD.md (linear merged, GH_TOKEN fix, line-ending rule)
  ([`c1bda8e`](https://github.com/Emmraan/design-skills/commit/c1bda8e97687fe540323c17557f2a8fd8d01b493))


## v0.2.1 (2026-09-11)

### Bug Fixes

- Release workflow used GITHUB_TOKEN, PSR needs GH_TOKEN
  ([`7f20ceb`](https://github.com/Emmraan/design-skills/commit/7f20cebb35898e02fee350781aff90b8c96a3232))


## v0.2.0 (2026-09-11)

### Chores

- Add CI release automation (python-semantic-release)
  ([`bf1cf48`](https://github.com/Emmraan/design-skills/commit/bf1cf48bb1b184f571fc8869dc7315c7caedb2b3))

### Documentation

- Add BUILD.md future-work plan to main
  ([`f2e43b9`](https://github.com/Emmraan/design-skills/commit/f2e43b9bbbaeb6bbe95123d5a92cec1abf953fe7))

- Update BUILD.md tracker (Phase A automation done, lives on main now)
  ([`06c877c`](https://github.com/Emmraan/design-skills/commit/06c877c9813db2648df941442d8046b60781b5fa))

### Features

- Add CI validation and pytest suite
  ([`b2196ee`](https://github.com/Emmraan/design-skills/commit/b2196eef9f00497e979a2a0fa52ea9e52b963a00))


## [Unreleased]

### Added
- Nothing yet.

## [0.1.0] — 2026-08-15

Initial release — the build is complete and the repository is in **maintenance mode**
(see `AGENTS.md` for operating rules and `CONTRIBUTING.md` for the add/update/delete
workflows).

### Added
- **Skill**: `SKILL.md` (portable Agent Skill — name, description, MIT license, workflow,
  maintenance mode), `README.md`, `INDEX.md` (auto-generated), `CONTRIBUTING.md`,
  `AGENTS.md`, `LICENSE` (MIT), `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`.
- **10 website analyses** (`references/websites/<slug>/` with `metadata.json` +
  `analysis.md` + `baseline.json`): Wispr, Ghost, Ramp, ClickUp, Assembly, Juno, Sendr,
  Gumroad, Primora, Mobbin. Each analysis is DESIGN.md-compatible (sections 1–9) plus
  extended synthesis sections 10–12 (component map, pattern position, synthesis notes).
- **Knowledge base files** under `references/`:
  - `collections/` — 6 editorial category guides (saas, ai, fintech, ecommerce, agency,
    portfolio)
  - `components/` — 10 section guides (hero, navbar, logo-cloud, features, stats,
    testimonials, pricing, faq, cta, footer)
  - `patterns/` — 5 page-assembly patterns (saas-landing, ai-product, fintech, ecommerce,
    portfolio-agency)
  - `design-tokens/` — 6 systems (color, typography, spacing, radius/shadows, motion, grid)
  - `interaction-patterns/` — 5 UX behavior guides
  - `accessibility/` — 4 checklists (a11y, contrast, semantics/ARIA, responsive)
  - `retrieval/` — knowledge-map.json (editorial) + industry/style/component indexes
    (auto-generated)
  - `prompts/` — generation prompt, synthesis rules, review checklist
- **Maintenance scripts** (`scripts/`): `add.py`, `update.py`, `update-all.py`,
  `delete.py`, `import.py`, `rebuild.py`, `validate.py`, shared `_common.py`, and
  `analyze-agent.md` (how to complete a draft analysis).
- **Extraction engine**: Dembrandt (`npx dembrandt <url> --save-output --design-md --wcag
  --crawl 5`) with per-site `baseline.json` snapshots + SHA1 fingerprint drift detection.

### Fixed
- `scripts/import.py`: structured-folder imports now rewrite `metadata.json` slug to match
  the destination folder and mark `fingerprint` as `pending` when no `baseline.json` is
  provided (previously copied the template metadata as-is, which failed validation).

### Changed
- Build plan consolidated into operating docs; `BUILD.md` removed now that all phases are
  complete.

[Unreleased]: https://github.com/Emmraan/design-skills/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/Emmraan/design-skills/releases/tag/v0.1.0
