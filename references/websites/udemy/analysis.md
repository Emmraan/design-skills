# Udemy — Design Analysis

> Source: `https://www.udemy.com/` · Baseline: `baseline.json` · Collected: 2026-09-11 (Dembrandt 0.32.2)
> Udemy is an online learning marketplace (millions of learners, independent
> instructors, plus Udemy Business). The site is **marketplace energy with classroom
> clarity**: a white canvas, near-black ink text at AAA contrast, one custom type
> family, and a single purple action color that turns browsing into enrolling.

## 1. Visual Theme & Atmosphere

- **Marketplace optimism.** White canvas with ink text and confident purple actions —
  the page feels like a busy, trustworthy bazaar of courses: dense with choice but
  never chaotic, because one color acts and one family speaks.
- **Search-first confidence:** the header search (autocomplete) plus a search-led hero
  say "whatever you want to learn is already here" — discovery is the product, not
  persuasion.
- **Dual-audience balance:** learners get course cards, ratings, and topics; instructors
  and business buyers get dedicated bands — same palette and type, different proof.
- Mood: energetic, democratic, competent — learning as shopping, done respectably.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Ink | `#2A2B3F` | Headlines + body text (13.85:1 on white, AAA); the voice of the page |
| Canvas | white `#FFFFFF`, tints `#F6F7F9` / `#E9EAF2` | Page background + alternating bands (ink on tints 11.5–12.9:1, AAA) |
| Action | purple `#6D28D2` | Primary buttons, links (white on purple 7.28:1, AAA) — the only color that acts |
| Brand | violet `#A435F0` | Logo + brand moments; action's brighter sibling, never a second CTA color |
| Secondary text | slate `#71758E` | Instructor names, meta, descriptions (4.53:1 on white — AA, never small/essential text) |
| Campaign tints | cyan `#C2E9EB`, peach `#FFD1CE`, lavender `#D2CAFF` | Smart-bar and plan banners — tinted bands carry campaigns, white cards sit on top |
| Proof | amber `#F69C08` | Star ratings — the marketplace's trust currency |
| Status | green `#206241`, red `#D51C0F` | Success/credit and errors only, never decoration |
| Footer ink | `#202230` | Dark footer + inverted bands (white on it 15.76:1, AAA) |

- **One color acts:** purple fills primary CTAs, outlines secondary CTAs, and colors
  links — nothing else competes for the click. Campaign tints decorate bands; they
  never carry actions.
- **Tints over gradients:** seasonal/promo messaging gets flat pastel bands (cyan,
  peach, lavender) with ink text at AAA — calm promotion without gradient noise.
- **Light handling:** light-first with a single dark footer/inverted band for rhythm —
  depth through section inversion, not dark mode.

## 3. Typography Rules

- **One custom family:** Udemy Sans (Regular/Medium/Bold/Light woff2) does everything —
  no pairing logic to learn, hierarchy purely through size + weight grades (300–700).
  Brand voice comes from the family itself, not from font combinations.
- **Display restraint:** 56/48/32px medium (500) at tight `1.0–1.1` leading — headlines
  state the offer plainly; confidence without editorial drama suits a catalog.
- **Body for scanning:** 18/16/14px at roomy `1.4–1.6` leading for descriptions;
  12–14px semibold/bold for prices, labels, eyebrows, and card metadata — the small
  sizes carry the commerce (price, rating, instructor) so they stay bold and legible.
- **Hierarchy:** 56px page statement → 32px section titles → 24px card-group titles →
  18/16px body → 14px commerce meta → 12px labels. Weight steps (300 body-light vs 700
  CTA/labels) separate reading text from acting text.

## 4. Component Stylings

- **Primary button:** purple fill (`#6D28D2`), white 14px/700 text, `8px` radius, `0 12px`
  padding — "Sign up". Compact and repeatable; the same shape works in header and hero.
- **Secondary button:** transparent fill, purple text, `1px` purple border, same 8px
  radius — "Log in". The **filled + outline dual CTA** (not ghost, a real bordered
  outline) is the signature: both buttons carry equal visual weight, conversion vs
  retention side by side.
- **On-dark variants:** white fill with ink text ("Subscribe now", "Get started" 16px/700,
  `0 48px` padding) and white-outline ghost ("Learn more") for inverted bands — same
  8px geometry, inverted roles.
- **Search:** header autocomplete input (4px radius, quiet border) — the most important
  component on the page, styled quieter than buttons so it invites typing rather than
  shouting.
- **Course cards:** image + title + instructor (slate) + amber star rating + price —
  a fixed information hierarchy repeated across every carousel; ratings are the
  marketplace's social proof engine.
- **Links:** purple, no underline by default, blue (`#1883FD`) on hover — color-shift
  feedback only, no layout movement.

## 5. Layout Principles

- **Spacing scale:** 8px base (1/4/5/6/8/10/12px micro steps); section rhythm from
  alternating white/tint bands rather than huge padding — density is the point, bands
  keep it scannable.
- **Section rhythm:** smart-bar campaign banner → header (nav + search + dual CTA) →
  search-led hero → category nav → course-card carousels → featured topics → career
  accelerators / AI roleplay bands → personal-plan banner → pricing → dark footer.
  Every band answers one shopper question: what, proof, price, next step.
