# Apple — Design Analysis

> Source: `https://www.apple.com/` (crawl landed on India locale `/in/`) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 4 pages: `/in/`, `/compliance/`, `/choose-country-region/`, `/in/retail/`; `/HRAccuracy` skipped — file download, not a page)

Apple's storefront is the benchmark for premium commerce restraint: the product photography carries all the emotion while the UI stays near-invisible. Every token serves one goal — remove friction between desire and ownership.

## 1. Visual Theme & Atmosphere

- Mood: calm, assured, gallery-like. Vast whitespace, full-bleed product imagery, quiet chrome.
- Philosophy: the interface apologizes for existing. No decorative elements; depth, color, and motion exist only to stage products and guide the next click.
- Locale-aware theming: light default surfaces with dark product bands interleaved; theme tokens are semantic (`--color-themeDark-*` / `--color-themeLight-*`) so bands invert cleanly.

## 2. Color Palette & Roles

- Grounds: white `#FFFFFF` (page) + `#F5F5F7` (section alternation) + `#FAFAFC` (fine print/footer beds).
- Ink: `#1D1D1F` body (16.83:1 on white, AAA) + `#333336` dark fills + `#424245` tertiary fills + `#454545` on `#F5F5F7` (8.81 AAA).
- Secondary text: `#6E6E73` + `#86868B` — reserved for captions, footnotes, and footer microcopy, never primary CTAs.
- Hairlines: `#D2D2D7` dividers (1px) — structure without boxes.
- Link/CTAs: `#0066CC` body links (5.57:1 on white, AA) with `#0071E3` focus-ring color and `#2997FF` glyph blue on dark grounds.
- Product accents: yellow `#FFE045`, red `#FF3037` / product-red `#AF1E2D`, oranges `#FF791B` / `#F56300` / `#B64400`, deep fills `#290D00` / `#330000` — these tint bands and badges per campaign, never the chrome.
- WCAG: all sampled pairs pass — 16/16, 15/15, 13/13, 13/13 AA across pages, most AAA (12–21:1 on body pairs).

## 3. Typography Rules

- Single superfamily: SF Pro Display (headlines: 64/48/40/32/28/24/21/19px) + SF Pro Text (UI/body: 34/20/17/14/12/10px), all observed at weight 600 with OpenType `case` + `numr` features for tabular numerals in prices/specs.
- Hierarchy logic: size steps are tight (64→48→40) because product images already create drama — type only labels and prices. Body 17px/1.47 for readability; captions 12/10px for legal/footer.
- Decision: one family, semibold-only voice, numerals that align. Borrow the restraint: let imagery shout, keep type factual.

## 4. Component Stylings

- CTAs: fully-rounded pills (980px radius, e.g. "Learn more", "View pricing", "Watch the event"), 11×21px padding, blue fill or outline variants; hover shifts color/fill, never shape.
- Cards: 18px-radius media tiles with asymmetric `0 18px 18px 0` variants for editorial splits; 5px for small anchors.
- Inputs: 12px radius, 1px `#86868B` border, translucent white fill; focus gets a red-tinted wash plus 2px `#0071E3` outline and ring shadow — unmissable accessibility.
- Links: six observed styles; body links underline by default and drop it on hover (inverted from the web norm — the underline IS the affordance on a page with few visual cues), footer links do the reverse.
- Nav: global nav with animated search fade-and-slide (0.32s); 10–11 mega-menus per page revealed in crawl.
- Logo/iconography: inline SVG mark (`#000000`, 65×44) + single SVG icon system — no icon fonts.

## 5. Layout Principles

- 8px spacing scale with fine sub-steps (2/4/5/6/7/8/9/9.6px) plus large structural jumps (24/30/40/44/84px) for section rhythm.
- Alternating full-bleed bands (white ↔ `#F5F5F7` ↔ dark product fills); hairline dividers instead of boxes; generous 84px-scale section padding so each product gets a "room".
- Retail/compliance/country pages reuse the same band system — one layout language across marketing, policy, and store content.

## 6. Depth & Elevation

- Nearly flat: a single whisper shadow `rgba(0,0,0,0.04) 0px 6px 16px -8px`. Hierarchy comes from tonal bands and scale, not elevation.
- Borders are hairlines (1px `#F5F5F7` on buttons, `rgba(0,0,0,0.56)` section rules, 1px `#D2D2D7` on headings) — structure felt, not seen.

## 7. Do's and Don'ts

- Do: alternate band tones for rhythm; pill CTAs everywhere; underline-as-affordance on sparse pages; tabular numerals for prices.
- Do: keep secondary greys to captions and footers; keep focus rings loud (2px + ring).
- Don't: add shadows, gradients (none observed), or decorative color — the product supplies all chroma.
- Don't: shrink body below 14–17px or loosen the 8px scale — density would break the calm.

## 8. Responsive Behavior

- 19-breakpoint ladder from 1746px down to 419px (1440/1170/1069/1068/1044/1023/834/833/800/776/767/735/734/641/640/480/419) — bands reflow, type steps down, pills stay tappable.
- Touch: 980px pills and full-width band CTAs are inherently thumb-friendly; search/nav collapse into the animated overlay.

## 9. Agent Prompt Guide

- Quick reference: `ecommerce / premium-minimal / banded-showcase / light / high complexity / dual CTA (Learn more + Buy/View pricing)`.
- Ready-to-use prompt: "Design a premium commerce page in the Apple logic: white and #F5F5F7 alternating bands, near-black #1D1D1F semibold single-family type with tabular numerals, fully-rounded pill CTAs, 18px media cards, hairline #D2D2D7 dividers, one blue link color with loud focus rings, essentially no shadows or gradients, full-bleed product imagery doing the emotional work, and a 19-step responsive ladder that keeps pills tappable. Every sampled pair must pass AA, body pairs AAA."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Global nav + animated search overlay — wayfinding that disappears.
2. Hero product band (full-bleed image + 64px headline + dual pill CTAs) — desire in one viewport.
3. Product tile grid (18px cards, alternating grounds) — compare without scrolling far.
4. Retail band (`/in/retail/`, richest tokens: inputs, shadow, 17 breakpoints) — store services as products.
5. Compliance/policy pages — trust infrastructure in the same visual language.
6. Country selector — locale routing as calm utility.
7. Footer (fine-print beds, microcopy hierarchy) — legal density made scannable.

### 11. Pattern Position

- Fits the commerce pattern (`patterns/ecommerce.md`) at its most restrained: interest → compare → buy, with policy/trust content (compliance, retail services) elevated to first-class bands instead of footer links.
- Page-flow logic: seduce (hero) → specify (tiles/specs) → reassure (retail services, compliance) → convert (sticky buy box / pill CTAs). The UI never competes with the product for attention.

### 12. Synthesis Notes

- Unique (borrow as logic): band-alternation as the only layout device; underline-as-affordance inversion; tabular-numeral pricing; single whisper shadow; theme-token band inversion (dark/light fills per campaign).
- Combine with: Gumroad's creator-commerce warmth (Apple brings restraint, Gumroad brings personality) and agency references' typographic courage (Apple's type is deliberately quiet — pair with KOTA/Matters scale logic for non-Apple brands that need louder voices).
- Avoid: copying the monochrome-plus-blue scheme verbatim (it reads "Apple clone" instantly); shrinking contrast below AA on links; adding decorative gradients/shadows; letting body type drop to caption sizes.
