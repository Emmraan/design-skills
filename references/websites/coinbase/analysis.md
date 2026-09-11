# Coinbase — Design Analysis

> Source: `https://www.coinbase.com/en-gb` · Baseline: `baseline.json` · Collected: 2026-09-11 (Dembrandt 0.32.2, 5 pages)
> Coinbase is the blue-chip crypto exchange (spot, derivatives, regional FCA info).
> The design is **a bank that learned product design**: institutional blue trust,
> a fully custom type system (Display/Sans/Text + Icons), one 56px pill button
> shape for every action, and soft layered shadows instead of crypto-neon noise.
> It converts skeptics, not degens.

## 1. Visual Theme & Atmosphere

- **Blue-chip calm.** White canvas, near-black ink (19.69:1 AAA), one royal blue
  (`#0052FF`) for all actions — the page feels like a bank branch redesigned by a
  product team: regulated, legible, quietly confident.
- **Dark bands for markets:** `#141519`/`#282B31` sections carry market/derivatives
  content (white on them 14–18:1 AAA) — trading lives in the dark, onboarding in
  the light.
- **Custom type as moat:** four proprietary families (Display/Sans/Text/Icons) —
  no Google font could say "we're the standard"; the voice is owned end to end.
- Mood: trustworthy, precise, mainstream — crypto with the edges filed off, on purpose.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Action | royal blue `#0052FF` | Every primary CTA (white on it 5.75:1, AA); the only color that converts |
| Action-light | sky `#578BFA` | Blue voice on dark bands (6+:1, AA); links/accents where royal would sink |
| Link | `#0667D0` | Text links (underline on hover); information, not conversion |
| Ink | near-black `#0A0B0D` | Headlines + body (19.69:1 on white, 17.25 on `#EEF0F3` — AAA); the voice |
| Secondary | slate `#5B616E` | Meta on light (5.44–6.21:1, AA); descriptions, captions |
| Surface | `#EEF0F3` | Light bands, icon-button fills; cool paper |
| Night | `#141519` / `#282B31` | Dark market bands (white 14–18:1, AAA) |
| Profit | green `#27AD75` | Positive market semantics on dark (6.86:1) — money-good, never decoration |
| Large-only trap | `#8A919E` on dark (4.48, 178 uses) | Large text only — never body |
| Fails (avoid) | ink-on-`#282B31` (1.39), white-on-`#EEF0F3` (1.14) | Disabled/hidden-state artifacts — never copyable patterns |

- **One blue converts, one blue informs:** `#0052FF` fills buttons; `#0667D0`
  underlines links. Flat fills for action, underline-shift for information.
- **Light handling:** light-first onboarding, dark market bands — trust in the
  light, trading in the dark.

## 3. Typography Rules

- **Four-family owned system:** CoinbaseDisplay for statements (80/64/52/44px,
  weight 400 — size-only hierarchy, tight `1.0–1.09`); CoinbaseSans for UI/labels
  (36→12px, 400–700); CoinbaseText for reading body (18/16/13px at `1.5–1.56`);
  CoinbaseIcons as a full icon font (64→16px glyphs incl. circular icon-buttons).
- **Display restraint:** 80px max, weight 400, leading 1.0 — confidence through
  scale and lettershapes, not boldness. A bank doesn't shout.
- **Body for compliance:** Text 18/16px at 1.5+ carries risk disclosures and FCA
  info — regulated copy must be genuinely readable, and it is.
- **Hierarchy:** Display size steps → Sans 20/18/600 subheads → Text body →
  14/13px labels/meta. Weight used sparingly (600 CTA/labels, 700 rarely).

## 4. Component Stylings

- **One pill for everything:** ALL buttons are `56px` pills, 16px/600 text —
  blue-filled "Sign up" (`0×24`), white "Learn more" (`16×32`), ink "See more
  assets" (`16×32`), sky-blue "Sign up" variant on dark. Same shape, four contexts —
  the **mono-shape CTA system** is the signature: users learn one shape, trust it
  everywhere.
- **Icon circle buttons:** gray/dark filled circles with Icons-font glyphs —
  compact actions (close, social, app) that rhyme with the pill geometry.
- **Links:** colored, no underline by default, underline + shift to `#3860BE` on
  hover — feedback is explicit (regulation likes explicit).
- **Inputs:** email-style signup fields pair with the blue pill — conversion unit
  is field + pill, always adjacent.
- **Cards:** soft layered shadows (`8px/12px` at 12%, `18px` ambient) lift market
  modules — depth through light, never borders or glows.

## 5. Layout Principles

- **Spacing scale:** 8px base with fine steps (1/3/4/5/6/8/10/12px) — dense,
  product-led rhythm; marketing breathes, market data packs tight.
