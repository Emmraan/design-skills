# ClickUp — Design Analysis

> Source: `https://clickup.com/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> ClickUp is a feature-heavy productivity SaaS. The marketing page is a masterclass in
> **scale and energy**: huge colorful type, saturated brand colors, and dense but organized
> feature storytelling that never feels cluttered.

## 1. Visual Theme & Atmosphere

- **Bold, vibrant, energetic.** A light canvas with saturated purple/blue brand colors and
  near-black buttons. It feels like a productivity tool that is also *fun*.
- **Scale as identity:** enormous display type (80px / 76px / 60px), tight leading, big
  statement headlines — the layout is loud and confident.
- **Color everywhere but controlled:** purple primary, blue secondary, and a light blue
  surface are used as brand washes; the black button is the counterweight that keeps it
  grounded.
- Mood: energetic, premium, feature-forward, trustworthy-fun.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / brand | purple `#6647F0` | Identity + primary interactive elements |
| Secondary | indigo `#7B68EE` | Brand support, secondary surfaces |
| Tertiary | blue `#0091FF` | Additional brand accent, links/highlights |
| Surface | light blue `#EDF6FD` | Card/panel surfaces |
| Text | near-black `#000000` | Headlines/body |

- **Brand-first palette:** saturated purple/indigo/blue family creates an instant brand
  identity. Text stays near-black for contrast.
- **Neutral strategy:** light blue-tinted surfaces keep the cool, techy feel.
- **Dark handling:** light-first primarily; dark panels used as deliberate contrast bands.

## 3. Typography Rules

- **Families:** Plus Jakarta Sans (headlines, 400-700/650) + Inter (body) + Sometype Mono
  (technical/data labels) + Shantell Sans (playful accents). A structured multi-family system.
- **Display scale:** 80px / 76px / 60px / 56px / 52px with `line-height ~1.05-1.2`, tight and
  bold. Headlines rely on **weight (700) + size**.
- **Body:** Inter at 14-18px, `1.5` leading.
- **Mono accent:** Sometype Mono for eyebrows, stats, technical labels — a developer-friendly
  signature.
- **Feature-rich scale:** the 90+ text styles show a very complete type system — a big-team
  product.

## 4. Component Stylings

- **Primary button:** near-black fill (`#202020`) with white text, ~15px radius, padding
  14px × 20px. Bold, grounded, stands out against color washes.
- **Secondary:** ghost/outline, brand-purple text.
- **Cards:** light-blue surface, small radius, hairline/shadow edges, generous padding.
- **Badges:** purple/blue filled pills.
- **Inputs:** white fill, bordered, small radius.

## 5. Layout Principles

- **Spacing scale:** 8px base with tight micro steps (1-7px observed); large section
  padding for breathing room.
- **Grid:** bento-style and alternating rows dominate; dense feature grids organized with
  clear columns and generous gaps.
- **Breakpoints:** 450 / 426 / 425 / 400 / 395 / 300 — very mobile-aware.
- **Section rhythm:** big statement → feature grid → proof → pricing, repeated.

## 6. Depth & Elevation

- **Subtle shadows:** `0 1px 3px` at 10% for cards; inset accent glows for highlights.
  Mostly flat with color washes doing the depth work.

## 7. Do's and Don'ts

- **Do:** commit to a saturated brand palette; use near-black buttons for contrast; build a
  complete type system with a mono accent; organize dense features with bento grids.
- **Don't:** let color compete with text (near-black text on saturated washes only); use
  weak contrast; make the dense grid feel cramped.

## 8. Responsive Behavior

- Huge display type fluid-scales; bento reflows to single column on mobile; nav collapses
  with CTA retained; touch targets respected.

## 9. Agent Prompt Guide

> Build a landing page with a **bold, vibrant, feature-forward aesthetic**: light canvas with
> a saturated purple/indigo/blue brand palette, near-black primary buttons, and huge display
> type (60-80px, weight 700, tight leading). Use a sans display family + a clean body sans +
> a mono accent for technical labels. Organize features with bento grids and alternating
> rows, dense but airy. Content tone: energetic, premium, confident — a fun but serious
> productivity tool.

## 10. Component Map

1. Nav — logo, links, bold black CTA.
2. Hero — huge type statement + product UI visual + CTA.
3. Logo cloud / trust — customer band.
4. Feature bento — saturated color cells, organized grid.
5. Product deep-dive — alternate rows, screenshots.
6. Stats — large numbers, mono labels.
7. Testimonials — quotes with logos.
8. Pricing — cards, highlighted plan, black CTA.
9. CTA band — brand moment.
10. Footer — muted, organized.

## 11. Pattern Position

Best fits the **SaaS landing** pattern (`patterns/saas-landing.md`) with a bento feature
grid. It shows how a feature-heavy product stays organized with strong color systems and
type discipline.

## 12. Synthesis Notes

- **Unique:** the complete multi-family type system; saturated purple/indigo/blue identity;
  near-black buttons against color washes; bento-grid density done right; the mono accent
  for technical detail.
- **Combine with:** Ghost's editorial restraint for hierarchy; Ramp's accent discipline;
  Wispr's dark warm canvas for a contrasting hero.
- **Weaknesses / avoid:** the saturated palette can read noisy for premium/calm brands;
  density needs strong organization or it feels chaotic; avoid copying its exact purple/blue
  family without changing roles.