# Kota — Design Analysis

> Source: `https://kota.co.uk/` · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/contact`, `/start-your-project`, `/blog`, `/newsletter`)

KOTA is a London creative/digital agency. The site is a craft pitch: monochrome canvas, oversized single-family typography, and one animated rainbow-gradient moment. It reads bold-brutalist but stays highly legible (WCAG AAA on core pairs).

## 1. Visual Theme & Atmosphere

- Mood: confident, loud, playful-precision. Giant uppercase headlines do the selling; the rest of the page stays quiet so the type lands.
- Philosophy: constraint as craft — one typeface, two neutrals, one electric link blue, one gradient party-trick. Nothing decorative beyond that.
- Light-first theme: warm light-grey (`#EFEFEF`) page ground with black type, inverted to full-black panels for contrast beats (stats, footer, CTA bands).

## 2. Color Palette & Roles

- Ground / surface: light grey `#EFEFEF` (page background) + pure white `#FFFFFF` (cards, panels, badges).
- Ink: black `#000000` — primary text, primary buttons, logo, borders. 5,503 high-confidence uses across all 5 pages. Contrast vs ground 18.26:1 (AAA, 897 samples); vs white 21:1 (AAA, 571 samples).
- Link accent: electric blue `#0000EE` — links and interactive affordances only. 8.17:1 vs ground (AAA) but 2.23:1 vs black, so it never sits on dark panels.
- Signature gradient (animated): violet `#633CC9` → teal `#3B8392` → magenta `#CB24CC`, `linear-gradient(90deg, …)`, 26 uses. Applied as animated rainbow text treatments on hero links, footer links, contact details, and statistics panels (3s ease-in-out loops).
- Muted neutrals: `#7B7B7B` / `#504F4F` for secondary text. Note: `#7B7B7B` on black is 4.96 (AA only) and on ground 3.68 (large-text only) — decorative/secondary use, not body copy.
- Known weak pair: white on `#EFEFEF` at 1.15:1 (108 samples) — fails everything; these are borders/ghost shapes, never text. Do not copy as a text treatment.

## 3. Typography Rules

- Single family everywhere: Neue Montreal (`__montreal_a78db3`, self-hosted woff2). No pairing — hierarchy comes purely from scale, weight, and case.
- Scale logic: display 307px/0.9 → 160px H2 uppercase with −3.2px tracking → 120px → 80/70/60px section heads → 44/40px leads → 34–12px body/labels. Tight line-heights (0.9–1.0) on display, relaxed (1.25–1.5) on body.
- Weights: 400 default, 300 for large light statements, 600 for emphasis links/labels. Uppercase reserved for the biggest headings.
- Decision: one grotesk at extreme scale contrast reads more "agency-confident" than any font pairing would. Borrow the logic (scale + case + tracking), not the 307px value itself.

## 4. Component Stylings

- Buttons: pill-first language. Primary = black pill (32–33px radius), white text, 15–22px horizontal padding ("Hire us" 18px ×4). Secondary = ghost pills with 2px black/white borders, or translucent white fills. Large form submits scale the same pill up to 28.8px type with 2px borders.
- Badges / filter chips / blog tags: same pill radius (32px on `li`/badge elements, 373 samples) with 2px outlines — filters read as buttons, which keeps the whole site tappable-feeling.
- Images/media: soft rectangles, 11px (253 samples) and 18px (15) radii — deliberately less round than pills, so photos feel calm against loud type.
- Inputs: underline-only (bottom 1px solid, no box radius) — forms stay minimal; the Submit pill carries the emphasis.
- Links: blue default; rainbow-gradient animated variant for showcase moments (contact, footer, hero).
- Logo: inline SVG wordmark/square in black, header context.

## 5. Layout Principles

- 8px-based spacing scale (8px ×708, plus 17.6/5/10/12/32px steps). Rhythm is generous-section / tight-type: huge headlines with tight leading, then airy padding between bands.
- Grid: full-bleed type bands alternating light/black; content panels inset as white cards. One-off asymmetric radius (`0 150px 0 0`) on divs signals deliberate rule-breaking at section joints.
- Section order (observed across crawl): oversized hero statement → services panel → work/case proof → statistics band → featured blog post → marquee strip → contact/start-project CTA → footer.

