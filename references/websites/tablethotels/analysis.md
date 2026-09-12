# Tablet Hotels — Design Analysis

> Source: `https://www.tablethotels.com/` (curated boutique hotels + Tablet Plus loyalty + magazine) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/tablet-trips`, `/tablet-plus`, `/en/hotels-on-sale`, `/magazine/en/`)

Tablet is curation-as-commerce: monochrome chrome, Playfair display headlines, Figtree UI, and photography that does all the seducing. The loyalty program (Tablet Plus), sale rails, trips, and a WordPress magazine all share one quiet system — selection is the luxury.

## 1. Visual Theme & Atmosphere

- Mood: gallery gift-shop for stays — black/white restraint, serif headlines, vivid hotel photography, loyalty lavender whispering upstairs.
- Philosophy: the edit is the product — every surface (trips, plus, sales, magazine) re-presents the same curated inventory through a different lens.
- Light-only; four engines (storefront, trips, loyalty, WP magazine) in one token family.

## 2. Color Palette & Roles

- Chrome: black `#000000` (21 AAA) / ink `#111111` (18.88) / `#333333` (12.63) on white; reversed white-on-`#222222` 15.91; stone `#E5E3DF` beds (16.38 with black).
- Neutrals: `#666666`, `#999999` (large-only 4.43 on charcoal), `#CCCCCC` hairlines; fails: `#AAAAAA` on white 2.32, black-on-`#333333` 1.66, disabled pairs — all non-text chrome.
- Accents (rationed): sky `#6AAAE4`, WP blues `#007CBA`/`#006BA1`/`#005A87`, orange `#E25F05`, purple `#8D198B`, loyalty lavender `#F3EAF7`, sale red `#E52D27` (4.43 large-only).
- Links: 7 styles, all resolving to cornflower `#3860BE` + underline on hover — the same hover hue Aman uses; a boutique-hotel convention worth noting.

## 3. Typography Rules

- Pairing: Playfair Display (62/40px campaign serif) + Figtree family (SemiBold 32→14 headings, Regular 24→10 UI, Medium 22→12; weights 500–700) + Roboto/Google Sans Text for app chrome.
- Logic: high-contrast Didone-style serif for desire, geometric-humanist sans for booking tasks. Magazine pages lean serif; transactional pages lean Figtree.
- Decision: editorial serif + systematic sans is the curation signal — borrow for any selective-commerce concept.

## 4. Component Stylings

- CTAs: charcoal pills (30/60px, 8×30px, white text, lift shadow on primary) + white secondary (6px, 12×16px; 100px pill with `#CCC` border) + lavender Plus chips + segmented joined controls (`0 4px 4px 0` / `8 0 0 8`).
- Cards: 8/12px hotel cards with `#CCC` hairlines and grey lift shadows; 100% round gallery arrows; 10px dialogs; 2–4px utility radii.
- Inputs: search-first, 8px email/password with `#FCFCFC` fills; focus inverts to cyan `#1EAE DB` + black outline — the most distinctive focus treatment observed; selects and checkboxes share it.
- Galleries: round prev/next over photography with scrim gradients (43 linear uses) for legible captions.

## 5. Layout Principles

- 8px scale (1/2/4/5/6/8/10/12/15/16/20/24/25/40px) across storefront, trips, loyalty, and magazine skins.
- Collection-led flow: hero search → curated collections → sale rails → Plus loyalty upsell → trips editorial → magazine stories → footer. Every page re-slices the same inventory.
- 14–16 dropdown menus per page; magazine runs WordPress blocks inside the same chrome.

## 6. Depth & Elevation

- Six grey shadows (0.06–0.2, up to 32px blur) + scrim gradients over photography. Cards float on white; photos carry gradient captions; loyalty surfaces glow lavender.
- Decision: monochrome elevation (greys only, no colored shadows) keeps photography color-true — the inventory's hues are never polluted.

## 7. Do's and Don'ts

- Do: AAA ink pairs; Playfair/Figtree pairing; charcoal pills + white secondary; scrim gradients for photo text; cyan-black focus visibility; 33-step responsive ladder.
- Do: keep sale reds/oranges to large flags; keep `#AAA` greys decorative.
- Don't: add brand hues to the chrome (accents live in photos and flags); don't flatten gallery arrows (round controls read "browse"); don't drop the magazine — editorial is the retention engine.

## 8. Responsive Behavior

- 33-breakpoint ladder (1281→300px) — collection grids collapse stepwise; segmented controls stack; gallery arrows persist; pills stay tappable.
- Touch: swipe galleries, full-width search, floating button intro (0.8s) for assistance.

## 9. Agent Prompt Guide

- Quick reference: `hospitality / curated-boutique / curation-grid / light / high complexity / dual CTA (book + Tablet Plus)`.
- Ready-to-use prompt: "Design a curated boutique-hotel page in the Tablet logic: monochrome AAA chrome with Playfair display headlines and Figtree UI, charcoal pill CTAs with white secondary, 8/12px photography cards with scrim-gradient captions and round gallery arrows, loyalty surfaces in whisper lavender, sale flags in rationed red/orange, cyan-black focus treatment, grey-only shadows, and a 33-step responsive ladder. The edit is the product — every surface re-slices one curated inventory."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Search hero (destination/dates/guests) — intent jewelry.
2. Curated collections (themed edits) — selection as content.
3. Sale rails (`/en/hotels-on-sale`) — urgency without noise.
4. Tablet Plus (lavender loyalty) — membership upsell.
5. Tablet Trips (itinerary editorial) — plan-level inspiration.
6. Magazine (WordPress storytelling) — SEO + retention.
7. Hotel PDPs (galleries, reviews, book) — conversion core.
8. Footer — quiet sitemap.

### 11. Pattern Position

- Fits the curation-commerce pattern: select → present (collections) → persuade (sales/Plus) → inspire (trips/magazine) → convert (PDP). Against Aman (single-brand sanctuary) and Flyward (single-service aviation), Tablet is multi-inventory curation — the three together span sanctuary, service, and selection.
- Page-flow logic: never show unfiltered inventory; every listing arrives pre-justified by an edit, a sale, a trip, or a story.

### 12. Synthesis Notes

- Unique (borrow as logic): edit-as-inventory (collections/trips/magazine as browse modes); loyalty as a color (lavender surfaces); cyan-black focus inversion; segmented joined controls; monochrome-elevation discipline; magazine-inside-commerce retention.
- Combine with: Aman's stillness and single-button discipline (Tablet's densest grids need sanctuary breaks) and MakeMyTrip's widget urgency (Tablet's calm could convert faster with a floating search).
- Avoid: copying the black/Playfair/Figtree formula verbatim (reads "Tablet clone"); small grey text (fails); colored shadows over photography; unfiltered inventory grids — curation is the whole point.
