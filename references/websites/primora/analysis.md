# Primora — Design Analysis

> Source: `https://primora.xyz/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Primora is a design/creative agency. The page is a **dark, editorial, serif-forward
> statement** — a near-black canvas, a large STK Bureau Serif display, and violet/coral
> accents that make the studio feel premium, experimental, and design-literate.

## 1. Visual Theme & Atmosphere

- **Dark, editorial, premium.** A near-black canvas with large serif display type — a
  deliberate "design studio" aesthetic, confident and art-directed.
- **Serif as identity:** STK Bureau Serif at 96px / 74px / 53px / 42px, tight leading,
  editorial. It signals "we are designers who care about typography."
- **Accent moments:** violet (`#8827DD`) and coral (`#F96D57`) appear as small, deliberate
  highlights — the energy points on a dark stage.
- Mood: premium, experimental, confident, design-credible.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / accent | violet `#8827DD` | Identity + highlights |
| Secondary | gray `#B6B2B8` | Muted structure |
| Tertiary | coral `#F96D57` | Secondary accents, CTAs |
| Surface | dark gray `#635F65` | Elevated surfaces on dark |
| Text / on-surface | near-black `#2B282D` | Dark canvas base |

- **Dark-first palette:** near-black canvas with gray surfaces; violet + coral as the two
  accents. Premium and editorial.
- **Neutral strategy:** warm-tinted dark grays — never pure black.
- **Dark handling:** dark is the base; light text (`#EFEDF0`) for contrast.

## 3. Typography Rules

- **Families:** STK Bureau Serif (display serif, 400) + Inter (body, 400-500) + Geist Mono
  (technical mono accents). A classic editorial + tech pairing.
- **Display scale:** 96px / 74px / 53px / 42px / 32px with `line-height ~1.0-1.2`, tight and
  refined. Headlines rely on **serif elegance + size**.
- **Body:** Inter at 18-21px, `1.5` leading.
- **Mono accent:** Geist Mono for labels, eyebrows, meta — the design-tool signature.

## 4. Component Stylings

- **Primary button:** dark fill (`#100E11`) with light text (`#EFEDF0`), ~8px radius, with a
  hairline border — refined and quiet.
- **Secondary:** ghost/outline.
- **Links:** light → violet/coral on hover.
- **Cards:** dark elevated surfaces, small radius, hairline edges.
- **Badges:** violet/coral small pills.

## 5. Layout Principles

- **Spacing scale:** 8px base with micro steps (2.6-10px observed); large section padding.
- **Grid:** editorial, asymmetric; full-width serif statements with strong negative space.
- **Breakpoints:** 992 / 991 / 768 / 767 / 479 — mobile-first collapse.

## 6. Depth & Elevation

- **Inset, subtle depth:** `0 0 0 1px inset` hairlines and violet glow insets
  (`0 53px 74px 32px inset`) — depth is atmospheric, not boxy.

## 7. Do's and Don'ts

- **Do:** lead with a large serif display; keep the canvas dark and warm; use two accents
  sparingly; mono labels for tech credibility.
- **Don't:** use a default techy sans headline; flood with color; use harsh pure black
  (tint it); make it look like a template.

## 8. Responsive Behavior

- Serif display fluid-scales; editorial sections collapse to stacked columns; nav collapses
  with CTA; mono labels remain legible.

## 9. Agent Prompt Guide

> Build a landing page with a **dark, editorial, design-studio aesthetic**: warm near-black
> canvas, light text, a large serif display (STK Bureau-style) at 42-96px with tight leading,
> and Inter body at 18-21px with a Geist Mono accent for labels. Use violet and coral-style
> accents sparingly for highlights and CTAs. Dark elevated cards with hairline borders,
> inset atmospheric depth, generous whitespace, asymmetric editorial layouts. Content tone:
> premium, experimental, design-credible.

## 10. Component Map

1. Nav — minimal dark, logo, muted links.
2. Hero — large serif statement + mono label + CTA.
3. Work / services — editorial serif section headers.
4. Selected projects — dark cards, mono meta.
5. Process — numbered editorial steps.
6. Clients / logos — quiet band.
7. Contact / CTA — violet or coral moment.
8. Footer — muted, mono accents.

## 11. Pattern Position

Best fits the **portfolio/agency** pattern (`patterns/portfolio-agency.md`): work-forward,
point-of-view hero, craft demonstrated through typography. It executes the "serif editorial
over techy template" differentiation for a design studio.

## 12. Synthesis Notes

- **Unique:** dark editorial serif identity for a design studio; STK Bureau Serif scale;
  violet + coral on warm near-black; inset atmospheric depth; mono accent for
  design-tool credibility.
- **Combine with:** Ghost's editorial hierarchy for section rhythm; Wispr's warm dark canvas
  (different accent logic); Ramp's accent discipline for CTA energy.
- **Weaknesses / avoid:** can feel niche/artsy for mainstream products; serif scale needs
  strong art direction; avoid copying its exact violet/coral on dark without changing roles.