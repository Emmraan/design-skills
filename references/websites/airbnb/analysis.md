# Airbnb — Design Analysis

> Source: `https://www.airbnb.co.in/` (India locale; crawl covered utility/host pages) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/login`, `/about/company-details`, `/resources/hosting-homes`, `/help`, `/refer`)

Airbnb's DLS (design language system) is a two-sided marketplace chrome: warm neutrals, one coral brand color, a variable grotesk with Indic-script subsets, and card grids that make photography the interface. Note: the crawl captured login/about/hosting/help/refer pages rather than search results — the token system is shared, but listing-page specifics should be enriched later.

## 1. Visual Theme & Atmosphere

- Mood: belong-anywhere warmth — white beds, soft greys, coral sparks, photography-first cards.
- Philosophy: the chrome disappears so places and hosts shine; brand color is rationed to logo, key CTAs, and wishlist hearts.
- Dual-audience: guest and host (`become-a-host`, hosting resources, referrals) share one token system with tier brand fills (core rausch, plus maroon `#92174D`, luxe purple `#460479`).

## 2. Color Palette & Roles

- Ink: `#222222` (15.91:1 on white AAA; 14.85 on `#F7F7F7`; 14.21/13.35 on grey beds) + secondary `#6C6C6C` (5.25 AA — meta/prices only).
- Brand: rausch coral `#FF385C` (logo, primary CTAs; 3.52 on white = large-text only — CTAs are bold/large by construction) + deep border/tertiary variants `#D80669` / `#DA1249` / `#D70466`.
- Tier fills: plus `#92174D`, luxe `#460479`; avatar-scheme accents (blue `#0D4DAA`, green `#015F1A`, orange `#8F3400`, purple `#503EB2`, magenta `#901E7C`, rausch `#A21039`) for host/guest identity chips.
- Functional: input-line blue `#318CF7`, link blue `#0000FF` (underlined), slider grey `#C1C1C1` (1.8 fail — decorative track), beige `#C5C1BB`.
- Known fails: white-on-`#F7F7F7` 1.07, `#C1C1C1` on white 1.8 — both non-text UI chrome.

## 3. Typography Rules

- Single variable family: Airbnb Cereal VF (weights 500/575/600/700, OpenType `salt`), shipped with Arabic/Cyrillic/Devanagari subsets for the India locale — internationalization is a font decision, not an afterthought.
- Scale: 40px H1 → 32/28/26/22/21 → 20/18/17 body/links → 16 UI → 14/13 → 12/11 captions. Tight, even steps — no display maximalism; cards carry the hierarchy.
- Decision: one friendly grotesk at moderate scale + photographic cards. Borrow for marketplaces where inventory imagery varies wildly.

## 4. Component Stylings

- CTAs: 20–32px rounded buttons (white fill + `#DDD` border + ink text default; rausch fills for primary), 100px/9999px pill extremes for search and filters; 4px for inline anchors.
- Cards: 16px image cards; 50% round wishlist hearts, language/currency pickers, carousel arrows; 12/14px sheets and pickers.
- Inputs: search-first (ink text, token-driven focus: inset white ring + dark border); `#DDD` hairline borders throughout.
- Links: ink default (no decoration), rausch for brand actions, blue underlined for legal/help, grey for meta — 5 styles, decoration used sparingly.
- Logo: inline SVG Bélo in rausch, 102×32, PWA-ready icon set.

## 5. Layout Principles

- 8px scale with product-tuned steps (4/5/5.5/6/7/8/11/12/14/15/16/24/32/48/80px) — card grids, search bars, and help content share one rhythm.
- Borders as structure: `#DDD` 1px card/search outlines, white 1–4px rings over imagery, ink 1px rules for emphasis. One triple-layer shadow (`0/2/4px` at 0.02–0.1) lifts cards; linear + radial gradients (5+5) scrim photography for legible overlays.
- Observed flow: auth → company trust → hosting resources → help → referrals — the supply-side funnel, not guest search (enrich later).

## 6. Depth & Elevation

- Minimal elevation: a single triple-layer card shadow + photo scrims. Depth comes from imagery layering (cards over beds, rings over photos), not surfaces.
- Decision: flat chrome + rich photography = infinite inventory variety without visual chaos.

## 7. Do's and Don'ts

- Do: ration rausch to brand moments; ink AAA body; Cereal-style single family with locale subsets; 16px cards + round save hearts; scrim gradients for text-over-photo.
- Do: keep `#6C6C6C` to meta text (AA floor) and slider greys decorative.
- Don't: set small text in rausch-on-white (3.52); don't add display type that fights photography; don't invent new radii — the 10-token scale is load-bearing.

## 8. Responsive Behavior

- 137-breakpoint granular ladder (2120→99px) — the densest observed: card columns reflow per ~20px, type steps continuously, pills/search stay tappable.
- Touch: round hearts/arrows and full-width search are thumb-first; login/help pages collapse to single column early.

## 9. Agent Prompt Guide

- Quick reference: `travel / warm-marketplace / card-grid-search / light / high complexity / dual CTA (book + become-a-host)`.
- Ready-to-use prompt: "Design a travel marketplace page in the Airbnb logic: white and warm-grey beds, single friendly variable grotesk with locale subsets, one coral brand color rationed to logo and primary CTAs, 16px photography cards with round save hearts, pill search with hairline borders, linear/radial photo scrims for overlay text, triple-layer card shadow only, signature snap easing, and a granular responsive ladder. Keep body AAA; keep brand color to large/bold uses."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Pill search (location/dates/guests) — intent capture as jewelry.
2. Photo card grid (16px cards, hearts, price + rating) — inventory as interface.
3. Hosting resources (`/resources/hosting-homes`, richest tokens) — supply-side education.
4. Help center — support as calm content.
5. Referral loop (`/refer`) — growth built into chrome.
6. Login/auth — low-friction entry.
7. Company/about — institutional trust.

### 11. Pattern Position

- Fits the marketplace pattern: demand capture (search) → browse (cards) → trust (host resources, reviews) → convert (book) → supply (become-a-host, referrals). Against Vita-Travel (dark retreat editorial), Airbnb is the bright transactional pole — together they cover inspiration-led and intent-led travel.
- Page-flow logic: the crawl's supply-side bias is itself a lesson — marketplaces must design host acquisition as carefully as guest conversion.

### 12. Synthesis Notes

- Unique (borrow as logic): locale-subset variable fonts; avatar-scheme identity palette; tier brand fills (core/plus/luxe); rausch rationing discipline; 137-step responsive granularity; photo-scrim gradient system.
- Combine with: Vita-Travel's dark editorial drama (Airbnb brings systems, Vita brings soul) and MakeMyTrip's bundling logic (next ref) for packages/transport cross-sell.
- Avoid: copying rausch + Cereal + 16px cards verbatim (instant clone); small rausch text; star-rating colors from other systems — Airbnb's trust language is self-contained.
