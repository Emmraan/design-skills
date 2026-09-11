# Vita Travel — Design Analysis

> Source: `https://vita-travel.webflow.io/` · Baseline: `baseline.json` · Collected: 2026-09-11 (Dembrandt 0.32.2)
> Vita Travel is a retreat-travel site (retreats, coaches, contacts — e.g. a 7-day
> mountain retreat in Romania). The design is **night-camp calm with ember energy**:
> a near-black teal canvas, white ink at AAA, generous pill CTAs, and a single
> orange accent that acts like firelight — warmth and booking urgency against the dark.

## 1. Visual Theme & Atmosphere

- **Retreat after dark.** Deep teal-black (`#091b20`) everywhere, white headlines at
  17.66:1 — the page feels like evening at a mountain lodge: quiet, premium, intimate.
- **Ember accent:** orange (`#FB9826`/`#FA8805`) appears sparingly at AAA contrast on
  the dark — highlights, hovers, key moments. Warmth is rationed, so it reads as
  special, not noisy.
- **Template clarity:** a compact Webflow build — statement hero ("Explore Retreats"),
  retreat/coaches/contacts pages, one conversion CTA repeated. Nothing decorative
  survives; every element books or informs.
- Mood: calm, grounded, quietly adventurous — wellness travel without pastel clichés.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Canvas | deep teal-black `#091B20` | Page background (white on it 17.66:1, AAA); the night the content glows against |
| Ink | white `#FFFFFF` | Headlines + body on dark (AAA); the voice |
| Structure | deep teal `#0D2E37` | Header/button fills, tonal bands — structure one step lighter than canvas |
| Ember | orange `#FB9826` / `#FA8805` | Accent moments — on dark 7–8:1 (AAA); firelight, never background |
| Link blue | `#0000EE` | Links on LIGHT surfaces only (on white 9.4:1, AAA) — on dark it fails (1.5–1.9:1) |
| Secondary text | gray `#9DA4A6` | Meta on dark (6.97:1, AA) — descriptions and supporting lines |
| Large-only gray | `#6B7679` | 3.78:1 on dark — large text only, never body |
| Hairlines | white at 10% alpha | `1px solid rgba(255,255,255,0.1)` dividers — structure without visible lines |

- **Two lights, two jobs:** white speaks, orange ignites. Blue links only where a
  light surface exists (buttons, light cards) — on dark bands, links go white/600.
- **Dark handling:** dark-first with tonal steps (`#091B20` → `#0D2E37`) instead of
  shadows — depth through color temperature, not elevation.

## 3. Typography Rules

- **One workhorse family:** Inter (Google Fonts, 300–700) does everything — display
  through meta. Retreat calm comes from spacing and tracking, not font romance.
- **Display with bite:** 60px/600 at tight `1.1` leading with **-3.6px tracking** —
  headlines feel carved and confident; the negative tracking is the brand's voice.
- **Section ladder:** 45px/600 (`1.0`, -3px) statements → 24px/600 body-leads →
  22/18px medium subheads → 16px/400 body (`1.25–1.3`) → 14px/600 labels → 12px meta.
  Tight leading up top, readable leading in body — drama first, comfort after.
- **Hierarchy:** size + tracking do the work (weight stays 400–600); links on dark go
  600 so they hold against the canvas.

## 4. Component Stylings

- **Primary button:** the signature — white fill, blue `#0000EE` text, fully pill
  `80px` radius, generous `20px 32px` padding ("Explore Retreats"). A big friendly
  pill glowing on the dark; radius used 12× site-wide, the most repeated token.
- **Secondary/dark button:** deep-teal fill (`#0D2E37`) pill, same 80px geometry,
  smaller `14px 24px` padding — quiet sibling for dismissive actions ("Decline" in
  the consent banner). Same shape language, stepped-down presence.
- **Links:** blue, no underline on light; white/600, no underline on dark — color and
  weight signal interactivity, never decoration. Hover/focus states shift toward
  orange (`#FB9826`/`#FA8805` at AAA) — ember feedback on interaction.
- **Logo:** inline SVG mark (20px, blue) in header — tiny, geometric, no wordmark
  dependency; icon system is pure SVG.
- **Structure:** hairline white-10% borders for divs; underline-style hairlines for
  text links where needed — everything structural dissolves into the dark.

## 5. Layout Principles

- **Spacing scale:** 8px base (8/14/16/20/30/32px steps) — compact and rhythmic;
  generous button padding (20×32) against tight section rhythm keeps the page
  breathable without being empty.
- **Section rhythm:** header (logo + nav + pill CTA) → statement hero (60px display +
  Explore Retreats) → retreat listings → coaches → contacts → footer. One question
  per band: where, with whom, how to book.
