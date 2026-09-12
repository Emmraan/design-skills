# Global Scrap Connect — Design Analysis

> Source: `https://www.globalscrapconnect.in/` (B2B scrap-trading marketplace, India) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 3 pages: `/`, `/about`, `/contact` — explicit paths, blogs intentionally skipped)

Global Scrap Connect is industrial marketplace trust: deep pine green (`#2B5E4B`, manifest theme), off-white grounds, Montserrat black display type up to 192px, and pill everything. Against Ajmal's affordable-luxury and Apple's premium-minimal, this is the B2B pole of ecommerce — it converts scrap dealers on credibility, not desire.

## 1. Visual Theme & Atmosphere

- Mood: modern mandi office — green, white, steel hairlines, marquee tickers, WhatsApp-era CTA density.
- Philosophy: legitimacy for an informal trade — big type, real addresses (JustDial + Instagram + LinkedIn + YouTube socials), contact-first funnel.
- Gradient-heavy imagery (63 scrim overlays + 23 radials) stages industrial photography without a photo system of its own.

## 2. Color Palette & Roles

- Brand: pine green `#2b5e4b` — white-on-green 7.49 AAA, green-on-paper hover 7.14 AAA; manifest theme too.
- Grounds: `#f8faf8` green-tinted white + `#ffffff` + mint tint `#e6f3e6`.
- Ink: `#1f2937` slate + `#1a1a1a` (17.4 AAA) + `#4a5565` (7.21 AAA on paper) + `#6a7282` (4.84 AA).
- Signal green `#4ade80` reserved for rings and decorative washes (fails on tint at 1.5 — correctly never body text); muted `#99a1af` decorative only (2.6 fail on white).
- Borders: `#e5e7eb`/`#f3f4f6` hairlines + black hairlines + white 50%/20% (dark zones) + green 30% rings.

## 3. Typography Rules

- Display: Montserrat 700/900, 192→14px — industrial shout, sized like hoardings.
- Body: Inter 300–900, 24→8px — neutral workhorse for listings and forms.
- Micro: ui-monospace 600/700/900, 14→9px — spec labels, codes, technical asides.
- Decision: three-family split (shout/speak/spec) fits trading — emotion, information, specification each get a voice.

## 4. Component Stylings

- CTAs: 7 variants, all 9999px pills — green solid (10×24, 8×16) + off-white bordered + oversized white 20×40 closer. Radius never varies; size and fill encode hierarchy.
- Cards: 24/16/12px radii with Tailwind sm/lg shadows (10% black) — listings lift just enough to scan.
- Inputs (`/contact`): `#f8faf8` fill, grey border, 16px padding, 8px radius — thumb-sized, high-contrast, zero decoration.
- Links: 6 styles (ink, green, two greys, white) — color-shift hovers, no underlines except body context.
- Logo: Cloudinary-hosted 160px transparent mark + round-border favicon set + og/twitter images.

## 5. Layout Principles

- 8px scale with 128/96/80/64/48px section air — hoarding-scale display over a dense 12–16px trading core.
- Funnel: green hero → categories/materials → trust (about) → listings proof → contact capture → footer with JustDial-class local proof.
- Marquee (35s) + pulse/spin/dash/ping accents animate an otherwise static B2B page — motion as vitality, not decoration.

## 6. Depth & Elevation

- Only Tailwind sm + lg shadows site-wide — restraint that keeps 192px type and scrims as the depth story.
- Decision: photography scrims + giant type carry dimension; components stay flat and scannable.

## 7. Do's and Don'ts

- Do: AAA white-on-green + ink pairs; pill-everything CTA discipline; mono spec labels; marquee vitality; local-proof socials (JustDial pattern for Indian B2B).
- Do: keep signal-green and muted grey decorative (both fail small text); keep contact inputs 16px-padded.
- Don't: add deal-styling that cheapens B2B trust; don't shrink listing type below 12px; don't invent new greens.

## 8. Responsive Behavior

- No breakpoints detected in tokens (Tailwind responsive modifiers handle it structurally) — verify mobile manually before borrowing layout.
- Touch: pill CTAs and 16px-padded inputs are thumb-safe; marquee must pause on reduced-motion.

## 9. Agent Prompt Guide

- Quick reference: `ecommerce / eco-industrial / marketplace-grid / light / medium complexity / dual CTA (list scrap + contact)`.
- Ready-to-use prompt: "Design a B2B trading-marketplace page in the Global Scrap Connect logic: deep pine-green primary with AAA white-on-green pairs, green-tinted off-white grounds, Montserrat-black hoarding display type with Inter body and mono spec labels, pill-everything CTAs where size and fill encode hierarchy, flat scannable listing cards with restrained shadows, image scrims plus one marquee for vitality, quiet high-contrast contact inputs, and local-proof socials. Convert on credibility, never on desire."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Green hero with hoarding type — category authority.
2. Material/category bands — browse the trade.
3. Listings proof — liquidity signal.
4. About (`/about`, 11/17 WCAG) — legitimacy story.
5. Contact (`/contact`, inputs) — lead capture close.
6. Marquee + socials footer — alive-and-local proof.

### 11. Pattern Position

- Fits the B2B-marketplace pattern: authority → browse (categories) → trust (about, local proof) → capture (contact). Against Ajmal (D2C luxury) and Apple (brand minimal), this is trade-led — the ecommerce trio now covers desire, brand, and transaction.
- Page-flow logic: assume the dealer is skeptical of online trade; every band answers "are you real" with addresses, socials, and human contact.

### 12. Synthesis Notes

- Unique (borrow as logic): hoarding-scale Montserrat as trust device; shout/speak/spec three-family split; pill-everything CTA discipline; JustDial-class local proof for Indian B2B; scrims-over-photography instead of a photo system; marquee vitality on static B2B.
- Combine with: SaaS pricing transparency for rate-card sections (scrap needs price discovery) and fintech KYC patterns for dealer verification flows.
- Avoid: copying pine-green + Montserrat verbatim (reads "scrap clone"); bazaar tactics that cheapen B2B trust; small muted-grey text; skipping the about page — legitimacy is the product.
