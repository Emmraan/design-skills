# Aman — Design Analysis

> Source: `https://www.aman.com/` (ultra-luxury resorts, sanctuaries and journeys) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/about-us`, `/contact-us`, `/destinations`, `/journeys`)

Aman is the study in restraint that justifies five-figure nightly rates: warm stone grounds, ink serif headlines, a single rectangular button, and slow motion. Nothing on the page raises its voice — the photography and the whitespace do the selling.

## 1. Visual Theme & Atmosphere

- Mood: sanctuary — stillness, warmth, privacy. The PWA manifest itself is themed `#F3EEE7`, so even the browser chrome breathes stone.
- Philosophy: luxury is the absence of noise — 5 colors, 1 button variant, no gradients, sharp corners, and the slowest motion system in the repo.
- Editorial structure: destinations and journeys read as magazine features with a "Reserve" coda, not as booking funnels.

## 2. Color Palette & Roles

- Ground: warm stone `#F3EEE7` (page + manifest) + white surfaces + black `#000000` (18.19 on stone, 21 on white).
- Ink: `#313131` body (11.27 on stone, 13.01 on white AAA) + `#585858` secondary (7.11 AAA on white) + stone-grey `#AAA6A3` for quietest meta.
- Interactive: links underline by default across all four tones (ink/stone/black/grey) and resolve to cornflower `#3860BE` without decoration on hover — the only hue on the site.
- Known fail: gold focus `#B38B5B` on stone at 2.69 — focus visibility is the one accessibility gap; darken the focus ring.
- No gradients; shadows are warm and breathy (stone-grey `199,197,199` glows, soft black 0.1–0.2).

## 3. Typography Rules

- Editorial pairing: Lyon Text/Display Web (serif headlines 31/24/20/16/15/10px, 700 display) + Whitney SSm (sans links/UI 24→10px) + BeausiteSlick (self-hosted woff/woff2 support).
- Logic: serif speaks (place, feeling), sans navigates (links, labels, forms). Small sizes (10–12px) are tracked out, never cramped.
- Decision: quiet scale — 31px max headline observed. Luxury here is refusal of display maximalism. Borrow the pairing and the restraint.

## 4. Component Stylings

- Buttons: exactly ONE variant — ink rectangle (10×15px, stone text, 1px ink border, 2–3px radius). No pills, no ghosts, no sizes. The discipline is the brand.
- Filter/search: 17px and 50px radius chips for destination filtering and cookie search — the only curves on the site, reserved for utility.
- Links: underline-first (unusual at this tier — the underline is the affordance on near-monochrome pages), cornflower hover.
- Logo: inline SVG wordmark in ink, 150×40, full favicon/PWA set.
- Iframes carry inset ink borders — even embeds obey the hairline system.

## 5. Layout Principles

- 8px scale with fractional optical steps (4/4.2/5/5.6/7/7.392/9/9.8/10/14/15/16/20/30/65px) — luxury is typeset, not gridded.
- Hairline architecture: ink 1px rules, `#404040` button borders, `#DDD` dividers, `#82847F` input lines — structure you feel through calm, not boxes.
- Flow: sanctuary hero → philosophy/about → destinations index → journey features → Reserve/contact. Booking is a conversation, placed last.

## 6. Depth & Elevation

- Five soft shadows, all low-contrast and warm — glows rather than lifts. No gradients anywhere.
- Decision: depth as atmosphere (warm haze), never as interface (no cards popping). Photography sits IN the stone, not ON it.

## 7. Do's and Don'ts

- Do: stone/ink AAA pairs; one rectangular button; underline-first links; serif/sans editorial pairing; fractional spacing; slow motion.
- Do: theme the PWA chrome to match the ground.
- Don't: add pills, gradients, brand hues, or display type — each would break the sanctuary contract. Fix the gold focus contrast (darken to pass).
- Don't: hurry — 0.6s buttons and 0.5s media are load-bearing mood.

## 8. Responsive Behavior

- 21-breakpoint ladder (1520→350px) — editorial columns collapse gracefully; hairlines hold the structure at every width; the single button stays tappable throughout.
- Touch: filter chips and Reserve CTA are thumb-first; journeys read as vertical scroll features on mobile.

## 9. Agent Prompt Guide

- Quick reference: `hospitality / serene-luxury / editorial-destinations / light / medium complexity / single CTA (Reserve)`.
- Ready-to-use prompt: "Design an ultra-luxury hospitality page in the Aman logic: warm stone grounds with ink serif headlines and sans navigation, AAA stone/ink pairs, exactly one rectangular button style, underline-first links resolving to a single hover hue, hairline borders and warm glow shadows instead of elevation, no gradients, slow 0.5–0.6s ease motion, fractional optical spacing, and a 21-step responsive ladder. Theme the app chrome to match. Luxury is refusal — add nothing loud."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Sanctuary hero (stone, serif headline, still photography) — arrival as exhale.
2. Philosophy/about band — the creed before the inventory.
3. Destinations index (filter chips as the only curves) — browse by longing.
4. Journey features (editorial long-form) — sell transformation, not rooms.
5. Contact/Reserve coda — conversation, not checkout.
6. Footer — quiet sitemap on stone.

### 11. Pattern Position

- Fits the sanctuary pattern: arrive → believe (philosophy) → wander (destinations/journeys) → enquire (Reserve). Against Flyward (quiet-luxury aviation, motion-led), Aman is stillness-led — together they define the luxury spectrum's two poles.
- Page-flow logic: the funnel is inverted — 90% inspiration, 10% transaction. The booking engine hides behind human contact.

### 12. Synthesis Notes

- Unique (borrow as logic): single-button discipline; underline-first luxury links; manifest-themed chrome; fractional optical spacing; slowest-motion system; monochrome-plus-one-hue restraint; inverted funnel (inspiration ≫ transaction).
- Combine with: Flyward's motion craft (Aman brings stillness, Flyward brings glide — a luxury page needs both registers) and Table Hotels' curation logic (next ref) for multi-property browsing.
- Avoid: copying stone/ink/cornflower verbatim (instant clone); adding urgency, pills, or gradients; speeding up motion; darkening into moody-luxury cliché — Aman's lightness IS the differentiator.
