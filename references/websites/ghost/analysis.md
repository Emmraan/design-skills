# Ghost — Design Analysis

> Source: `https://ghost.org/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Ghost is an open-source publishing platform. The marketing page is a masterclass in
> **editorial software marketing**: near-invisible chrome, type-led hierarchy, and color used
> as a single, confident accent.

## 1. Visual Theme & Atmosphere

- **Light-first, calm, confident.** A near-white canvas with crisp off-black type — the page
  reads like a well-typeset publication, which is exactly the right metaphor for a
  publishing platform.
- **Type is the hero.** Inter at huge display sizes with tight line-height. Very little
  decoration; the information architecture carries the design.
- **Accent pops, sparingly:** magenta/pink and lime appear as tiny but unmistakable
  highlights (links, eyebrows, moments) — a restrained "brand twinkle."
- Mood: professional, editorial, trustworthy, unflashy.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / brand | slate `#94A3B8` | Neutral brand tone (secondary to neutral) |
| Accent 1 | magenta `#FF247D` | The energetic accent — links, highlights, CTAs |
| Accent 2 | lime `#D1FF19` | Secondary accent — small moments, badges |
| Surface | light gray `#E5E7EB` | Card/panel surfaces on white |
| Text | ink `#111827` | Off-black body/headline (never pure black) |

- **Roles, not rainbow:** the palette is white + ink + one magenta accent. Lime is a
  secondary twinkle. This economy is the source of its confidence.
- **Neutral strategy:** cool grays tinted blue (`#94A3B8`, `#E5E7EB`) — calm, professional.
- **Dark handling:** primarily light-first; dark surfaces used sparingly for contrast bands.

## 3. Typography Rules

- **Family:** Inter family throughout — InterDisplay for headlines, InterVariable for body.
  One family, differentiated by weight + size (the disciplined "one family" approach).
- **Display scale:** 96px / 72px / 60px / 48px with `line-height ~1.0-1.35`, tight and bold.
  Headlines lean on **weight (600-700) + size**, not a second family.
- **Body:** 16-18px, `1.5` leading, comfortable 60-75ch measure — highly readable.
- **Labels:** small uppercase/letterspaced or tiny 12px — eyebrows and meta stay quiet.
- **Variable font** = performance-friendly (1 file, many weights).

## 4. Component Stylings

- **Primary button:** dark fill (`#15171A`) with white text, small radius (~6px), compact
  padding (8px × 16px). Black buttons on white = editorial authority.
- **Secondary / tertiary:** ghost and text links, restrained.
- **Links:** ink → accent (magenta) on hover, subtle.
- **Cards:** light gray surface, hairline/shadow edges, generous padding.
- **Badges:** lime/magenta accents for "new"/highlights — tiny, high-contrast.

## 5. Layout Principles

- **Spacing scale:** 8px base with tight micro steps (1-12px observed) for precise rhythm;
  sections use large vertical padding for calm breathing room.
- **Grid:** centered, strongly max-width'd columns; lots of whitespace; sections are
  flat bands separated by whitespace, not boxes.
- **Breakpoints:** 1400 / 1280 / 1120 / 1100 / 1024 / 1000 — smooth desktop→tablet→mobile.
- **Editorial rhythm:** headline → subhead → body → CTA, repeated consistently.

## 6. Depth & Elevation

- **Nearly flat:** hairline borders (1px, ~10-3% black) and very soft shadows
  (`0 10px 32px -5px` at 10% for the few elevated cards). Elevation is used to lift one
  element, never to decorate.

## 7. Do's and Don'ts

- **Do:** let type carry hierarchy; keep one accent and use it sparingly; use a single
  variable font family; black-on-white CTAs for authority.
- **Don't:** add decorative gradients; make everything a box; use 3+ accent colors; shrink
  body below 15px.

## 8. Responsive Behavior

- Display type fluid-scales; hero compresses gracefully at tablet/mobile.
- Nav collapses to a hamburger (CTA retained); grids collapse to single column.
- Touch targets respected; accordions/FAQ collapse cleanly.

## 9. Agent Prompt Guide

> Build a landing page with a **light, editorial, type-led aesthetic**: near-white canvas,
> off-black ink text, a single magenta-style accent used only for links/highlights/CTAs.
> Use ONE sans variable family for both display (72-96px, weight 600-700, tight leading) and
> body (16-18px, 1.5 leading). Black primary buttons on white. Flat surfaces with hairlines,
> generous whitespace, centered columns with a strong max-width. Content tone: professional,
> editorial, confident — the design should feel like a well-typeset magazine.

## 10. Component Map

1. Nav — minimal, logo left, CTA right, transparent→white on scroll.
2. Hero — huge type statement + supporting visual + dark CTA.
3. Logo cloud / proof — quiet band.
4. Features — editorial rows (text + visual alternating).
5. Product/editor — product deep-dive section.
6. Testimonials / social proof — quotes, type-led.
7. Pricing — clean tables/cards, highlighted plan.
8. CTA band — accent or dark moment.
9. Footer — muted links, legal.

## 11. Pattern Position

Best fits the **SaaS landing** pattern (`patterns/saas-landing.md`), specifically the
"text-forward/editorial confidence" hero direction. It proves a developer/product audience
responds to calm type-led SaaS over colorful template-y SaaS.

## 12. Synthesis Notes

- **Unique:** one-family variable typography discipline; black-on-white authority buttons;
  the "publishing-grade" editorial calm; near-zero shadow depth; magenta + lime as tiny
  brand twinkles on a slate-neutral base.
- **Combine with:** the warm dark editorial hero of Wispr (contrast in theme); the bold
  accent discipline of Ramp; a playful bento grid from ClickUp for feature density.
- **Weaknesses / avoid:** can be too plain for consumer/playful brands; very little color
  energy means it relies on copy + photography; avoid copying its exact magenta/lime pairing
  without changing the roles.