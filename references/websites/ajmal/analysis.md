# Ajmal — Design Analysis

> Source: `https://in.ajmal.com/` (Ajmal Perfumes India, Shopify + Tailwind + Headless UI) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/products/buy-3-at-1799/`, 3 oud perfume PDPs)

Ajmal India is a mid-market D2C fragrance storefront on Shopify: warm ivory grounds, bronze-gold CTAs, serif display touches, and review stars everywhere. It is the opposite commerce pole to Apple — rich, dense, promotion-led — while staying AAA on body text.

## 1. Visual Theme & Atmosphere

- Mood: opulent bazaar made orderly — ivory `#FFFBFA`, bronze, gold stars, oud imagery, but inside a disciplined Shopify grid.
- Philosophy: persuasion density — badges, bundles ("buy 3 at 1799"), ratings, and price-reveal animations stack purchase reasons above the fold.
- Light-only theme; no dark mode observed.

## 2. Color Palette & Roles

- Grounds: warm ivory `#FFFBFA` (page) + white `#FFFFFF` (cards/inputs) + `#FCFCFC`/`#FCF8EF` tints.
- Ink: black `#000000` body (19.8–21:1, AAA) + `#242424` (15.52 AAA) + `#262626` neutrals.
- Brand accent: bronze `#BC8B57` / `#BC8A57` — primary CTA fill, badges `#B57D45`, email inputs. Caveat: white on bronze is 3.01 (large-text only) and bronze on white 2.94 (fail) — CTA text rides below AA; size/weight carries it, but do not copy small bronze-on-white text.
- Star gold: `#E5AD23` (`--jdgm-star-color`, Judge.me reviews) — 2.03:1 on white (fail) but stars are non-text decoration; keep them chunky.
- Functional: green `#008000` (in-stock/WhatsApp-style cues), link blue `#1D4ED8` (5.37 AA on `#E6E6E6`), sand `#D8C3A5` at 40% for washes, Tailwind ring blue `#3B82F6`.
- WCAG: body pairs AAA; failures cluster on decorative/CTA golds and disabled states (`#999` on `#DDD` at 2.1).

## 3. Typography Rules

- Trio: Alexandria (100–700, workhorse: 36px H1 down to 9px captions), Philosopher (display serif: 36/28/24/20px for product names and romantic headlines), JudgemeStar-700 (review glyphs), plus Inter/Assistant for app chrome.
- Pairing logic: geometric sans for UI density + high-contrast serif for desirability. Prices often set in Alexandria 600–700 with tabular feel.
- Decision: serif display + sans UI is the affordable-luxury signal. Borrow the pairing, keep body ≥13px (captions at 9–11px are legal/microcopy only).

## 4. Component Stylings

- CTAs: bronze pill-ish (20px radius, 8×15px, white text, `0 4px 12px rgba(0,0,0,.2)` shadow) for add-to-cart; black 4–5px rectangles for secondary/utility; 25px and 30px badge radii for offers.
- Badges: bronze filled (10px, light 300) for offers + black micro (12px) for labels — promotion language is baked into the component set.
- Product cards: 5px radius, `#DDD` 1px borders, layered soft shadows (0.06–0.2 alpha, up to 10px blur); carousel dots 50% round.
- Inputs: pill search (100px radius), bronze newsletter email block, boxed text inputs with dashed cyan focus outline; select dropdowns with soft focus rings.
- Links: black default → blue hover; grey `#7B7B7B` → gold `#E6AB10` hover on editorial links; footer white underlined.
- Price motion: `priceReveal` (0.5s) + `strikeIn` (0.4s) keyframes animate discounts — the sale IS an interaction.

## 5. Layout Principles

