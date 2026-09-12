# Context7 — Design Analysis

> Source: `https://context7.com/` (up-to-date documentation API for LLMs and AI coding agents) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/plans`, `/about`, `/enterprise`, `/contact`)

Context7 is documentation-grade calm: Tailwind stone (`#fafaf9`/`#292524` at 14.52 AAA), one emerald (`#059669`, honestly AA-large-only at 3.61), Inter + JetBrains Mono, and a library-search input as the hero. Against AI siblings (Wispr's voice, Sendr's utility, Primora's craft), this is the infrastructure pole — it sells to developers building agents, in docs readers trust.

## 1. Visual Theme & Atmosphere

- Mood: well-kept library reading room — stone paper, hairline tables, mono callouts, no decoration budget spent anywhere except the search.
- Philosophy: accuracy as aesthetic — the page looks like correct documentation because correct documentation is the product.
- Announcement bar + support pill ("Open support", 50px) frame the page as a maintained service, not a launch.

## 2. Color Palette & Roles

- System: stone bg `#fafaf9` + ink `#292524` (14.52 AAA) + white surfaces + `#d5d2d0` hairlines + `#78716c` secondary (4.59 AA) + `#57534e` (7.3 AAA).
- Brand: emerald `#059669` — AA-large-only on stone (3.61) and white-on-emerald (3.77): large-text and button-only discipline, honestly observed.
- Depth: deep `#064e3b` (hover `#075e47`) — every link on the site hovers to `#036546`. One hover color site-wide.
- Wash: mint `#d1fae5` accents (hover `#b2d5c3`); fail `#a8a29e` on stone 2.41 decorative only.

## 3. Typography Rules

- Voice: Inter 500/600, 36→11px — quiet, bookish, never below 500 weight.
- Code: JetBrains Mono 500, 14px — library names and identifiers speak mono.
- OpenType calt/liga — ligatured code as craft signal. Borrow the voice/mono split for any docs product.

## 4. Component Stylings

- Search hero ("Search for a library"): white 8px input, 16px left / 40px right padding — the product's front door, designed as furniture.
- Buttons: 6 variants, 8px system — emerald solid, emerald outline, stone fill, ink 6px closer, plus a split-button with asymmetric radii (8-0-0-8 / 0-8-8-0) for mode toggles.
- Links: 7 styles, ALL hovering to deep green `#036546` — the whole site agrees on one hover destination.
- Tables: hairline `#d5d2d0` rules (header/section/table/thead/tr) — plans and docs read as ledger.
- Logo: 116×28 light SVG with 8px safe zone + favicon + og-image.

## 5. Layout Principles

- 8px scale (1/2/4/6/8/10/12/16/20/24/32/40/64/80/128px) with 128px hero air — vast calm over a dense 12–16px docs core.
- Funnel: search hero → library proof → plans → enterprise → about → contact — evaluation-led, search-first.
- 10 breakpoints (1536→600) — unusually granular desktop ladder (1536/1350/1280/1108/1092) plus standard mobile stops.

## 6. Depth & Elevation

- One sm ring-shadow + one xl drop for the hero card — flat ledger with a single lifted object (the search).
- Decision: the search floats, everything else sits — attention architecture for a search product.

## 7. Do's and Don'ts

- Do: AAA stone pairs; emerald large-text-only discipline; single hover color; split-button radii for toggles; ledger tables; 10-step responsive ladder.
- Do: keep emerald off small body text (3.61 fails AA); keep `#a8a29e` decorative.
- Don't: add accent colors (emerald + deep + mint is the budget); don't decorate reading pages; don't slow 0.083–0.3s micro-motion.

## 8. Responsive Behavior

- 10-step ladder (1536→600) — search stays full-width, tables scroll or stack, pills wrap; fast micro-motion keeps mobile snappy.
- Touch: 8px buttons need 44px targets on mobile — verify before borrowing densities.

## 9. Agent Prompt Guide

- Quick reference: `ai / emerald-stone / docs-led / light / medium complexity / dual CTA (search + plans)`.
- Ready-to-use prompt: "Design an AI-docs product page in the Context7 logic: warm stone grounds with AAA ink text, one emerald used only for large text and buttons, deep-green single-destination link hovers, Inter voice plus JetBrains Mono for identifiers, a library-search input as the floating hero object, ledger-style hairline tables, split-buttons with asymmetric radii for mode toggles, flat surfaces with one lifted card, and a 10-step responsive ladder. Convert on accuracy, never on hype."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Library search hero (floating card) — intent capture.
2. Integration proof bands — works-with-my-stack scan.
3. Plans (`/plans`, 20 menus opened) — packaging depth.
4. Enterprise (`/enterprise`, 15/18 WCAG) — procurement trust.
5. About (`/about`) — accuracy-story legitimacy.
6. Contact (`/contact`) — capture close.

### 11. Pattern Position

- Fits the AI-infra pattern: search → prove (integrations) → package (plans) → procure (enterprise). Against Wispr (consumer voice), Sendr (utility), Primora (craft), Context7 is machine-facing — the AI set now covers human and machine audiences.
- Page-flow logic: assume the buyer is an engineer evaluating for an agent pipeline; every band answers "is it current and accurate."

### 12. Synthesis Notes

- Unique (borrow as logic): search-as-floating-hero; single hover color site-wide; emerald large-only discipline; ledger tables as marketing; split-button asymmetric radii; announcement + support framing; 10-step granularity.
- Combine with: SaaS pricing transparency for plans depth and devtool changelog patterns for the freshness proof Context7's funnel implies but doesn't show.
- Avoid: copying stone + emerald + Inter verbatim (reads "Context7 clone"); emerald small text; decorating reading pages; skipping freshness signals — stale docs kill AI-infra trust.
