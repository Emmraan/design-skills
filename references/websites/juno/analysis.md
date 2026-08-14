# Juno — Design Analysis

> Source: `https://www.withjuno.com/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Juno is an employee wellbeing, recognition & rewards platform (HR-tech). The page is a
> study in **warm, human, playful design for an enterprise audience**: a coral-led palette
> with mint and gold accents that feels welcoming, not corporate.

## 1. Visual Theme & Atmosphere

- **Warm and approachable.** A light canvas with a coral primary (`#FE7A53`), mint
  secondary (`#E5F6ED`), and warm gold (`#FECE30`) accents. It reads friendly, human, and
  optimistic — a counter to gray enterprise software.
- **Round and soft:** large-radius buttons, pill shapes, rounded cards — friendly geometry.
- **Black buttons anchor it:** near-black CTAs against the warm palette keep it from being
  too sugary.
- Mood: warm, human, playful, trustworthy.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / brand | coral `#FE7A53` | Identity + primary accents |
| Secondary | mint `#E5F6ED` | Soft surfaces, backgrounds, support |
| Tertiary | gold `#FECE30` | Additional accent, rewards/highlights |
| Surface | cream `#FFF5D6` | Warm surfaces, cards |
| Text | gray `#333333` | Body/headline (soft, not black) |

- **Warm brand palette:** coral + mint + gold is a distinctive, friendly identity. Text uses
  soft gray (`#333`) rather than harsh black — keeps the warmth.
- **Neutral strategy:** cream/mint-tinted surfaces — always warm, never clinical.
- **Dark handling:** primarily light-first; minimal dark usage.

## 3. Typography Rules

- **Families:** TT Travels Next (display, 800 weight) + TT Travels Text (body, 400-700) +
  fallback sans. An extra-bold geometric display pairing.
- **Display scale:** 76px / 48px / 39px / 24px with `line-height ~1.0-1.3`, extra-bold and
  tight. Headlines rely on **weight (800) + size**.
- **Body:** 15-16px, `1.5` leading.
- **Bold display voice:** the 800-weight headlines give a friendly-but-strong personality.

## 4. Component Stylings

- **Primary button:** near-black fill with white text, fully rounded (pill), padding 12px ×
  16px — a bold anchor on the warm palette.
- **Secondary:** soft mint/coral tints.
- **Cards:** cream/mint surfaces, rounded corners, soft shadows.
- **Badges/chips:** rounded, gold/coral fills.

## 5. Layout Principles

- **Spacing scale:** 8px base with micro steps (3-12px observed); large section padding for
  air.
- **Grid:** centered columns with warm-colored section bands; cards arranged in friendly,
  rounded grids.
- **Breakpoints:** 991 / 768 / 767 / 601 / 600 / 479 — aggressive mobile-first collapse.

## 6. Depth & Elevation

- **Soft, friendly shadows:** `4px 4px 20px` at 9%, `0 30px 70px` at 30% for elevated
  cards — soft and round, matching the geometry.

## 7. Do's and Don'ts

- **Do:** use a warm, human palette; extra-bold friendly display type; soft rounded
  geometry; near-black CTAs to anchor; warm-tinted surfaces.
- **Don't:** go corporate-gray; make the palette sugary without a dark anchor; use harsh
  black text; use sharp/angular geometry.

## 8. Responsive Behavior

- Display type fluid-scales; cards stack; nav collapses with CTA retained; soft rounded
  touch targets maintained.

## 9. Agent Prompt Guide

> Build a landing page with a **warm, human, playful aesthetic**: light canvas with a coral
> primary, mint secondary, and gold accent, on cream/mint-tinted surfaces. Use an extra-bold
> geometric display sans for headlines (40-76px, weight 800, tight leading) with a clean body
> sans at 15-16px. Near-black pill-shaped CTAs as the contrast anchor. Rounded cards, soft
> shadows, generous whitespace. Content tone: friendly, optimistic, human — wellbeing-grade,
> not corporate.

## 10. Component Map

1. Nav — warm transparent → white blur; dark CTA.
2. Hero — friendly headline + product/visual + dark pill CTA.
3. Value props — mint/cream cards, rounded.
4. Features — warm bands, alternating.
5. Recognition/rewards — gold highlights.
6. Testimonials — warm quotes.
7. Pricing — rounded cards, highlighted plan.
8. CTA band — coral or dark moment.
9. Footer — warm, muted.

## 11. Pattern Position

Best fits the **SaaS landing** pattern (`patterns/saas-landing.md`) for an HR/employee
platform, executed in the "playful/warm" style direction. It shows enterprise buyers can be
served with human warmth, not gray corporate software.

## 12. Synthesis Notes

- **Unique:** the coral+mint+gold warm identity for an enterprise product; extra-bold 800
  display voice; soft rounded geometry + shadows; warm-tinted surfaces instead of gray.
- **Combine with:** Ramp's accent discipline for restraint; Ghost's type hierarchy; a mono
  accent from ClickUp for product density.
- **Weaknesses / avoid:** can feel too friendly for serious/fintech contexts; the warm
  palette needs the dark CTA anchor or it loses contrast; avoid copying its exact
  coral/mint/gold without changing roles.