- 8px scale with dense sub-steps (1/2/3/4/5/6/7/8/10/12/15/16/20/22px) — Shopify-section packing for collection grids, PDP galleries, and upsell rails.
- Hairline system: `#E5E7EB`/`#EBEBEB`/`#DDDDDD` 1px rules separate sections instead of whitespace alone — density without clutter.
- PDP order: gallery → title (Philosopher) → stars → price + strike → variant/size → bronze CTA → trust badges → accordions → reviews → related.

## 6. Depth & Elevation

- Real shadow system (11 styles): card lift `0 2px 4px rgba(0,0,0,.1)`, CTA `0 4px 12px rgba(0,0,0,.2)`, popover `0 0 10px rgba(0,0,0,.2)`, Tailwind double-layer `0 1px 3px + 0 1px 2px`. Plus 2 linear gradients (subtle washes).
- Decision: shadows sell tactility for un-scentable products — cards and CTAs float off the ivory ground like shelf displays.

## 7. Do's and Don'ts

- Do: bronze CTAs + black secondary; serif product names + sans UI; stars near every price; animate the discount, not the page.
- Do: keep body AAA; keep gold stars large (they fail contrast at small sizes).
- Don't: set small text in bronze-on-white or gold-on-white; don't drop the hairline system (density turns to mush); don't add more families — four (incl. star glyphs) is already the limit.

## 8. Responsive Behavior

- 36-breakpoint ladder (1400→300px, incl. 1024/990/989/900/812/800/769/768/767/761/760/751/750/749/700/680/650/560/501/500/480/460/450/420/391/390/346/320/319/300) — collection grids collapse stepwise to single-column PDPs; pills/inputs stay thumb-sized.
- Carousels advance on mobile (3 advances observed per PDP); menus collapse to 6–8 drawers.

## 9. Agent Prompt Guide

- Quick reference: `ecommerce / affordable-luxury / dense-pdp / light / high complexity / dual CTA (bronze add-to-cart + black secondary)`.
- Ready-to-use prompt: "Design a mid-market D2C storefront in the Ajmal logic: warm ivory grounds with hairline dividers, serif display product names over geometric-sans UI, bronze rounded CTAs with soft lift shadows beside black utility buttons, gold review stars by every price, animated price-reveal and strikethrough discounts, dense PDP stacking (gallery, variants, trust badges, accordions, reviews), and a fine-grained responsive ladder down to 300px. Keep body text AAA; keep gold/bronze text large-only."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Announcement/bundle bar ("buy 3 at 1799") — promotion as header.
2. Nav + pill search + cart — commerce wayfinding.
3. Hero/category bands — campaign imagery.
4. Collection grid (badged cards, stars, prices) — browse density.
5. PDP core (gallery, Philosopher title, stars, priceReveal/strikeIn, variants, bronze CTA).
6. Trust rails (shipping, authenticity, returns) — risk reversal.
7. Reviews (Judge.me stars) — social proof at volume.
8. Related/upsell carousels — basket building.
9. Bronze newsletter block + footer — capture and sign-off.

### 11. Pattern Position

- Fits the commerce pattern (`patterns/ecommerce.md`) in promotion-led form: every viewport answers "why buy now" (bundle, badge, stars, strike price). Where Apple converts through calm and Gumroad through personality, Ajmal converts through stacked proof.
- Page-flow logic: hook (offer) → browse (grid) → desire (PDP serif + imagery) → justify (price animation + reviews) → convert (bronze CTA) → retain (newsletter).

### 12. Synthesis Notes

- Unique (borrow as logic): discount-as-interaction (priceReveal/strikeIn); star-color as a design token; bronze+black dual CTA language; hairline-separated density; serif-for-desire/sans-for-density pairing.
- Combine with: Apple's band rhythm and focus-ring discipline (Ajmal's focus states are weak — Apple's 2px blue ring would fix them) and Gumroad's personality to warm the template feel.
- Avoid: copying the bronze-on-white small text (fails contrast); shrinking stars below legibility; adding dark mode naively (the ivory/bronze system doesn't invert cleanly); removing reviews — they are load-bearing trust.
