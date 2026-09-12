# Coursera — Design Analysis

> Source: `https://www.coursera.org/` (MOOC marketplace — individuals + business) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/about`, `/business`, `/about/how-coursera-works`, `/leadership/` via blog redirect)

Coursera is the institutional pole of learning marketplaces: academic blue, Source Sans throughout, credential-grade restraint, and a dual consumer/employer funnel sharing one token system. Against Udemy's deal-led energy, Coursera converts on university-brand trust.

## 1. Visual Theme & Atmosphere

- Mood: campus quad, digitized — white grounds, academic blue, partner-logo walls, career-outcome bands.
- Philosophy: borrowed prestige — university and employer brands do the persuading; Coursera's own chrome stays neutral, legible, and AA-or-better on every functional pair.
- Dual audience: `/business` mirrors the consumer catalog for L&D buyers without changing the visual language (same pattern as One Medical's employer mirror).

## 2. Color Palette & Roles

- Brand: academic blue `#0056D2` (6.44 AA on white; manifest theme too, bg `#2D89EF`) + bright CTA blue `#136EF0` (4px primary buttons, inset-ring shadow) + deep navy `#0B408B` (white-on-navy 9.9 AAA hover/focus).
- Ink: `#0D0F12` (19.19 AAA) + `#0F1114` (18.91) + slate `#48546E` (7.58 AAA) + `#333333`.
- Structure: hairline `#C1CBDB`, input borders `#5E6F92`, beds `#E9EEF7`/`#F0F6FF`/`#F6F6F6`, callout sky `#B0E5FB`.
- Meta: `#8495B0` underlined links (decorative-large only).
- Known fails: light-on-slate 2.78/1.6, sky-on-white 2.03, near-black hover 1.02 — all decorative washes and disabled states, never body text.

## 3. Typography Rules

- Single superfamily: Source Sans Pro 600/700 (84px display → 12px captions) + Source Sans 3 500/600 for UI + Helvetica micro-fallbacks.
- Scale: 84/64/48/44/40/32/30/28/24/20/16/14/13/12 — display sizes for mission statements, compact 14–16px for catalog density.
- Decision: one humanist sans at semibold-and-up throughout — academic clarity without sterility. Borrow for any credential-heavy product.

## 4. Component Stylings

- CTAs: four fills, one language — bright-blue 4px primary (12×32px), white/blue-outlined 16px secondary, dark 32px pill, white/grey 32px pill. Radius encodes emphasis (4px = commit, 32px = explore).
- Cards: 16px course cards with soft grey shadows; 1000px-round imagery; 100% round instructor avatars — faces as trust markers.
- Inputs: pill search (40px radius) for catalog + 4px text inputs with slate borders + 4px selects; checkbox/radio share the hairline system.
- Links: 9 styles, all resolving to `#3860BE` on hover (the web-wide trust-hover convention, sixth site running).
- Logo: inline SVG wordmark in brand blue, 127×32, full favicon set; partner logo wall as social-proof component.

## 5. Layout Principles

- 8px scale (1/2/4/5/8/10/11/12/16/18.5/20/24/28/32/64px) with 64px section air around a dense 12–20px catalog core.
- Catalog funnel: pill search hero → partner proof wall → career-path bands ("Start my career", 16px chips) → course rails → outcome stats → business upsell → footer.
- Three gradient families stage heroes and career bands; blue inset-ring shadows mark primary actions.

## 6. Depth & Elevation

- Minimal: blue inset action rings + soft grey card shadows (2–12px) + gradient staging. Cards lift just enough to scan; nothing floats decoratively.
- Decision: flat catalog + glowing primary actions — attention goes to enroll buttons, not surfaces.

## 7. Do's and Don'ts

- Do: AAA ink pairs + AA brand blue; radius-coded CTA hierarchy; pill search; partner walls; career-path chips; 43-step responsive ladder.
- Do: keep sky/meta tones decorative (they fail small text); keep business pages in the same tokens.
- Don't: add deal-styling (strikes, countdowns) — credential trust breaks under bazaar tactics; don't shrink catalog type below 12–14px; don't invent new blues.

## 8. Responsive Behavior

- 43-breakpoint ladder (1920→0px) — catalog rails collapse stepwise to single-column mobile; pill search stays full-width; chips wrap; business tables stack.
- Touch: 32px+ pills and full-width search are thumb-first; about-page carousels (3 advances) swipe natively.

## 9. Agent Prompt Guide

- Quick reference: `education / institutional-blue / catalog-led / light / high complexity / dual CTA (enroll + for business)`.
- Ready-to-use prompt: "Design a learning-marketplace page in the Coursera logic: white grounds with academic-blue primary actions, AAA ink body text, single humanist sans family at semibold-and-up, pill catalog search, 16px course cards with round instructor avatars, radius-coded CTA hierarchy (4px commit, 32px explore), partner-logo proof walls, career-path chips, blue inset-ring action emphasis, and a 43-step responsive ladder. Convert on credentials, never on deals."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Catalog search hero (40px pill) — intent capture.
2. Partner logo wall — borrowed prestige.
3. Career-path chips (16px) — goal-led browsing.
4. Course rails (16px cards, avatars, ratings) — dense comparison.
5. How-it-works (`/about/how-coursera-works`, 9/9 WCAG) — methodology trust.
6. Business funnel (`/business`, 17/19 pass) — employer distribution.
7. About + leadership — institutional backing.
8. Outcome stats bands — ROI proof for both audiences.

### 11. Pattern Position

- Fits the catalog-learning pattern: search → browse (rails) → trust (partners, outcomes, methodology) → enroll → expand (business). Against Udemy (deal-led marketplace), Coursera is credential-led — the pair now covers price-driven and prestige-driven learning demand.
- Page-flow logic: assume the learner wants a better job; every band answers "will this get me hired" with partners, paths, or stats.

### 12. Synthesis Notes

- Unique (borrow as logic): radius-coded CTA hierarchy; partner wall as core component; career-path chips as navigation; dual-audience single-token system; credential-over-deal conversion stance; 43-step responsive granularity.
- Combine with: Udemy's search-deal mechanics for price-sensitive segments (Coursera brings prestige, Udemy brings urgency — a learning page needs to know which game it's playing) and SaaS pricing transparency for business tiers.
- Avoid: copying academic-blue + Source Sans verbatim (reads "MOOC clone"); bazaar tactics that corrode credential trust; small sky/slate text; dropping the business funnel — employer distribution is half the revenue story.
