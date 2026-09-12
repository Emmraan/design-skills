# Phantom — Design Analysis

> Source: `https://phantom.com/` (Solana/multichain self-custody wallet) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/about`, `/explore`, `/download`, `/security`)

Phantom makes self-custody feel safe for normals: cream grounds, grape ink, lilac pills, mint trust badges, and the loudest focus rings in the repo. Against Coinbase's institutional blue, Phantom is crypto's friendly face — warmth as a security strategy.

## 1. Visual Theme & Atmosphere

- Mood: cozy onboarding — cream `#FFFDF8` (page + manifest), lavender washes, rounded everything, ghost mascots implied by curves.
- Philosophy: fear-removal — every scary crypto concept (keys, chains, swaps) arrives inside a soft pill with a mint badge nearby.
- Light-only; friendliness is structural, not a skin.

## 2. Color Palette & Roles

- Grounds: cream `#FFFDF8` + lavender `#F5F2FF` + `#E2DFFE` washes + near-white `#FDFCFE`/`#F4F2F4`.
- Ink: grape `#3C315B` (11.78 on white, 11.52/10.58 on near-whites, 9.1 on `#E2DFFE` — all AAA).
- CTA: lilac `#AB9FF2` fills with grape text (5.03 AA on hover/focus states); blue `#4A87F2` secondary (3.42 large-only on cream — keep large).
- Trust: mint `#2EC08B` round badges + `#32AE88` borders; hairlines `#E9E8EA`.
- Neutrals: `#86848D` (3.31 large-only), `#B4B4B4`, `#707070` input borders, `#BBBBBB` ghost borders.
- Loudest focus in repo: cyan `#1EAE DB` wash + 4px orange `#FF7243` outline on every input — unmissable by design.
- Known fails: cream-on-white 1.02, disabled cream pairs — decorative washes only.

## 3. Typography Rules

- Custom "Phantom" face (Inter-derived woff, weights 350/600/700): 96/64px display → 40/36/32 → 24/20 → 16/15/14 UI → 13/12 links.
- Logic: light-350 large statements, 600–700 for CTAs and figures. Friendly geometry at huge sizes reads approachable, not intimidating.
- Decision: proprietary-feeling type from an Inter base — borrow the tactic (custom cut of a neutral grotesk) for ownable-but-legible voices.

## 4. Component Stylings

- CTAs: lilac 32px pills (16×32px, grape text) + 96px ghost pills (32px padding); transform-lift hovers ("Download" floats) with expo easing.
- Badges: 50% round mint pills (15px) — security/chain markers as candy.
- Cards: 8/12/16/24/28/48px radii with 2px ink borders (`#0F0F0F`/`#1C1C1C`) — neo-brutalist outlines softened by cream and curves; colored borders (lilac/mint/cornflower) code categories.
- Inputs: email/search with cyan+orange focus treatment; `#707070` rest borders.
- Links: 4 styles, all → cornflower `#3860BE` + underline on hover (fourth site with this convention — it is a web-wide trust pattern).
- Logo: inline SVG ghost-mark in grape, 152×30, full PWA set.

## 5. Layout Principles

- 8px scale with section jumps (1/3/4/5/6/8/10/12/16/20/24/32/48/96/128px) — airy 96–128px bands around a compact 4–16px component core.
- Funnel: hero reassurance → chains/features → explore ecosystem → download (platform pills) → security proof → about. Download is the only conversion.
- Tinted shadows (lavender/ink glow, 0–4px) instead of black lifts — elevation in brand colors.

## 6. Depth & Elevation

- Five tinted shadows + zero gradients. Cards outlined in ink float on cream with lavender glows — sticker-book depth.
- Decision: colored elevation keeps the friendly register where black shadows would read "serious fintech".

## 7. Do's and Don'ts

- Do: AAA grape/cream pairs; lilac pills + mint badges; ink-outlined cards; loud focus rings; expo-ease lift hovers.
- Do: keep blue `#4A87F2` and grey `#86848D` to large/bold uses (both fail small text).
- Don't: darken into Coinbase-institutional territory (friendliness is the moat); don't shrink display type (96px welcome is load-bearing); don't mute the focus rings.

## 8. Responsive Behavior

- 20-breakpoint ladder (1536→400px) — display type steps down, pills stack full-width, cards single-column; download pills stay tappable.
- Touch: 32px pills and round badges are thumb-first; transform hovers degrade gracefully to taps.

## 9. Agent Prompt Guide

- Quick reference: `crypto / friendly-crypto / download-led / light / medium complexity / single CTA (Download)`.
- Ready-to-use prompt: "Design a friendly crypto-wallet page in the Phantom logic: cream grounds with grape AAA ink, lilac pill CTAs and mint trust badges, ink-outlined cards with tinted lavender glows, custom-feel grotesk at huge friendly sizes, cyan-and-orange unmissable focus rings, expo-ease lift hovers, airy 96px section bands, and a 20-step responsive ladder. Warmth is the security strategy — never darken into institutional fintech."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Reassurance hero (96px welcome + lilac Download pill) — fear-removal first.
2. Chain/feature bands (badged cards) — capability without jargon.
3. Explore ecosystem — network effects as content.
4. Download matrix (platform pills) — single conversion, every OS.
5. Security proof — audits and self-custody explained kindly.
6. About — team humanity behind the ghost.

### 11. Pattern Position

- Fits the wallet-funnel pattern: reassure → show (chains) → prove (security) → install (download). Against Coinbase (exchange-institutional), Phantom owns self-custody-friendliness — the pair now covers custodial and non-custodial crypto UX.
- Page-flow logic: assume the visitor is scared of losing keys; answer that fear in the first viewport, explain features second.

### 12. Synthesis Notes

- Unique (borrow as logic): warmth-as-security (cream/grape/lilac/mint emotional stack); loudest focus rings observed; tinted-glow elevation; expo-ease lift CTAs; ink-outlined friendly cards; proprietary-cut typeface tactic.
- Combine with: Coinbase's institutional proof patterns (Phantom brings warmth, Coinbase brings weight — together they define crypto's full register) and fintech onboarding clarity for seed-phrase flows.
- Avoid: copying cream/grape/lilac verbatim (instant clone); small blue/grey text; black shadows or gradients that institutionalize the warmth; hiding the download CTA behind learn-more detours.
