# Mobbin — Design Analysis

> Source: `https://mobbin.com/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Mobbin is a product-design reference library (SaaS tool for designers). The page is a
> **clean, current, product-first design** — white canvas, strong sans display type, a
> vivid blue accent, and pill-shaped dark buttons. It looks like the kind of tool a designer
> would respect.

## 1. Visual Theme & Atmosphere

- **Clean and confident.** A white/near-white canvas with crisp dark type and a single vivid
  blue accent (`#0000EE`) for interactive moments.
- **Type-led, product-credible:** a strong grotesque display (M Saans) at 80px / 56px with
  tight leading — modern and precise. Fits a product for designers.
- **Dark anchors:** near-black (`#141414`) pill buttons ground the light design.
- Mood: current, precise, premium-tech, design-credible.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / accent | vivid blue `#0000EE` | Interactive elements, links, highlights |
| Secondary / button | near-black `#141414` | Primary buttons (contrast anchor) |
| Surface | white / light gray `#ADADAD` | Canvas + elevated surfaces |
| Text | dark gray `#404040` | Body/meta |

- **Restraint:** white + dark type + one vivid blue. The blue is the only saturated color —
  the brand signal.
- **Neutral strategy:** clean grays; warm-free (cool, techy).
- **Dark handling:** light-first; near-black used for buttons and select surfaces.

## 3. Typography Rules

- **Families:** M Saans (display, 300-652 variable weights) + M Saans Variable Light (body) +
  Geist Mono (technical mono accents). A single, highly-consistent grotesque family.
- **Display scale:** 80px / 56px / 32px / 24px with `line-height ~1.0-1.25`, tight and bold.
  Headlines rely on **weight + size**.
- **Body:** M Saans Light at 14-16px, `1.38-1.43` leading.
- **Mono accent:** Geist Mono for labels/technical eyebrows — a design-tool signature.
- **Variable weights (300/456/600/652)** give the family a rich, precise scale.

## 4. Component Stylings

- **Primary button:** near-black fill (`#141414`) with white text, fully rounded (pill,
  999px observed), padding 11px × 16px — a clean, flat chip.
- **Secondary:** ghost/outline, blue text.
- **Links:** near-black → vivid blue on hover.
- **Cards:** white surfaces, small shadow (`0 8px 40px` at 4%), generous padding, generous
  radius (16-30px observed).
- **Badges/chips:** rounded, dark or blue.

## 5. Layout Principles

- **Spacing scale:** 8px base with generous steps (4-28px observed) — comfortable rhythm.
- **Grid:** centered, airy; product/library content in rounded cards with strong gaps.
- **Breakpoints:** 1199 / 810 / 809 / 720 / 98 — modern responsive collapse.

## 6. Depth & Elevation

- **Soft, minimal depth:** `0 8px 40px` at 4% for cards, white ring shadows
  (`0 0 0 2px #fff`). Elevation is subtle — content-first.

## 7. Do's and Don'ts

- **Do:** keep the canvas white and clean; use ONE vivid accent; a strong consistent
  grotesque display; pill dark CTAs; generous rounded cards.
- **Don't:** add competing saturated colors; clutter the airy grid; use heavy shadows.

## 8. Responsive Behavior

- Display type fluid-scales; hero collapses cleanly; nav collapses with CTA; cards stack to
  single column; touch targets respected.

## 9. Agent Prompt Guide

> Build a landing page with a **clean, current, product-credible aesthetic**: white canvas,
> dark type, a single vivid blue accent for interactive elements, and a consistent grotesque
> display family (40-80px, tight leading) with a light body weight and a mono accent for
> labels. Near-black pill primary buttons. Rounded cards with subtle soft shadows, generous
> whitespace, centered airy layout. Content tone: precise, premium-tech — a tool designers
> and builders would trust.

## 10. Component Map

1. Nav — minimal, logo left, dark pill CTA right.
2. Hero — strong display statement + product/library visual + CTA.
3. Product/library — rounded cards, mono labels.
4. Features — clean alternating rows.
5. Stats / proof — large numbers.
6. Testimonials — quotes from designers.
7. Pricing — cards, highlighted plan.
8. CTA band — blue or dark moment.
9. Footer — muted, organized.

## 11. Pattern Position

Best fits the **SaaS landing** pattern (`patterns/saas-landing.md`) for a designer-facing
tool. It executes "product-first" credibility: the design itself signals the product
category (design tools) through type, mono accents, and precision.

## 12. Synthesis Notes

- **Unique:** the M Saans variable-weight system; white + one vivid blue economy; pill dark
  CTAs; Geist Mono design-tool signature; rounded card library layout.
- **Combine with:** Ghost's editorial hierarchy for section rhythm; Ramp's accent discipline;
  Wispr's dark warm canvas for a contrasting hero; a serif display from Primora for a more
  editorial voice.
- **Weaknesses / avoid:** can be generic if the blue/white recipe is used without a
  distinctive display type; the clean look relies on strong content; avoid copying its
  exact blue + M Saans-style pairing without changing roles.