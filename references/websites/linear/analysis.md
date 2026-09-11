# Linear — Design Analysis

> Source: `https://linear.app/` · Baseline: `baseline.json` · Collected: 2026-09-11 (Dembrandt 0.32.2)
> Linear is issue tracking & project management for software teams. The marketing site is
> a masterclass in **dark, surgical developer minimalism**: a near-black canvas, off-white
> type at AAA contrast, one family of type, pill CTAs — calm, fast, and engineered.

## 1. Visual Theme & Atmosphere

- **Dark command-center.** Near-black canvas (`#08090A`) with off-white type (`#F7F8F8`).
  The page feels like the product itself: a tool, not a billboard.
- **Surgical restraint:** color is rationed — neutrals do 95% of the work, accents appear
  only where they have a job (action, link, status). Nothing decorative.
- **Engineered calm:** generous negative space, quiet hairlines, small precise type for
  meta content. Confidence expressed through precision, not loudness.
- Mood: focused, premium, technical-but-warm — craft for people who build software.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Canvas | near-black `#08090A` | Page background, dark-first |
| Text | off-white `#F7F8F8` | Headlines + body (18.7:1, AAA) |
| Secondary text | gray `#8A8F98` | Descriptions, meta (6.1:1, AA) |
| Structure | `#62666D` / `#202122` | Borders, muted surfaces, hairlines |
| Primary accent | green `#27A644` | Brand + primary action color |
| Link / focus | blue `#4EA7FC` | Links, focus states |
| Energy accent | lime `#E4F222` | Secondary highlights, moments of energy |
| Info accent | periwinkle `#828FFF` | Tertiary highlights |
| Destructive | red `#EB5757` | Errors/destructive only, never decoration |

- **One accent per job:** green acts, blue links, red warns — accents never compete on the
  same element. This discipline is the system.
- **Text is off-white, never pure `#FFF`** — softer on dark, premium.
- **Dark handling:** dark-first (not a dark mode toggle); depth comes from hairlines and
  inset borders rather than lighter panels.

## 3. Typography Rules

- **Family:** Inter Variable — a single workhorse family, differentiated by weight
  (300–700) rather than multiple faces. Fallbacks are system grotesques.
- **Weight-as-hierarchy:** semibold grades (510/590) instead of full bold — headlines feel
  crisp, never heavy. Display at tight `line-height 1.0` (72px → 48px → 32px).
- **Display details:** negative tracking on big headlines (`-1.58px` at 72px) plus
  OpenType features (`cv01`, `ss03`) for distinctive letterforms.
- **Body:** 15–18px at `1.5–1.6` leading, comfortable measure for long product copy.
- **Mono for the technical:** Berkeley Mono (12–14px) for code, keyboard hints, and
  technical labels — signals "built for developers" instantly.
- **Labels:** 10–13px muted gray for eyebrows, meta, legal — quiet and precise.
- A serif display face (Tiempos) ships in the font stack for editorial headline moments.

## 4. Component Stylings

- **Primary button:** light pill (`#E5E5E6` fill, near-black text, `9999px` radius,
  `0 20px` padding) — "Get started". Inverted against the dark canvas, impossible to miss.
- **Secondary button:** ghost pill (translucent white fill, off-white text, same radius)
  — "Contact sales". The **dual-pill CTA** (light + ghost) is the signature move.
- **Tertiary chip:** 16px radius, hairline border, 12px type — quiet actions.
- **Cards:** dark surfaces with 1px inset hairlines (`rgba(255,255,255,0.03–0.05)`),
  small radii — structure through borders, not shadows.
- **Inputs:** minimal, square-ish, quiet padding — form follows function.
- **Primitives:** Radix UI under the hood — accessibility (focus, keyboard, ARIA) comes
  from the component base, not bolted on.

## 5. Layout Principles

- **Spacing scale:** 8px base with tight micro steps; large section padding creates the
  calm rhythm — dense UI details floating in generous negative space.
