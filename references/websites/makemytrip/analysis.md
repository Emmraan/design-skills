# MakeMyTrip — Design Analysis

> Source: `https://www.makemytrip.com/` (Indian OTA — flights, hotels, packages) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 4 rich pages: `/`, `/about-us.php`, careers, `/about-us/work-from-home.php`; `/blog` redirected to an empty `install.php` and contributed no tokens)

MakeMyTrip is the dense booking-counterpart to Airbnb's calm marketplace: a blue/red conversion engine with a floating search widget, 12 homepage carousels, gradient campaign banners, and three typefaces covering UI, display, and handwritten warmth.

## 1. Visual Theme & Atmosphere

- Mood: bustling travel bazaar with a trustworthy cashier — promotions everywhere, but the search widget and price logic stay legible.
- Philosophy: conversion density done responsibly — body text holds AAA while decoration (gradients, carousels, display type) carries the excitement.
- Light-only; manifest black theme-color with white background (PWA shell).

## 2. Color Palette & Roles

- Primary: booking blue `#008CFF` (CTAs, links; 3.39 on white = large/bold-only — CTAs comply by size) + deep blues `#0055B7` / `#124680` for text-on-light actions + ink `#4A4A4A` body (8.86 AAA) + blacks AAA.
- Grounds: `#F2F2F2` page bed + white cards; hairline `#D8D8D8`.
- Accents: sale red `#EB2026` (2.01 with ink — decorative flags only; 4.42 large-text on white for hover states), MyBiz coral `#FF664B`, purple `#6558A0`, muted `#848484` (3.74 large-only), `#CCCCCC` (fails — disabled/decorative only).
- Heaviest gradient use observed so far: 5 linear families (75+24+3+2+1) for campaign banners and scrims.
- WCAG: body/ink pairs AAA (8.86–21); failures cluster on decorative reds/greys and disabled states — a documented pattern, not an accident.

## 3. Typography Rules

- Trio: Lato 500–900 (workhorse 64→10px) + Abril Fatface (61/40/30 display serif for campaign headlines) + Caveat 700 (48px handwritten for playful annotations) + icomoon/FontAwesome icons.
- Logic: black-weight Lato for prices and CTAs (scannability), Fatface for romance, Caveat for human winks. Display type advertises; Lato transacts.
- Decision: three voices is the OTA maximum — borrow the layering (transact/seduce/humanize), keep body Lato ≥12px.

## 4. Component Stylings

- Search widget: floating card with tabbed verticals (flights/hotels/etc.), blue-focus inputs (`#F9FCFF` wash + `#D8D8DD` border), 4px radii, 34px pill search CTA.
- Cards: 16px with asymmetric variants (`0 0 16 16` footers, `16 16 0 0` image tops); 26px white pill chips with lift shadows; 20/30px badges; 50%/100% round indicators.
- Buttons: grey 34px pill (disabled pattern), white 26px chips, blue-outlined segmented controls.
- Inputs: 12px padded text/password with inset borders at rest, blue focus system on engage; checkboxes share the focus wash.
- Links: 8 styles; blue default → white on hover (banner contexts), ink, navy `#124680`, red `#ED1C24` → black hover for sale links.
- 12 carousel advances on the homepage — the page is a carousel of carousels.

## 5. Layout Principles

- 8px scale (2/4/5/6/8/10/12/13/15/16/20/22/30/40/50px) packing widget, rails, and grids.
- Floating-widget-over-hero structure: the search card overlaps the hero band, collapsing the funnel to zero scroll. Below: offer carousels → category rails → trust/about → app install → footer.
- 14-shadow elevation stack (0.04–0.2 alpha, up to 30px blur) separates widget, cards, and sticky elements on the grey bed.

## 6. Depth & Elevation

- Richest elevation observed: 14 shadows + 5 gradient families. Widget floats highest, cards mid, banners glow behind. Borders stay hairline (`#D8D8D8`) so shadows do the separation work.
- Decision: density requires elevation discipline — consistent blur language keeps 12 carousels from becoming noise.

## 7. Do's and Don'ts

- Do: AAA body ink; blue CTAs at large/bold sizes; floating search widget; gradient banners for campaigns; carousel-everything with progress cues.
- Do: keep reds/greys decorative (their contrast fails); keep disabled states visibly disabled (1.6–1.8).
- Don't: set small text in brand blue (3.39) or red; don't flatten the widget (it IS the conversion); don't add a fourth typeface.

## 8. Responsive Behavior

- 41-breakpoint ladder (2000→98px) — widget stacks, carousels become swipe rails, grids collapse stepwise; pills/CTAs stay thumb-sized.
- Touch: carousels are swipe-native (12 advances captured by crawler alone); sticky search persists on scroll.

## 9. Agent Prompt Guide

- Quick reference: `travel / booking-dense / widget-led / light / high complexity / single CTA (Search)`.
- Ready-to-use prompt: "Design an OTA booking page in the MakeMyTrip logic: grey bed with floating white search widget overlapping the hero, booking-blue CTAs at large bold sizes, AAA ink body text, red/coral sale accents kept decorative, gradient campaign banners, 16px cards with asymmetric variants, carousel rails with motion cues, Lato workhorse with serif-display campaign headlines and handwritten winks, 14-shadow elevation stack, and a 41-step responsive ladder. Keep functional text AAA; keep brand colors to large/bold uses."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Floating search widget (vertical tabs + blue-focus inputs + pill Search) — zero-scroll conversion.
2. Hero band + gradient campaign banners — excitement layer.
3. Offer carousels (12) — promotion rhythm.
4. Category rails (flights/hotels/packages/mybiz) — vertical cross-sell.
5. Trust/about + careers + WFH pages — institutional backing.
6. App-install band (`install.php`) — mobile capture.
7. Footer — dense link farm, scannable by weight.

### 11. Pattern Position

- Fits the OTA booking pattern: search → compare (rails/carousels) → persuade (offers) → convert (widget/PDP) → retain (app). Against Airbnb (browse-led) and Vita-Travel (inspiration-led), MakeMyTrip is intent-led — the trio covers every travel planning mode.
- Page-flow logic: assume the visitor knows they want to travel; spend zero pixels persuading and all pixels on speed, price, and choice.

### 12. Synthesis Notes

- Unique (borrow as logic): floating-widget-over-hero as the whole funnel; heaviest gradient/shadow system observed used coherently; three-voice type layering; carousel-of-carousels with crawler-visible advances; color-coded vertical accents (blue consumer, coral MyBiz).
- Combine with: Airbnb's card restraint and focus discipline (MMT's focus states are decent; Airbnb's token rigor would sharpen them) and Vita-Travel's editorial soul (MMT's densest pages need inspiration breaks).
- Avoid: copying the blue/red/grey trio verbatim (reads "Indian OTA clone"); small blue/red text; flattening elevation (density collapses without it); dropping the widget below the fold.
