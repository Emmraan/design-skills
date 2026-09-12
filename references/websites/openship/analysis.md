# Openship — Design Analysis

> Source: `https://openship.io/` (open-source deployment platform) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/pricing`, `/features`, `/about`, `/contact`)

Openship is deployment-infrastructure drama: a near-black aurora hero (`#0F0F0F` manifest) breathing over 16–22s ambient cycles, a single custom geometric sans (Gellix), and a theming system of plum/sea/terra tint bands (`--th-clr-*-bg` at 8%) switched per section. Against Linear's restrained dark and Taste Skill's warm paper, this is the expressive pole of developer-tools — motion and tint carry the brand, not chrome.

## 1. Visual Theme & Atmosphere

- Mood: night-launch control room — dark aurora hero, glowing ticker, light content sections, tinted theme bands.
- Philosophy: infrastructure you can feel — ambient motion (breathe, sway, halo, ticker) sells "always running" better than any uptime badge.
- Mixed theme: dark-declared (`#0F0F0F` manifest) with white AAA content grounds — dark for drama, light for reading.

## 2. Color Palette & Roles

- Ink/ground: `#000000` (21 AAA on white) + `#2e2e2e` (13.58 AAA) + secondary `#737373` (4.74 AA); hairline `#e8e8e8`/`#efefef`/`#f0f0f0`.
- Theme tints: plum `#6c5ce7`, sea `#00b894`, terra `#e05874` — each washed at 8% alpha as section backgrounds via CSS vars (`--th-*`), so whole page zones re-theme without new components.
- Accent: lavender `#a29bfe` (hover `#8a84d8`) for dark-zone pills and badges.
- Dark zones: `#18191e` grounds with `#f3f4f4` (15.93 AAA) + `#8c8c8e` (5.23 AA) text; white 8–9% hairlines.
- Known fails: `#9e9e9e` on white 2.68, `#858585` AA-large only — decorative ticker/meta text, never body.

## 3. Typography Rules

- Single family: Gellix (custom, Thin→Black), weights 300/500/600, 84px display → 10px captions (25 steps) — one geometric voice at every size.
- Decision: licensing a distinctive grotesque replaces an accent color — the type IS the brand. Borrow for infra products that need personality without color noise.

## 4. Component Stylings

- CTAs: black pill (8×20px) primary + glassy dark pills (white 2% fill, 9% border, lavender variants with 45% borders) — solid for commitment, glass for exploration.
- Badges: 999px pills (13px/500) + 50% dots — status language borrowed from dashboards, used as marketing proof.
- Inputs (`/contact`): `#fafafa` fill, `#e8e8e8` border, 10px radius, 14px horizontal padding — quiet, high-contrast, zero decoration.
- Links: 3 styles resolving to `--th-text-heading` on hover — tint-aware links that follow the section theme.
- Favicon kit complete (16→512px + PWA + og/twitter images); SVG icon system; shadcn/ui + Radix + Tailwind under the hood.

## 5. Layout Principles

- 8px scale (1/2/4/6/8/10/12/13/14/16/18/22/24/80px) — 80px section air, dense 12–16px feature core.
- Funnel: aurora hero with ticker → tint-banded features → proof → pricing → about → contact — classic SaaS spine with theme-tinted vertebrae.
- 11 homepage gradients stage hero and bands; 10-step breakpoint ladder (1000→520px) collapses grids stepwise.

## 6. Depth & Elevation

- Micro ring+drop shadows (3–4% black) for cards + one dramatic `-20px 80px` upward glow for dark-zone staging — elevation as theater lighting.
- Decision: flat light sections, glowing dark zones — depth marks narrative beats, not hierarchy.

## 7. Do's and Don'ts

- Do: AAA ink pairs both themes; 8%-alpha tint bands for section theming; glass pills on dark; ticker for "live system" feel; 10-step responsive ladder.
- Do: keep muted greys decorative-only (they fail small text); keep aurora cycles slow (16s+) — ambient, never distracting.
- Don't: add a second accent (lavender + three tints is already the budget); don't speed up ambient motion; don't decorate form inputs.

## 8. Responsive Behavior

- 10 breakpoints (1000/980/900/820/768/720/640/620/600/520px) — ticker and aurora persist on mobile, grids stack, pills wrap; ambient keyframes are cheap transforms, safe on low-end.
- Touch: 999px pills and full-width inputs are thumb-first; ticker must pause on reduced-motion.

## 9. Agent Prompt Guide

- Quick reference: `developer-tools / aurora-dark / product-funnel / dark-declared mixed / high complexity / dual CTA (deploy + pricing)`.
- Ready-to-use prompt: "Design a deployment-platform page in the Openship logic: near-black aurora hero with 16–22s ambient breathe/sway cycles and a scrolling ticker, single geometric sans family from thin to black, 8%-alpha plum/sea/terra tint bands that re-theme each section via CSS variables, black pill primary CTAs with glassy dark-zone secondaries, dashboard-style status badges, ring-shadow cards with one dramatic dark-zone glow, AAA ink pairs in both themes, quiet 10px contact inputs, and a 10-step responsive ladder. Sell infrastructure as a living system, never as a dashboard screenshot."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Aurora hero + ticker (30s scroll) — "system is alive" statement.
2. Tint-banded feature zones — themed comparison without new components.
3. Status badges/pills — dashboard trust language.
4. Pricing (`/pricing`, 17/24 WCAG) — transparent packaging.
5. About + contact (`/contact` has the only inputs) — team + capture close.

### 11. Pattern Position

- Fits the infra-launch pattern: ambient hero → themed features → proof → pricing → contact. Against Linear (restrained dark, product-led) and Taste Skill (paper docs-led), Openship is expressive dark — the dev-tools trio now covers restraint, warmth, and drama.
- Page-flow logic: assume the developer fears downtime sub-consciously; every ambient pixel answers "this runs while you sleep."

### 12. Synthesis Notes

- Unique (borrow as logic): CSS-var tint-band theming at fixed 8% alpha; aurora ambient cycles as brand (16–30s keyframes); ticker as vitality signal; single-family type-as-brand; glass-on-dark CTA secondaries; dashboard badges as marketing.
- Combine with: Linear's restraint for docs pages (drama for launch, calm for reading — theme as narrative) and Taste Skill's install-command hero for the conversion moment Openship's funnel skips.
- Avoid: copying aurora + Gellix + lavender verbatim (reads "Openship clone"); fast ambient motion; tint bands stronger than ~8% (they stop being bands, start being noise); grey small text.
