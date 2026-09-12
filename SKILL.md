---
name: design-skills
description: >-
  UI/UX design knowledge base that gives AI agents the design intelligence to build
  original, high-quality websites of any category. Use when generating, redesigning,
  or prototyping any website, landing page, page section, component, or design system;
  when the user wants a unique, original design (never a template clone); when asked
  for design inspiration, references, design tokens, spacing/typography/color systems,
  layout patterns, interaction patterns, or accessibility guidance for a website.
  Provides analyzed design knowledge synthesized from many reference sites. Never
  copy a single reference — always combine multiple references into a new design
  language.
license: MIT
metadata:
  author: Emmraan
  version: "0.1.0"
---

# Design Skills

A **Design Knowledge Base** — analyzed design intelligence from real websites, ready for
synthesis. When the user wants a website built, you use this knowledge base to produce an
**original** design: you combine patterns, tokens, and ideas from multiple references into a
design the user has never seen before.

This is a knowledge skill, not a template skill. It contains no finished pages to copy.

## Core Principles (non-negotiable)

1. **Never copy.** No single website here may be reproduced. These are *references for
   synthesis*, not blueprints.
2. **Synthesize from multiple sources.** Retrieve at least 3 references (websites +
   components + patterns) before designing.
3. **Generate a new design language.** The output must not look like any single reference.
   Combine layout from one, color logic from another, type pairing from a third, and create
   something new.
4. **Preserve accessibility.** Contrast, focus states, keyboard navigation, semantic HTML,
   ARIA — always.
5. **Preserve responsiveness.** Every design must work from mobile to desktop; fluid type
   and spacing, defined breakpoints.
6. **Design decisions, not pixels.** Analyses describe *why* a design works (hierarchy,
   spacing logic, color roles) — apply the *logic*, not the exact values.

## When to Use

Activate when the user asks to:
- Build a website or landing page (any industry: SaaS, AI, fintech, ecommerce, agency,
  portfolio, healthcare, etc.)
- Redesign or improve an existing page's look and feel
- Design a specific section or component (hero, pricing, navbar, footer, FAQ, stats…)
- Create or extend a design system / design tokens
- Find design inspiration or explain why a design works

## Workflow (run this every time)

### 1. Understand the request
Identify: industry/category, page type (landing/multi-page/app), audience, theme preference
(dark/light), tone (minimal/bold/playful/premium), and any constraints (framework, a11y, speed).

### 2. Read the map
Read `INDEX.md` (the master index — always small). Do **not** read the whole repository.

### 3. Retrieve references
Use the indexes under `references/retrieval/` to find the most relevant references:

| If you need | Read |
|---|---|
| Websites for an industry/style | `retrieval/industry-index.json`, `retrieval/style-index.json` |
| A component design | `retrieval/component-index.json` |
| Which site is best for which part | `retrieval/knowledge-map.json` |

Open **3+ website analyses** in `references/websites/` and any matching component/pattern
files. Read the `analysis.md` files (not the whole repo).

Then read `references/processes/ui-build-playbook.md` and follow its phases —
Brief lock, Design-language lock, Compose, De-AI pass, Critique, Polish.

### 4. Analyze the pieces
Extract from each reference what you'll reuse *as logic*:
- **Layout & hierarchy** — how sections are ordered, what draws the eye first
- **Spacing system** — the scale and rhythm, not the exact px
- **Typography** — pairing logic, scale relationship, measure
- **Color** — the *roles* (primary/neutral/accent/surface), contrast logic, not the hex
- **Interactions & motion** — how behavior reinforces hierarchy
- **Accessibility** — what the reference does right that you must also do

### 5. Synthesize
Combine the strongest ideas into one coherent design language. Deliberately choose
*different* options for at least 2 of: layout, color, typography — so the result is not a
copy of any single source. Record a short synthesis note for yourself (which idea came from
where) before generating.

### 6. Generate
Produce the design with a **new** design language. Structure the page with the most fitting
pattern from `references/patterns/`. Use token systems from `references/design-tokens/` and
accessibility rules from `references/accessibility/`. Ship real, responsive code — the
sections should follow the component guidance in `references/components/`.

### 7. Validate
Check against `prompts/review-checklist.md`: contrast AA+, visible focus, keyboard-only
navigation works, semantic HTML, touch targets ≥44px, fluid responsiveness, and that no
single reference was copied. Then present the result.

## Prompt Rules for Generation

- Retrieve **multiple** references before designing.
- Combine inspirations; never mirror one site.
- Create an **original layout** and a **new design language**.
- Preserve accessibility and responsiveness in every output.
- If the user names a reference site, treat it as *one* input among several — still synthesize.

## Maintenance Mode (keep the knowledge base fresh)

When the user gives you a **URL** or asks to add/update/remove a website, use the scripts in
`scripts/`:

| Task | Command |
|---|---|
| Add a site from a URL | `python scripts/add.py <url>` then complete the draft analysis |
| Update a site (original changed) | `python scripts/update.py <slug>` |
| Refresh all sites | `python scripts/update-all.py` |
| Delete a site | `python scripts/delete.py <slug>` |
| Import a manually prepared folder | `python scripts/import.py <folder>` |
| Regenerate all indexes | `python scripts/rebuild.py` |
| Validate the repo | `python scripts/validate.py` |

After adding/updating, always run `rebuild.py` + `validate.py`. See
`scripts/analyze-agent.md` for how to complete a draft `analysis.md` from a Dembrandt
extraction. Full process for humans: `CONTRIBUTING.md`.

**Manual deep-analysis path:** if the user provides a site's real HTML/CSS (e.g. downloaded
via the Woblo Chrome extension), prefer analyzing the actual source over the Dembrandt draft —
it yields exact component structure, breakpoints, and values. Drop the folder through
`import.py` and base the `analysis.md` on the real source.

## Repository Map (load on demand only)

```
references/
├── collections/           category source lists (saas, ai, fintech, …)
├── websites/<slug>/       per-site: metadata.json, analysis.md, baseline.json
├── components/            per-section design guidance (hero, pricing, …)
├── patterns/              page assembly patterns per industry
├── design-tokens/         color/type/spacing/radius/motion/grid systems
├── interaction-patterns/  UX behaviors (nav, feedback, modals, forms, …)
├── accessibility/         contrast, semantics, ARIA, responsive rules
├── retrieval/             JSON indexes for fast lookup
├── prompts/               generation prompts, synthesis rules, review checklists
├── processes/             frontier UI-build process: playbook + observations + changelog
├── copywriting/           human-copy rules (no AI patterns in generated copy)
```

Read `INDEX.md` first. Load only the files you need — the indexes exist so you never read
the whole repository.
