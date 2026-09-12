# PharmEasy — Design Analysis

> Source: `https://pharmeasy.in/` (Indian online pharmacy + diagnostics) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/about-us`, `/blog/`, `/online-medicine-order`, `/generics`)

PharmEasy is a high-density healthcare marketplace: teal-green trust chrome over a category-tile grid, offer yellows and coral sale accents, and upload-prescription flows. Where One Medical converts on calm, PharmEasy converts on availability and price.

## 1. Visual Theme & Atmosphere

- Mood: busy neighborhood chemist, digitized — dense, colorful, always offering something (generics promos, order flows, blog health content).
- Philosophy: utility density — category tiles, carousels with 3s progress fills, and sticky order CTAs keep the path to medicine under two taps.
- Light-only; manifest teal `#10847E` carries the brand into the PWA chrome.

## 2. Color Palette & Roles

- Primary: teal-green `#10847E` (buttons, links, focus borders; 4.54:1 on white AA, mirrored white-on-teal for hover/focus states).
- Ink: `#30363C` (12.22 AAA on white; 11.47 on `#F5F8FC`) + pure black AAA + `#4F585E` secondary (7.27 AAA).
- Offer accents: yellow `#F5B326` (deal badges/borders) + coral `#F47779` (sale flags — 2.71 on white, decorative-only) + pink wash `#FFD7E1` + blue `#3661B0` (info links) + teal-dark `#187484`.
- Neutrals: `#8897A2` meta text (3.0 — large-only) + `#B4C0D3` + hairline border blues `#E6EBF4` / `#DCE4F1` / `#D7DFE5`.
- Known fails: dark-on-teal 2.1, coral-on-white 2.71 — keep both out of body text.

## 3. Typography Rules

- Dual sans: Inter (500/600/700; 40px H2 down to 10px captions) for product/UI + Open Sans (500–700; 30/28/26/20/18/16/14/12) for content/blog.
- Logic: semibold-and-up everywhere — density demands weight for scannability; body 13–16px, captions 10–12px, micro-labels 11px semibold.
- Decision: two near-identical sans families is redundant but harmless (both render neutral); borrow the weight discipline, not the duplication.

## 4. Component Stylings

- CTAs: teal filled (4px, 12px padding) for primary order actions + 100px pill variant + outlined teal ghost + tinted blue/pink chips (4px, 4×12px) for filters — one color, four urgency levels.
- Category tiles: 16px radius cards; product cards 8px with hairline borders and layered soft shadows (0.04–0.12 alpha, up to 18px blur); round 50%/100% icon buttons.
- Inputs: tel-first (icon-padded 15×16×15×45px, teal focus border) for OTP/login flows; email with blue glow focus; 4px radii throughout.
- Links: ink underlined → plain on hover; teal plain; black → teal on hover; 7 styles covering footer, content, and app chrome.
- Nav: slideDown animation (0.25s); 4 menus per transactional page; carousel page-indicators with 3s fill animation.

## 5. Layout Principles

- 8px scale (1/4/8/10/12/15/16/20/22/24/32/40/48/50/64px) tuned for tile grids and dense PDPs.
- Order funnel: search/upload-prescription hero → category tiles → offer carousels → generics promos → medicine PDPs → diagnostics cross-sell → blog trust content → footer.
- Editorial (`/blog/`, WordPress + FontAwesome) and corporate (`/about-us`) skins share tokens with the storefront — one brand, three engines.

## 6. Depth & Elevation

- Functional shadow stack (6 styles): card hover `0 6px 10px + 1px 18px + 3px 5px` triple-layer at 0.04–0.08 alpha, popover `0 2px 14px 4px`, inset hairline `0 -1px 0 inset` for sticky bars. No gradients.
- Borders do categorical work: yellow `#EFD06C` = offer, cyan `#CEF8FF` = info, blue `#B5CDF7` = interactive — color-coded hairlines, a quiet triumph.

## 7. Do's and Don'ts

- Do: teal AA pairs; hairline category colors; triple-layer soft shadows; tel-first OTP inputs; 3s carousel progress.
- Do: keep coral/yellow to badges and large flags (both fail small-text contrast).
- Don't: set body text in `#8897A2` (large-only); don't flatten the tile radii (8/16px rhythm aids scanning); don't add serif or display type — utility is the brand.

## 8. Responsive Behavior

- 22-breakpoint ladder (1400→98px) — tile grids collapse 5→4→2→1 columns; sticky order bars persist; OTP inputs stay full-width tappable.
- Touch: 100px pill CTAs and 50% round icon buttons are thumb-first; nav collapses to drawers with slideDown motion.

## 9. Agent Prompt Guide

- Quick reference: `healthcare / clinical-utility / marketplace-grid / light / high complexity / dual CTA (order medicines + upload prescription)`.
- Ready-to-use prompt: "Design a healthcare marketplace page in the PharmEasy logic: white grounds with teal-green primary actions, ink AAA body text, yellow/coral offer accents kept to badges, 8/16px tile cards with hairline color-coded borders and triple-layer soft shadows, tel-first OTP inputs with teal focus, carousel progress indicators, semibold dual-sans type, and a 22-step responsive ladder. Keep functional accents AA; keep sale colors decorative-only."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Search/upload-prescription hero (tel input + pill CTA) — intent capture in one viewport.
2. Category tiles (16px cards) — browse by ailment/product.
3. Offer carousels (3s progress fills) — promotion rhythm.
4. Generics promo bands — price-sensitive conversion.
5. Medicine PDPs (`/online-medicine-order`) — transactional core, 4/4 WCAG pass.
6. Diagnostics cross-sell — basket expansion.
7. Blog health content — SEO trust layer.
8. About + footer — institutional backing.

### 11. Pattern Position

- Fits the healthcare-marketplace pattern: capture intent (search/Rx upload) → browse (tiles) → persuade (offers/generics) → transact (PDP/OTP) → retain (refills/blog). Against MavenClinic (empathy-led) and One Medical (calm-led), PharmEasy is access-led — the trio now covers every healthcare conversion emotion.
- Page-flow logic: need → find → save → buy → refill. The upload-prescription CTA short-circuits browsing for chronic patients.

### 12. Synthesis Notes

- Unique (borrow as logic): color-coded hairline borders as category language; triple-layer soft shadows at low alpha; upload-prescription as primary CTA; carousel progress fills; tel-first OTP input patterns.
- Combine with: One Medical's serif calm for editorial/trust bands (PharmEasy's densest pages need breathing room) and Ajmal's PDP discount animation (priceReveal would lift generics promos).
- Avoid: copying the teal/yellow/coral trio verbatim (reads "Indian pharmacy clone"); small coral/yellow text; flattening shadows (density needs the lift cues); adding display typography that fights the utility voice.