- **Catalog grid:** course cards in horizontal carousels (homepage) collapsing to
  stacked grids — browsing density on desktop, thumb-scrolling on mobile.
- **Band inversion:** pastel campaign tints and one dark footer break the white rhythm
  — pacing through tonal bands instead of decorative dividers.

## 6. Depth & Elevation

- **Purple-tinted layered shadows** for cards and popovers (`2px/8px` + `4px/16px` at
  low opacity) — lift feels native to the brand hue rather than neutral gray.
- **Hairline rings for structure:** `0 0 0 1px` rings define inputs, filters, and card
  edges — structure through borders, shadows reserved for float moments (dropdowns,
  autocomplete, modals).
- **Feedback through color, not motion drama:** button/link hovers shift color
  (purple → brighter hover `#8330FC`, link → blue); no observed bounce or parallax —
  a marketplace must feel fast and stable, not playful.

## 7. Do's and Don'ts

- **Do:** white + ink AAA foundation; one purple for all actions; filled + outline dual
  CTAs; single-family weight-grade type; tinted bands for campaigns; amber stars as the
  trust currency; dark footer for closure.
- **Don't:** use slate `#71758E` for small or essential text (AA only); add a second
  acting color beside purple; gradient-fill promo bands (flat tints carry AAA text);
  restyle course-card hierarchy per section (repetition IS the usability); underline
  everything — reserve decoration for hover feedback.

## 8. Responsive Behavior

- Compact ladder (1280 → 1024 → 897 → 768 → 640 → 480 → 400) — tuned for catalog
  density rather than marketing drama; carousels become swipe strips, then stacked cards.
- Header collapses to search + menu; dual CTAs survive (Sign up retained, Log in moves
  to menu); hero search stays full-width and tappable.
- Course-card metadata (instructor, rating, price) keeps hierarchy at small sizes;
  14px/700 CTA text stays legible; filters collapse behind a "Filter" button.

## 9. Agent Prompt Guide

> Build a landing page with a **learning-marketplace aesthetic**: white canvas with
> tint bands (`#F6F7F9`/`#E9EAF2`), ink text (`#2A2B3F`, AAA), one purple action
> (`#6D28D2`, white text AAA) for every button and link, slate (`#71758E`) for
> light-only meta. One custom sans family, weight grades 300–700: medium display
> (56→24px, tight 1.0–1.1 leading), roomy body (18/16/14px, 1.4–1.6), bold 12–14px
> commerce labels. Dual 8px CTAs — purple-filled primary plus purple-outline
> secondary, white-on-dark variants for inverted bands. Search-led hero with
> autocomplete; course/topic cards in carousels with fixed hierarchy (image → title →
> instructor → amber stars → price). Campaigns as flat pastel bands (cyan/peach/
> lavender) with ink text, never gradients. Purple-tinted layered shadows for float,
> hairline rings for structure. Tone: energetic, democratic, competent — a bazaar of
> learning you can trust.

## 10. Component Map

1. Smart-bar — pastel campaign banner (cyan tint observed) with ink text; dismissible promo.
2. Header — logo left, category nav, autocomplete search center, outline "Log in" + filled "Sign up" right.
3. Hero — statement headline (56px) + prominent search + supporting visual.
4. Category nav — side-nav categories for topic browsing.
5. Course-card carousels — fixed hierarchy cards (image/title/instructor/stars/price) per topic row.
6. Featured topics band — topic index (`/featured-topics/`) for SEO + discovery depth.
7. Career accelerators band — outcome-led programs (`/career-accelerators/`).
8. AI roleplay band — interactive learning promo (`/ai-roleplay/`).
9. Personal-plan banner — lavender-tint subscription pitch with feature icons.
10. Pricing — plan cards + "Subscribe now" white-on-dark CTA.
11. Footer — dark ink (`#202230`), multi-column links, muted slate meta.

## 11. Pattern Position

Best fits an **education-marketplace landing** (no `education` pattern file exists yet —
this analysis is the seed): search-led discovery hero, catalog-card carousels with
rating proof, topic-index depth, outcome programs, subscription banner, transparent
pricing. It borrows the SaaS skeleton (hero → proof → features → pricing → CTA) but
replaces product screenshots with catalog density and star-rating social proof — the
genre markers to codify are search-first heroes, fixed-hierarchy course cards, and
tint-band campaign rhythms.

## 12. Synthesis Notes

- **Unique:** single custom family scaled across a whole marketplace (no pairing to
  imitate, just weight discipline); filled + *bordered-outline* dual CTA (both buttons
  equal weight, unlike ghost secondaries); tint-band campaign system with AAA ink text;
  amber star ratings as the trust currency; catalog-card repetition as usability.
- **Combine with:** Linear's dark restraint for a premium "pro learning" tier band;
  Ghost's editorial calm for instructor-storytelling sections; Maven's serif warmth for
  human-outcome narratives; Ramp's single-accent discipline (already mirrored here —
  swap purple for teal to change the brand temperature entirely).
- **Weaknesses / avoid:** density depends on real catalog depth — sparse content makes
  carousels feel empty, not rich; slate meta at small sizes is AA-only, don't copy it
  into essential roles; the purple + white-card look is strongly "Udemy" — lift the
  *system* (one action color, fixed card hierarchy, tint bands) with a different hue
  and family, never the exact purple + card combo.