- **Single conversion path:** one CTA shape, one CTA color logic, repeated — the
  whole page funnels to "Explore Retreats"; secondary pages (coaches, contacts)
  support rather than compete.
- **Band pacing:** tonal steps between canvas and structure-teal separate sections —
  no cards-on-gray, no dividers shouting.

## 6. Depth & Elevation

- **No shadows, no gradients observed** — depth is purely tonal (canvas vs structure
  teal) plus hairline rings. On near-black, shadows would be invisible anyway; the
  system is honest about its medium.
- **Motion is the elevation:** `0.2s ease` across links (10 contexts), buttons (3),
  hero (1) — hover/focus color shifts toward ember orange give the only sense of
  lift. Fast, uniform, calm — nothing bounces on a retreat page.
- **Feedback through warmth:** interactive deltas move toward orange on hover/focus
  at AAA — the interface literally warms under the cursor.

## 7. Do's and Don'ts

- **Do:** near-black teal canvas with AAA white ink; one pill radius (80px) for all
  buttons; generous CTA padding; single-family Inter with negative display tracking;
  rationed ember-orange accents; tonal (not shadow) depth; 0.2s ease everywhere.
- **Don't:** put blue `#0000EE` text on dark (1.5:1, fails) — blue links need light
  surfaces; use `#6B7679` for body text (3.78:1, large-only); add shadows/gradients
  on near-black (invisible clutter); use a second CTA shape — the pill IS the brand;
  paste pastel wellness clichés over this palette.

## 8. Responsive Behavior

- Compact Webflow ladder (479 → 767/768 → 800 → 991 → 1024 → 1440 → 1920) — display
  60px scales down, pill CTAs keep 80px radius and padding at thumb sizes.
- Header collapses to logo + menu; Explore Retreats survives as the sticky action.
- Retreat/coach content stacks single-column; hairline structure holds without
  shadows at small widths.

## 9. Agent Prompt Guide

> Build a landing page with a **dark retreat-travel aesthetic**: near-black teal
> canvas (`#091B20`), white ink (AAA 17.7:1), structure teal (`#0D2E37`) for tonal
> bands, ember orange (`#FB9826`) rationed to accent/hover moments (AAA on dark),
> muted gray (`#9DA4A6`) for AA meta. One sans family (Inter): 60px/600 display with
> tight leading (1.1) and negative tracking (-3.6px), 45px section statements, 24→16px
> body ladder, 14px semibold labels. Fully pill buttons (80px) — white-fill primary
> with blue text and generous 20×32 padding, dark-fill quiet secondary. Links blue
> on light, white semibold on dark, warming to orange on hover. Hairline white-10%
> dividers, zero shadows, zero gradients. Uniform 0.2s ease motion. Tone: calm,
> grounded, quietly adventurous — night-camp calm with ember energy.

## 10. Component Map

1. Header — inline SVG logo mark left, retreat/coaches/contacts nav, white pill "Explore Retreats" right.
2. Hero — 60px tracked display statement + primary pill CTA over dark canvas (0.2s ease-in motion).
3. Retreat listings — retreat destinations (e.g. 7-day mountain retreat) with ember highlights.
4. Coaches band — guide/team proof with secondary gray descriptions.
5. Contacts band — booking enquiry path.
6. Consent banner — dark pill "Decline" secondary action, same 80px geometry.
7. Footer — dark, hairline-separated links.

## 11. Pattern Position

Best fits a **travel landing** (no `travel` pattern file exists yet — this analysis
is the seed): statement hero → listings → people-proof (coaches) → booking path →
footer. It borrows the SaaS skeleton (hero → proof → CTA) but replaces product proof
with place + people proof — the genre markers to codify are destination listings as
the proof band and a single repeated booking CTA instead of tiered pricing.

## 12. Synthesis Notes

- **Unique:** pill-CTA-as-brand (80px everywhere, 12 uses — radius as identity);
  negative display tracking as voice; ember-rationing (one warm accent, AAA, used
  like firelight); tonal-not-shadow depth honest to near-black; hover-that-warms
  interaction model.
- **Combine with:** Ghost's editorial calm for retreat storytelling/long-form;
  Udemy's fixed-hierarchy cards for retreat listings at scale; Maven's serif warmth
  for human-outcome narratives; Linear's dark restraint for premium-tier bands.
- **Weaknesses / avoid:** robots.txt blocked subpage crawl (listings depth unobserved —
  don't invent card systems beyond the evidence); blue-on-dark and gray-body traps
  are baked into the source — copy the system, not the failures; the teal-dark +
  orange-pill look is strongly "Vita" — lift the *system* (pill CTA, ember rationing,
  tonal depth) with a different hue pair, never the exact palette.