- **Section rhythm:** statement headline → supporting copy → dual-pill CTA → product
  proof → feature deep-dives → pricing → closing CTA. Each section earns attention once.
- **Breakpoints:** dense fluid scale (1601 → 1536 → 1440 → 1280 → 1160 → mobile) —
  continuous refinement rather than 2–3 crude jumps.
- **Grid:** centered, narrow-measure compositions; the product visual is the hero's
  co-star, not decoration.

## 6. Depth & Elevation

- **Hairlines over shadows** for structure: 1px inset borders define cards and panels.
- **Layered soft shadows** for float moments (dialogs, dropdowns): stacked low-opacity
  black shadows plus a faint light inset on top edge — lifted, not glowing.
- **Ambient gradients (17 observed):** subtle dark glows behind sections — atmosphere,
  never decoration. Restraint keeps them premium.

## 7. Do's and Don'ts

- **Do:** dark-first canvas; one family + weight grades; dual-pill CTAs; hairline
  structure; AAA body contrast; mono for technical labels; accessible primitives.
- **Don't:** add a second competing accent on one element; use pure white text or pure
  black canvas; decorate with gradients; round everything the same — radius carries
  meaning (pills act, small radii whisper).

## 8. Responsive Behavior

- Display type fluid-scales down the dense breakpoint ladder; hero stacks to single
  column with CTA pair intact.
- Nav collapses, primary CTA retained; hairline cards stack without losing hierarchy.
- Touch targets stay comfortable; mono labels and meta remain legible at small sizes.

## 9. Agent Prompt Guide

> Build a landing page with a **dark developer-minimal aesthetic**: near-black canvas
> (`#08090A`), off-white type (`#F7F8F8`, AAA), secondary gray (`#8A8F98`) for meta.
> One type family (Inter-style variable sans, semibold grades 500–600, tight display
> leading, negative tracking on headlines) + a mono face for technical labels. Dual-pill
> CTAs — light filled primary plus ghost secondary. Structure with 1px hairlines, small
> radii for chips, layered soft shadows only for floating elements. One accent per job
> (green acts, blue links, red warns). Content tone: calm, precise, engineered — a tool,
> not a billboard.

## 10. Component Map

1. Navbar — dark, hairline-bottom; logo left, quiet links, dual-pill CTA right.
2. Hero — centered statement type (72px, tight) + dual-pill CTA + product visual.
3. Logo cloud / trust bar — customer logos as a quiet muted band.
4. Features / product deep-dives — alternating rows pairing copy with UI proof.
5. Stats / proof — restrained numbers band; proof through product, not hype.
6. Pricing — tiered cards on dark, highlighted plan, pill CTA per tier.
7. CTA band — closing statement + the dual-pill pattern repeated.
8. Footer — muted multi-column, meta gray, legal quiet.

## 11. Pattern Position

Best fits the **saas-landing** pattern (`patterns/saas-landing.md`) executed with
developer-tool restraint: trust-forward hero, product-as-proof, transparent pricing.
No `developer-tools` pattern file exists yet — this analysis is the seed for one (C2):
dark-first canvas, mono technical labels, and product-screenshot heroes are the genre
markers to codify.

## 12. Synthesis Notes

- **Unique:** the dual-pill CTA system (light + ghost); weight-grade typography instead
  of multi-family pairing; hairline-based dark structure; one-accent-per-job discipline;
  Radix-based accessible components as a design decision.
- **Combine with:** Ramp's single-electric-accent logic (swap green for lime to change
  the brand temperature); Ghost's type-led calm for content sections; Wispr's warm
  editorial serif for a less technical voice.
- **Weaknesses / avoid:** dark-first excludes light-mode audiences — don't default to it
  for consumer/friendly brands; the aesthetic depends on restraint, so adding marketing
  ornament breaks it fast; avoid copying the exact green + pill combo without changing
  roles (that reads as a Linear clone, not inspiration).