- **Section rhythm:** nav (logo + markets links + blue Sign up) → statement hero +
  signup field → asset/market bands → derivatives dark bands → trust/compliance
  (FCA info) → footer. Every band answers one skeptic question: what, is it safe,
  how do I start.
- **Compliance as design:** FCA-info and regional pages are first-class sections,
  not footer links — regulation is a trust feature, displayed not buried.
- **Light/dark pacing:** light onboarding alternates with dark market bands —
  safety in the light, action in the dark.

## 6. Depth & Elevation

- **Soft light shadows:** layered neutrals (`8/12`, ambient `18px`, hairline grays)
  — cards float like paper on a desk. No brand-color glows (unlike FundingPips):
  elevation is neutral because the brand speaks through blue fills, not light.
- **No gradients observed** — flat fills + shadow do all depth work; restraint reads
  as solvency.
- **Motion discipline:** `0.2/0.3s ease-in-out` (586 uses) — link/card background
  shifts, button opacity via custom bezier. Everything acknowledges, nothing
  performs; financial UI must feel deterministic.

## 7. Do's and Don'ts

- **Do:** one blue for all conversion; mono-shape 56px pill CTAs; owned/custom type
  (or a strict Display/Sans/Text role split); light-onboard/dark-trade pacing;
  compliance as visible trust bands; AAA body contrast; neutral shadow elevation.
- **Don't:** set body in `#8A919E`-on-dark (4.48, large-only); copy the dark-on-dark
  or white-on-light artifacts; add a second acting color beside blue; neon-glow
  crypto clichés (this system's whole edge is NOT looking like crypto); bury risk
  disclosures — legibility is the conversion strategy.

## 8. Responsive Behavior

- Full ladder (400 → 426 → 500–600 → 640 → 768/767 → 896 → 1280/1279 → 1440 →
  1600) — 80px display scales down, 56px pills keep geometry and 16px/600 text at
  thumb sizes; market data bands stack into cards.
- Header collapses to logo + menu; blue Sign up survives as the sticky action.
- Dark bands keep white AAA at all widths; signup field + pill stay adjacent (the
  conversion unit never breaks).

## 9. Agent Prompt Guide

> Build a landing page with a **blue-chip crypto aesthetic**: white canvas,
> near-black ink (AAA 19:1), royal blue (`#0052FF`) for every converting action,
> sky blue (`#578BFA`) for the blue voice on dark, slate (`#5B616E`) AA meta,
> profit green only for money-good semantics. Owned-feel type split: display
> (80→44px, weight 400, tight leading) for statements, sans UI (36→12px) for
> labels, text family (18/16px, 1.5+) for reading body, icon font for glyphs.
> Mono-shape 56px pill CTAs — blue primary, white/ink secondaries, sky variant on
> dark; links underline on hover. Soft neutral layered shadows, zero gradients.
> 0.2–0.3s ease-in-out acknowledgement motion. Compliance content as visible trust
> bands. Tone: trustworthy, precise, mainstream — a bank that learned product design.

## 10. Component Map

1. Header — logo left, market/product links, blue pill "Sign up" right.
2. Hero — 80px display statement + email field + blue pill conversion unit.
3. Asset bands — market listings with profit-green semantics.
4. Derivatives dark bands — trading content on night surfaces.
5. Trust/compliance band — FCA/regional info as first-class sections.
6. Learn band — white "Learn more" pill education path.
7. Footer — dark, dense, regulatory closure.

## 11. Pattern Position

Best fits a **crypto landing** (no `crypto` pattern file exists yet — this analysis
is the seed): statement hero + conversion unit → markets proof → dark trading
bands → compliance trust → footer. It borrows the SaaS skeleton and fintech trust
mechanics (front-loaded trust, transparent product) but replaces institutional
stiffness with product-led warmth — the genre markers to codify are the field +
pill conversion unit and compliance-as-design.

## 12. Synthesis Notes

- **Unique:** mono-shape CTA system (one 56px pill, four contexts); four-family
  owned type with an icon font; field + pill conversion unit; compliance-as-design
  trust bands; neutral-shadow (not glow) elevation as anti-crypto positioning.
- **Combine with:** FundingPips' number-hero energy for upside moments (kept blue,
  never neon); Ramp's institutional restraint for trust bands; Udemy's fixed-
  hierarchy cards for asset listings; Ghost's editorial calm for Learn content.
- **Weaknesses / avoid:** white-on-blue is AA (5.75) not AAA — fine for large CTA
  text, don't set small blue-button labels; several low-contrast artifacts baked
  into states — audit, don't copy; the blue-pill-on-white look is strongly
  "Coinbase" — lift the *system* (mono-shape CTAs, conversion unit, compliance
  bands) with a different hue, never the exact blue + pill combo.
