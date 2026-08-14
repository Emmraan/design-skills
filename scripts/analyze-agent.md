# analyze-agent.md — How to Complete a Draft Website Analysis

This file tells the **AI agent** (not a human) how to turn a Dembrandt extraction into a
finished `references/websites/<slug>/analysis.md`. It is used by `scripts/add.py` and
`scripts/update.py` in maintenance mode.

## Inputs

1. **Dembrandt extraction** — the JSON token snapshot (colors, typography, spacing, radius,
   shadows, motion, components, breakpoints) and the generated `DESIGN.md` draft
   (run with `--design-md --wcag --crawl 5`).
2. **Metadata** — industry, style, layout, theme, complexity, CTA signals.
3. **This template** — `references/websites/_template/analysis.md`.

> **Real source preferred:** if the user provides the site's actual HTML/CSS (e.g. Woblo
> export: `index.html` + `css/` + `assets/`), analyze the real source instead of relying only
> on the Dembrandt draft. It gives exact component structure, class names, real breakpoints,
> and values — use it for the Component Map and responsive sections.

## What to do

1. Read the Dembrandt `DESIGN.md` draft and token JSON.
2. Fill every section of the template, in order:
   - Sections 1–9: the DESIGN.md-compatible base (visual theme, colors + roles, typography,
     components, layout, elevation, do's/don'ts, responsive, agent prompt guide).
   - Sections 10–12: the extended synthesis sections (component map, pattern position,
     synthesis notes). These are the most important — they drive the "original design" goal.
3. **Write design decisions, not pixel values.** For example: "uses a tight 4px-based spacing
   scale with generous section padding (128px) to create calm rhythm" — not a raw dump.
4. Derive the **color roles** from the palette (what is primary vs neutral vs accent) rather
   than just listing hex codes.
5. Derive the **typography pairing logic** (display vs body, scale relationship).
6. Write concrete, useful **synthesis notes**:
   - What is *unique* about this site (worth borrowing as logic).
   - What to *combine* this with to create an original design.
   - Weaknesses / what to avoid copying.
7. Keep it in English. Be specific and concrete.

## Output

A complete `analysis.md` next to the site's `metadata.json` and `baseline.json` in
`references/websites/<slug>/`.

## After writing

Run:
```bash
python scripts/rebuild.py
python scripts/validate.py
```
