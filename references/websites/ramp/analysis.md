# Ramp — Design Analysis

> Source: `https://ramp.com/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Ramp is a corporate card & spend-management fintech. The marketing page is a masterclass
> in **black + one electric accent**: premium, precise, high-contrast — banking-grade
> confidence without banking conservatism.

## 1. Visual Theme & Atmosphere

- **Black and acid.** A pure-black primary (`#0C0A08` on white surface) paired with an
  electric acid-lime accent (`#E4F222`). The result is immediate, unmistakable, premium.
- **Precision & scale:** large statement type, generous whitespace, and an almost brutalist
  confidence. The design says "we are serious about money, and we own our aesthetic."
- **Single accent discipline:** the acid lime is reserved for CTAs and key highlights — the
  whole page feels like the accent is the only color that matters.
- Mood: confident, premium, sharp, financial-but-not-boring.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / accent | acid lime `#E4F222` | The ONLY action color — CTAs, highlights |
| Neutral | warm gray `#D2CECB` | Secondary surfaces, muted structure |
| Surface | white `#FFFFFF` | Page canvas |
| Text | near-black `#0C0A08` | Headlines + body (warm-tinted black) |

- **Extreme economy:** four roles max. Black text on white + lime accent. This restraint is
  the brand.
- **Neutral strategy:** warm gray (not cool) — keeps the premium, non-technical feel.
- **Dark handling:** predominantly light-first with black type; dark panels used as
  deliberate contrast bands.
- Text is **warm black**, never pure `#000` — slightly softer, premium.

## 3. Typography Rules

- **Family:** Lausanne — a single, distinctive grotesque. One family, differentiated by size
  and weight (mostly 300-700). Monospaced/technical accents for data/eyebrows where useful.
- **Display scale:** 64px / 48px / 40px / 28px with `line-height ~1.0-1.14`, tight and bold.
  Headlines lean on **size + tight leading**.
- **Body:** 16-18px, `1.5` leading, comfortable measure.
- **Labels:** small (10-14px), muted — eyebrows, meta, legal stay quiet and precise.
- **Tabular figures** for numbers (fintech) so prices/figures align.

## 4. Component Stylings

- **Primary button:** lime fill (`#E4F222`) with near-black text, small radius (~6px),
  tight padding — a confident, flat "press me" chip.
- **Secondary button:** ghost/outline, black text, quiet.
- **Cards:** white or warm-gray surfaces, hairline borders, minimal shadow.
- **Inputs:** white fill, 10px radius, bordered.
- **Badges/stats:** large numbers, black, lime highlight for the key figure.

## 5. Layout Principles

- **Spacing scale:** 8px base, tight micro steps (1-24px observed) with large section
  padding — precise rhythm, generous negative space.
- **Grid:** strong grid, asymmetric editorial compositions; large type + empty space = premium.
- **Breakpoints:** 600 / 500 / 480 / 449 — aggressive responsive collapse to mobile.
- **Section rhythm:** statement headline → supporting copy → one lime CTA.

## 6. Depth & Elevation

- **Flat-first with layered shadows** for depth moments: stacked soft shadows
  (`0 35px 59px` at 3%, `0 20px 50px` at 9%) used to float cards/dialogs. Mostly the design
  is confident flat surfaces with hairlines.

## 7. Do's and Don'ts

- **Do:** commit to black + ONE electric accent; large type + whitespace; precise fintech
  copy; flat buttons; tabular numbers.
- **Don't:** add a second competing accent; use gradients on buttons; make the page busy;
  use default banking navy/blue (this is the differentiation).

## 8. Responsive Behavior

- Huge display type fluid-scales; asymmetric hero collapses to single column.
- Nav collapses to hamburger, CTA retained; cards stack.
- Touch targets ≥44px; tables/numbers remain readable on mobile.

## 9. Agent Prompt Guide

> Build a landing page with a **black + one acid accent aesthetic**: white canvas, near-black
> (warm-tinted) type, and a single electric lime-style accent used ONLY for primary CTAs and
> key highlights. Use one distinctive grotesque sans family for display (40-64px, tight
> leading) and body (16-18px, 1.5). Flat surfaces, hairline borders, generous whitespace,
> precise fintech copy with tabular figures. Content tone: sharp, confident, premium —
> financial authority without navy-blue conservatism.

## 10. Component Map

1. Nav — transparent→white blur; black logo; lime CTA.
2. Hero — big statement type + product/visual + lime CTA.
3. Logo cloud / trust — customers, quiet band.
4. Features / product — split rows, black type, lime highlights.
5. Stats — large numbers with lime key figure.
6. Testimonials — editorial quotes, faces/logos.
7. Pricing — cards, highlighted plan, lime CTA.
8. CTA band — black or lime moment.
9. Footer — muted, legal links.

## 11. Pattern Position

Best fits the **fintech** pattern (`patterns/fintech.md`): trust-forward hero, precise
numbers, transparent pricing. It executes the "bold accent over institutional navy"
differentiation move for fintech perfectly.

## 12. Synthesis Notes

- **Unique:** the acid-lime-on-black brand system; extreme color economy; premium
  "anti-banking" fintech confidence; warm-black type; tabular figures discipline.
- **Combine with:** Wispr's warm editorial serif (contrast pairing for an AI brand);
  Ghost's type-led calm; a playful accent from Gumroad for consumer energy.
- **Weaknesses / avoid:** the look depends entirely on the accent choice — a wrong accent
  reads generic; can feel too stark for playful/consumer brands; avoid copying its exact
  lime + black without changing the roles.