## 6. Depth & Elevation

- No shadow system at all (zero shadows extracted). Depth comes from tonal inversion (grey ↔ black ↔ white) and 1–2px borders: 2px solid black/white on interactive elements, 1px white-at-30% on dark links, underline borders on inputs.
- Decision: flat + high-contrast + outlined pills = crisp at every breakpoint, zero shadow-tuning cost. Works because the type scale already creates hierarchy.

## 7. Do's and Don'ts

- Do: one family, extreme scale contrast; monochrome + single accent; pills for everything clickable; animate the gradient, not the layout.
- Do: keep muted greys to secondary/decorative roles (their contrast is AA-or-worse).
- Don't: place electric blue on black (2.23:1); don't set white text on the light ground; don't add shadows — the system has none and doesn't need them.
- Don't: mix a second typeface in — the single-family discipline is the brand.

## 8. Responsive Behavior

- Wide breakpoint ladder (20 stops from 1920px down to 499px): 1920/1450/1400/1300/1200/1150/1100/1024/1000/900/899/850/849/769/768/600/599/550/500/499. Collapse strategy is type-first: display sizes step down through the ladder while pills stay ≥44px-equivalent touch targets.
- Touch: pills and chips are naturally large; underline inputs avoid tiny tap zones. Marquee (20s linear) and rainbow loops are the only continuous motion — both pause-safe candidates for `prefers-reduced-motion`.

## 9. Agent Prompt Guide

- Quick reference: `agency / bold-brutalist / type-led-hero / light with black inversions / high complexity / single CTA ("Hire us")`.
- Ready-to-use prompt: "Design a bold agency page in the KOTA logic: light-grey ground with black inverted bands, single grotesk family with extreme scale contrast (giant tight uppercase display, small relaxed body), pill buttons/chips throughout (black primary, outlined ghosts), underline-only inputs, photos at small radii, no shadows, electric-blue links, and ONE animated violet-teal-magenta gradient text moment for the hero/footer. Keep body contrast AAA; keep muted greys decorative only."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Giant type hero (307/160px statement + black "Hire us" pill) — stance first, nav second.
2. Services panel (white ground, pill chips per offering) — scannable capability list.
3. Selected-work proof band — images at 11/18px radii against loud type.
4. Statistics band (black ground, rainbow-animated figures) — credibility with playfulness.
5. Featured blog post module — editorial depth, "Strategy first. Always" voice.
6. Marquee strip (20s linear) — motion divider between proof and conversion.
7. Start-your-project / contact CTA (large pill Submit, underline inputs) — single conversion goal.
8. Footer (black, rainbow link treatments) — sitemap + personality sign-off.
9. Blog + newsletter pages — same system extended to long-form and capture.

### 11. Pattern Position

- Fits the agency pattern (`patterns/portfolio-agency.md`): demonstrate craft → build affinity → start a conversation. KOTA compresses it: the typography IS the portfolio — craft is proven in the first viewport, work proof follows, conversion is always one "Hire us" away.
- Page-flow logic: shock (scale) → orient (services) → prove (work + stats) → voice (blog) → convert (contact). The alternating light/black bands pace scrolling like chapters.

### 12. Synthesis Notes

- Unique (borrow as logic): single-family extreme-scale typography as brand; monochrome + one animated gradient moment instead of a broad accent system; pill-everything clickability; zero-shadow flat depth via tonal inversion and 2px outlines.
- Combine with: Primora's editorial-premium polish (KOTA brings loudness, Primora brings refinement) and a product reference (Ghost/Mobbin restraint) to temper the maximalism; portfolio-agency galleries for case-study depth KOTA implies but doesn't fully show in tokens.
- Avoid: copying the 307px display size or the exact violet-teal-magenta gradient verbatim; low-contrast grey-on-grey text; blue-on-black links; adding shadows or a second typeface — each would break the constraint system that makes this work.
