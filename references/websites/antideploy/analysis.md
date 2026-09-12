# Antideploy — Design Analysis

> Source: `https://antideploy.com/` ("Connect your agent" — deploy infrastructure for coding agents) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 paths: `/`, `/pricing`, `/docs`, `/api/v1`, `/docs/quickstart` — `/api/v1` returns raw JSON, honestly zero tokens)

Antideploy is web brutalism with manners: pure blue (`#0000ff`, 8.16 AAA on paper) on warm paper (`#faf9f6`, ink `#09090b` at 18.9 AAA), Instrument Sans display, animated architecture diagrams (dgWire/wireDrift/diagramFloat keyframes), and a "Copy the prompt that connects your coding agent" pill CTA. Every link on the site hovers to `var(--blue)` — one destination, total discipline. The docs app runs its own orange manifest (`#ef7025`) with twoslash code-annotation tokens.

## 1. Visual Theme & Atmosphere

- Mood: blueprint with a pulse — warm paper, engineering blue, drifting wire diagrams, twoslash-annotated code.
- Philosophy: the agent is the user — copy-prompt CTAs, quickstart-first docs, API endpoint in the crawl path without apology.
- `/api/v1` in the extraction returning zero tokens is documented, not hidden — endpoints aren't pages.

## 2. Color Palette & Roles

- Grounds: warm paper `#faf9f6` + `#ffffff` + `#f5f1ef` hairlines + `#e3e0d8` card borders.
- Primary: pure blue `#0000ff` — 8.16 AAA on paper, the rare saturated primary that's also accessible; deep `#1800ad` manifest theme.
- Ink: `#09090b` (18.9 AAA) + `#45413f` (10.09 AAA) + `#5c5b55` (6.47 AA) + `#777371` (4.69 AA).
- Code accents: emerald `#16a672` (fails on paper 2.96 — badges/large only), tag blue `#3772cf`, warn amber `#c37d0d`, legal blue `#476cff`, teal `#4fa1ab`, docs orange `#ef7025`.
- Fail `#b0b2c2` on paper 2.0 decorative only.

## 3. Typography Rules

- Display: Instrument Sans 500–700, 84→8px — contemporary grotesque with graded weights (560/650!) for precise emphasis steps.
- UI: Inter 500–700 for app surfaces; PaperMono + IBM Plex Mono for code (14→8px) with cv02/cv03/cv04/cv11 alternates.
- Decision: three-layer type (display/UI/code) with weight grades instead of new families. Borrow for agent-infra seriousness.

## 4. Component Stylings

- Primary: blue 999px pill (12×20.8px) with blue glow shadow (`rgba(0,0,255,0.7)` 6×16) — the button radiates.
- Secondary: 3%-ink ghost 9999px pill — whisper-quiet alternative.
- Status pills: emerald-12% and blue-solid 999px badges (11–12px/600) — system state as jewelry.
- Agent CTA: "Copy the prompt that connects your coding agent" (999px) — machine onboarding as marketing.
- Links: 14 styles, ALL hovering to `var(--blue)` — the strictest hover discipline in the repo.
- Logo: 79×141 inline SVG `#0000ff` (portrait ratio — unusual, memorable) + full favicon set.

## 5. Layout Principles

- Fractional 0.8x spacing (12.8/3.2/23.2/2.4/5.6px + standards) — tighter rhythm than context.dev's 0.9x.
- Funnel: blue hero with wire diagrams → agent-connect CTA → pricing → docs/quickstart depth.
- 11 breakpoints (1040→700, tablet-dense: 1040/1024/900/860/859/840/820/767/760/720/700) — mid-range granularity nobody else bothers with.

## 6. Depth & Elevation

- Blue glow + ring shadows + one 5%-ink micro-drop — glow means primary, rings mean structure, drops barely exist.
- Animated diagrams (dgCell 0.3s → diagramFloat 5.4s) give depth through motion, not elevation.

## 7. Do's and Don'ts

- Do: AAA blue-on-paper + ink pairs; single hover destination; glow-primary buttons; wire-diagram motion; quickstart-first docs; tablet-dense breakpoints.
- Do: keep emerald badges large-or-decorative (2.96 fails); keep API endpoints out of design claims.
- Don't: add accent colors (blue + code-token set is the budget); don't solid-ify ghost secondaries; don't slow diagram motion past ambient.

## 8. Responsive Behavior

- 11-step tablet-dense ladder (1040→700) — mid-range devices get bespoke stops; verify small-phone (<700) manually, the ladder ends there.
- Touch: pill CTAs thumb-first; copy-prompt button must stay full-width on mobile.

## 9. Agent Prompt Guide

- Quick reference: `ai / blue-brutal / product-funnel / light / high complexity / dual CTA (copy agent prompt + pricing)`.
- Ready-to-use prompt: "Design an agent-deploy-infrastructure page in the Antideploy logic: warm paper grounds with AAA ink text, pure accessible blue primary with glow-shadow buttons, Instrument-Sans-style graded grotesque with mono for code, every link hovering to one blue destination, animated wire architecture diagrams, copy-the-agent-prompt pill CTAs, emerald status badges, fractional tight spacing, tablet-dense responsive ladder. Sell to the agent through the human."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Blue hero + wire diagrams — living-architecture statement.
2. Agent-prompt copy pill — machine onboarding.
3. Pricing (`/pricing`) — packaging transparency.
4. Docs + quickstart (150k+159k chars, orange manifest) — depth with its own accent.
5. API endpoint (`/api/v1`, zero tokens) — honest infrastructure surface.

### 11. Pattern Position

- Fits the agent-infra pattern: electrify (blue) → equip (copy prompt) → prove (diagrams) → package (pricing) → deepen (docs). Against Context.dev (rainbow maximalism) and Firecrawl (ember minimalism), Antideploy is brutalist blue — maximal restraint, maximal color.
- Page-flow logic: assume the human pastes and the agent reads; copy must survive both audiences.

### 12. Synthesis Notes

- Unique (borrow as logic): single-destination link hovers; accessible saturated primary; glow-as-primary; wire-diagram motion system; agent-prompt CTA; tablet-dense breakpoints; fractional-tight spacing; portrait-ratio logo; honest zero-token endpoint documentation.
- Combine with: Context.dev's dynamic OG for share-worthy agent pages and Firecrawl's badge jewelry for compatibility proof Antideploy lacks.
- Avoid: copying blue-paper + Instrument verbatim (reads "Antideploy clone"); second primaries; decorative emerald text; hiding the API — endpoints are trust.
