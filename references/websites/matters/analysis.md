# Matters — Design Analysis

> Source: `https://www.matters.sg/` · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/about`, `/work`, `/work/subaru-singapore`, `/work/effortlessly-free`)

Matters is a Singapore branding/design practice site (Tony Thong, Webflow-built). It is the dark, texture-led counterpart to KOTA's light brutalism: near-black ground, warm bone type, one acid-lime accent, heavyweight grotesk headlines cut with serif-italic asides, and a film-grain overlay for analog warmth.

## 1. Visual Theme & Atmosphere

- Mood: after-hours studio — intimate, confident, slightly rebellious. Dark ground with electric-lime sparks reads creative-director rather than corporate-agency.
- Philosophy: personality through pairing and texture, not through color count. Two typefaces, three neutrals, one accent, one grain overlay.
- Voice-led: hero statements are stances ("The right idea saves everything", "Because how it looks is how it…"), selling taste before process.

## 2. Color Palette & Roles

- Ground: near-black `#171717` / `#1A1B1F` (716 high-confidence uses, all 5 pages). Everything lives on this.
- Primary text: warm bone `#E3E1D8` (202 uses) — softer than pure white, 13.68:1 vs ground (AAA). Supporting off-whites `#DDDDD2` / `#F3F0DD` / `#F5F8F7` play the same role at lower emphasis.
- Accent: acid lime `#E6FF5A` (163 uses, hero titles + key descriptors) — 16.06:1 on black (AAA, 125 samples) but 1.23 on light grounds, so it is strictly a dark-ground accent. Never place it on bone.
- Secondary tint: pale aqua `#D1ECEE` (ghost links at 30% alpha) + taupe `#ABAAA3` for hover states (5.34:1 vs dark text, AA).
- Depth neutral: charcoal `#403F3D` (266 uses) for panels/blocks on the dark ground.
- Known weak pairs (decorative only): mid-grey `#43464D` on black at 1.9 (26 samples), white on `#DDDDD2` at 1.37, `#333333` on black at 1.42 — ambience, never body copy. One case-study red `#D83D35` with off-white at 4.24 passes large-text only.
- No gradients, no shadows — flat dark layers separated by tone and grain.

## 3. Typography Rules

- Pairing logic: Montserrat Variable (Google Fonts, weights 200–900) for massive grotesk statements + Awesome Serif Italic variable for contrast asides. Heavy-shout vs soft-whisper is the whole brand voice.
- Scale: display 384px/900 → 269px/700 → 192px/800 → 154px → 134px serif → stepped down through 77/56/38px to 12.8px labels. Tight leading (0.9–1.0) on display, generous (1.75–2.31) on small body.
- Decision: weight does the hierarchy work (700–900 up top, 300–500 in body), so color can stay restrained. Borrow the shout/whisper pairing logic, not the 384px value.

## 4. Component Stylings

- Buttons: oversized pills — 160px radius "Menu", 400px radius contact pills ("hello@matters.sg / Come say hello", "Start a Brief"). Dark fills on dark ground, defined by shape and bone text rather than contrast fills.
- Badges: transparent ground, bone text, ~10/19px padding — quieter siblings of the button pills.
- Links: underline-capable with color-shift hovers (grey → `#32343A`) and subtle press-down scale (0.94 matrix). No decoration by default on nav links; editorial links underline.
- Cards/work covers: bone-tinted bars (`bar_work-cover`) over dark — case thumbnails read as light windows punched into the black page.
- Inputs: none observed (conversion happens via email/brief links, not forms) — a deliberate low-friction choice for a solo practice.

## 5. Layout Principles

- 8px-based scale with fine sub-steps (3/3.2/3.84/4/4.8/5.4/6.4/8px) — Webflow-style granular control for optical alignment of oversized type.
- Full-bleed dark bands; work covers as inset light windows; hero type routinely bleeds past viewport edges (overflow-as-style).
- Section order: stance hero → selected-work covers → about/position → case-study depth (Subaru, Effortlessly Free) → brief/contact CTA → footer.

## 6. Depth & Elevation

- Zero shadows, zero gradients. Depth stack: black ground → charcoal blocks → bone windows → lime sparks → grain overlay on top of everything.
- The `grain` animation (0.7s, steps(3), all pages) is the elevation system: analog noise unifies flat layers the way a shadow system would on a product site.

## 7. Do's and Don'ts

- Do: dark-ground-only lime; bone instead of pure white for warmth; serif-italic asides against grotesk shouts; grain for cohesion.
- Do: keep pill radii extreme (160–400px) — the softness offsets the heavy type.
- Don't: set lime on light grounds (1.23:1); don't use mid-greys for text on black; don't add shadows or gradients — the system is flat by design.
- Don't: add a contact form — the mailto/brief-link conversion is part of the low-ceremony positioning.

## 8. Responsive Behavior

- Webflow-standard ladder: 992/991/768/767/479px. Type-first collapse: colossal display steps down through stops while pills and work covers reflow to single column.
- Touch: giant pills are inherently tappable; underline-free nav avoids tiny targets. Grain + marquee are the only continuous motion — both pause-safe under `prefers-reduced-motion`.

## 9. Agent Prompt Guide

- Quick reference: `agency / dark-expressive / work-led / dark / medium complexity / single CTA ("Start a Brief")`.
- Ready-to-use prompt: "Design a dark expressive studio page in the Matters logic: near-black ground with warm-bone text, one acid-lime accent reserved for dark backgrounds, heavyweight grotesk display paired with serif-italic asides, oversized pill buttons and contact chips, work covers as light windows on the dark page, flat layers with a subtle film-grain overlay instead of shadows, fast 0.2s ease interactions plus one slow marquee. Keep body contrast AAA; keep mid-greys decorative only."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Stance hero (384px grotesk + serif-italic aside + lime spark) — taste first.
2. Selected-work covers (bone bars on black) — proof without leaving the page.
3. Marquee strip (10s linear) — motion divider.
4. About/position band — who and why, briefly.
5. Case-study pages (Subaru Singapore, Effortlessly Free) — depth for serious buyers.
6. Brief CTA (giant pill, mailto-first) — single conversion goal.
7. Footer (contact, socials, sitemap) — quiet sign-off on black.

### 11. Pattern Position

- Fits the agency pattern (`patterns/portfolio-agency.md`) in solo-practice form: personality → proof → contact, with no process theater. Where KOTA proves craft through typographic volume and Primora through editorial polish, Matters proves it through taste collisions (grotesk × serif, black × lime, digital × grain).
- Page-flow logic: provoke (stance) → show (covers) → convince (cases) → convert (brief). The work covers do double duty as visual rhythm and credibility.

### 12. Synthesis Notes

- Unique (borrow as logic): shout/whisper type pairing at extreme weights; dark-ground-only acid accent discipline; film grain as a shadow replacement; mailto-first conversion instead of forms; light-window work covers on a black page.
- Combine with: KOTA's pill system and section pacing (both speak pill; together they define an agency component language) and Primora's editorial refinement to civilize the maximalism. KOTA + Matters together give a light/dark agency pair — synthesize one page that can swing both ways.
- Avoid: copying the lime-on-black + grain combo verbatim (it is becoming a studio cliché); low-contrast grey text; gradients/shadows that fight the flat system; shrinking the display type to "safe" sizes — the scale IS the design.
