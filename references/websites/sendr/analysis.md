# Sendr — Design Analysis

> Source: `https://www.sendr.ai/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Sendr is an AI product (sendr.ai). The page pairs **clean, modern sans typography with
> unexpected handwriting accents** — a light canvas, near-black type, a vivid blue accent,
> and playful scribbled annotations that make the AI feel approachable and human.

## 1. Visual Theme & Atmosphere

- **Clean and current.** A white/near-white canvas with strong sans display type and a vivid
  blue accent (`#0000EE`) for interactive moments.
- **Human touch:** handwriting-style fonts (Caveat, Nanum Pen Script) appear as annotation
  accents — like a human circled a note on a whiteboard. This warmth softens the "AI" coldness.
- **Premium tech:** near-black (`#19191D`) type, generous whitespace, and a distinct editorial
  serif display (Hedvig Letters Serif) for select statements.
- Mood: clean, modern, warm-tech, editorial.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / text | near-black `#19191D` | Headlines, structure |
| Accent / link | vivid blue `#0000EE` | Interactive, links, highlights |
| Surface | white `#FFFFFF` | Canvas |
| Text secondary | dark gray `#151517` | Body/meta |

- **Economy:** white + near-black + one vivid blue. The handwriting fonts provide the
  "color" of personality rather than a bright palette.
- **Neutral strategy:** near-black with warm tint; clean grays.
- **Dark handling:** light-first; dark surfaces used sparingly as contrast bands.

## 3. Typography Rules

- **Families:** Inter Display (display, 400-700) + Hedvig Letters Serif (editorial display
  serif for statements) + Inter Variable (body) + handwriting accents (Caveat, Nanum Pen
  Script). A contemporary mixed system.
- **Display scale:** 64px / 60px (serif) / 40px with `line-height ~1.0-1.1`, tight and bold.
- **Body:** Inter at 14-17px, `1.5` leading.
- **Signature move:** the serif display (Hedvig) for key statements + handwriting annotations
  — a memorable editorial + human combo.

## 4. Component Stylings

- **Primary button:** white fill with vivid blue text (observed), ~10px radius, flat — a
  clean, modern chip.
- **Secondary:** ghost/outline, near-black text.
- **Links:** near-black → vivid blue on hover.
- **Cards:** white surfaces, hairline/shadow edges, generous padding.
- **Inputs:** bordered, small radius.

## 5. Layout Principles

- **Spacing scale:** 8px base with micro steps (0.3-10px observed); large section padding.
- **Grid:** centered, airy columns; the editorial serif statement sections break the rhythm
  as full-width bands.
- **Breakpoints:** 1400 / 1200 / 1199 / 975 / 810 — modern responsive collapse.

## 6. Depth & Elevation

- **Near-flat with hairline borders:** subtle 0.5px+ layered shadows for elevation. Depth is
  minimal; whitespace and type carry the design.

## 7. Do's and Don'ts

- **Do:** pair clean sans with an editorial serif + handwriting accents; use one vivid
  accent; keep a light, airy canvas.
- **Don't:** overload with color; make the handwriting fonts the main text (keep as accents);
  use default AI gradients.

## 8. Responsive Behavior

- Display and serif type fluid-scale; hero collapses cleanly; nav collapses with CTA;
  annotations (handwriting) remain legible at mobile.

## 9. Agent Prompt Guide

> Build a landing page with a **clean, modern, human-tech aesthetic**: white canvas,
> near-black type, a single vivid blue accent for interactive elements, and playful
> handwriting-style annotations as accents (a human circled a note). Use a clean sans display
> (40-64px, bold, tight leading) with an editorial serif for key statements and a body sans at
> 14-17px. Flat surfaces with hairlines, generous whitespace. Content tone: current,
> approachable, premium-tech — an AI product that feels warm, not cold.

## 10. Component Map

1. Nav — minimal, logo left, blue accents on interactive.
2. Hero — bold sans headline + serif statement + handwriting annotation + CTA.
3. How it works — editorial steps with annotations.
4. Features — clean cards.
5. Product deep-dive — AI in action.
6. Testimonials — warm quotes.
7. Pricing — clean cards, highlighted plan.
8. CTA band — blue moment.
9. Footer — muted.

## 11. Pattern Position

Best fits the **AI product** pattern (`patterns/ai-product.md`) with the "human/approachable
AI" differentiation — annotations and handwriting soften the product, and the serif display
adds editorial confidence.

## 12. Synthesis Notes

- **Unique:** the sans + editorial serif + handwriting-annotation combo; near-black type on
  white with a single vivid blue; the "human circled a note" warmth for AI.
- **Combine with:** Wispr's dark warm canvas for a contrasting hero; Ramp's accent
  discipline; Ghost's editorial type hierarchy.
- **Weaknesses / avoid:** handwriting fonts as body text would hurt readability; the clean
  look can be generic without the serif/annotation signature; avoid copying its exact
  blue + serif combo without changing roles.