# Gumroad — Design Analysis

> Source: `https://gumroad.com/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Gumroad is a marketplace for selling digital products. The page is a **maximalist,
> playful celebration of color and type** — enormous ABC Favorit type, saturated
> yellow/lime/pink accents, and a light canvas that feels like a fun brand poster.

## 1. Visual Theme & Atmosphere

- **Bold, playful, loud.** Huge type (up to 192px!), a light canvas, and saturated accent
  colors (yellow `#FFC900`, lime `#F1F333`, pink `#FF90E8`).
- **Type IS the design:** enormous ABC Favorit headlines dominate; layout is centered and
  poster-like. It feels like a fun consumer brand — "selling digital goods should be fun."
- **Color as accents, not floods:** the bright colors appear in buttons, highlights, and
  brand moments against white.
- Mood: playful, confident, creative, consumer-friendly.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / accent | yellow `#FFC900` | Identity + CTAs |
| Secondary | lime `#F1F333` | Secondary accents |
| Tertiary | pink `#FF90E8` | Buttons, playful highlights |
| Surface | white `#FFFFFF` | Canvas |
| Text / on-surface | red `#DC341E` | Accent text, highlights |

- **Playful brand palette:** yellow + lime + pink is high-energy and consumer-friendly. The
  canvas stays white so the accents pop.
- **Neutral strategy:** white with occasional red/muted text for contrast.
- **Dark handling:** light-first; dark surfaces rare.

## 3. Typography Rules

- **Family:** ABC Favorit throughout — a distinctive grotesque with character. One family,
  differentiated by weight (400-700) and enormous size.
- **Display scale:** 192px / 96px / 72px / 60px / 48px with `line-height ~0.9-1.25`,
  oversized and tight. Headlines rely on **sheer scale** — the signature.
- **Body:** 16-20px, `1.4-1.6` leading.
- **Signature move:** the 192px display type — poster-scale typography is the brand.

## 4. Component Stylings

- **Primary button:** saturated fill (pink/yellow observed) with black text, small radius
  (~4-6px), bordered — playful chips.
- **Secondary:** outlined, black text.
- **Cards:** white surfaces, hairline/shadow edges, rounded corners (16-24px observed).
- **Badges:** bright color pills.

## 5. Layout Principles

- **Spacing scale:** 8px base with generous steps (4-48px observed) — the largest spacing
  scale of the set, matching the big type.
- **Grid:** centered, poster-like; big blocks with lots of whitespace; asymmetric playful
  moments.
- **Breakpoints:** 2000px observed (limited extraction) — the layout is primarily large
  centered poster sections.

## 6. Depth & Elevation

- **Near-flat with playful borders:** 1px solid black borders observed on buttons — a
  bold, graphic, "sticker" quality. Minimal shadows.

## 7. Do's and Don'ts

- **Do:** commit to poster-scale type; use saturated playful accents against white; graphic
  borders on buttons; a distinctive single display family.
- **Don't:** let the size become unreadable on mobile; use the bright colors as text floods;
  clutter the poster rhythm.

## 8. Responsive Behavior

- The 192px type fluid-scales dramatically; poster sections collapse to stacked cards;
  buttons stay thumb-friendly; brightness contrast maintained.

## 9. Agent Prompt Guide

> Build a landing page with a **playful, maximalist, poster-like aesthetic**: white canvas,
> enormous display type (up to 150-200px, tight leading), and saturated accent colors
> (yellow/lime/pink-style) used for CTAs and highlights. Use one distinctive grotesque
> family for display and body, differentiated by size and weight. Graphic bordered buttons,
> rounded cards, generous whitespace, centered poster sections. Content tone: fun, bold,
> creative — a consumer brand, not a corporate product.

## 10. Component Map

1. Nav — playful logo, links, bright CTA.
2. Hero — poster-scale headline + product/CTA.
3. How it works — playful editorial steps.
4. Features — bright cards.
5. Testimonials / creators — bold quotes.
6. Pricing — graphic cards, highlighted plan.
7. CTA band — bright moment.
8. Footer — playful, muted accents.

## 11. Pattern Position

Best fits the **ecommerce** pattern (`patterns/ecommerce.md`) for digital products, executed
in the "playful/consumer" style. It proves digital-commerce can be a bold brand poster
rather than a neutral storefront.

## 12. Synthesis Notes

- **Unique:** poster-scale 192px type; yellow+lime+pink saturated identity on white;
  graphic 1px-black-bordered buttons; the "fun consumer brand" energy for a marketplace.
- **Combine with:** Ramp's accent discipline (restraint); Ghost's editorial hierarchy;
  Wispr's dark warm canvas for a contrasting hero.
- **Weaknesses / avoid:** oversized type needs very strong copy to justify; can be too loud
  for B2B/premium; avoid copying its exact yellow/pink + 192px look without changing roles.