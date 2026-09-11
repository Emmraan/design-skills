# Design Skills

[![validate](https://github.com/Emmraan/design-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/Emmraan/design-skills/actions/workflows/validate.yml)

A **UI/UX Design Knowledge Base** built as a portable Agent Skill. It gives AI coding agents
(Claude Code, OpenCode, Codex, Cursor, Cline, Roo Code, and any MCP/Agent-Skills compatible
client) the design intelligence to build **original, high-quality websites of any category** —
never a template clone.

The repository stores **analyzed design knowledge**, not screenshots: how layouts are built,
how spacing/typography/color systems work, what makes a component effective, how interactions
behave, and what good accessibility looks like. The AI retrieves relevant references and
**synthesizes** them into a new design language.

> Inspiration and synthesis — not copying.

## Install

```bash
npx skills add https://github.com/Emmraan/design-skills
```

Or copy this folder into your agent's skills directory (e.g. `.opencode/skills/design-skills`).

## How an agent uses it

1. `SKILL.md` loads when a design/website task matches.
2. Agent reads `INDEX.md` (the small master map).
3. Agent retrieves only the relevant references via `references/retrieval/*.json`.
4. Agent analyzes 3+ references, synthesizes, and generates an original design.
5. Agent validates against the accessibility/responsiveness checklists.

## Repository structure

```
SKILL.md                 Skill instructions (design brain)
INDEX.md                 Master index — agent's entry point after SKILL.md
references/
  collections/           Category source lists
  websites/<slug>/       Per-site: metadata.json, analysis.md, baseline.json
  components/            Section-level design guidance
  patterns/              Page assembly patterns per industry
  design-tokens/         Reusable design systems (color, type, spacing, motion…)
  interaction-patterns/  UX behaviors
  accessibility/         Contrast, semantics, ARIA, responsive rules
  retrieval/             JSON indexes for fast retrieval
  prompts/               Generation prompts + review checklists
scripts/                 add / update / delete / import / rebuild / validate
```

## Maintain the knowledge base

```bash
# Add a site from a URL (scaffolds the folder, prints the Dembrandt command to run,
# then finalize with the produced JSON — you run Dembrandt yourself)
python scripts/add.py https://example.com
python scripts/add.py https://example.com --finalize output/<domain>/<timestamp>_v0.28.0.json

# Update a site when the original changed (prints a drift-check command; accept a new snapshot)
python scripts/update.py <slug>
python scripts/update.py <slug> --finalize <new-json>

# Update all sites when originals changed (prints drift-check commands, one at a time)
python scripts/update-all.py

# Remove a site
python scripts/delete.py <slug>

# Import a manually prepared folder (see references/websites/_template/)
python scripts/import.py ./my-folder

# Regenerate indexes + validate
python scripts/rebuild.py
python scripts/validate.py
```

> **Deep-analysis tip:** For sites where you want the most accurate analysis, download the
> site's real HTML/CSS with the [Woblo Chrome extension](https://chromewebstore.google.com/detail/woblo/gpamgcimpfifhcbelkmhlnienpppklcn)
> and drop the export folder through `import.py` — the analysis is then written from the
> actual source instead of an automated draft.

Full process: see `CONTRIBUTING.md`.

## Requirements

- Python 3.10+ for repo-management scripts (`pip install -r requirements.txt`)
- Node.js 18+ for [Dembrandt](https://github.com/dembrandt/dembrandt) extraction
  (run via `npx dembrandt …`; browser installed on demand)

## License

MIT
