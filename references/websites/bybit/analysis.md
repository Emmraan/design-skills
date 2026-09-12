# Bybit — Design Analysis

> Source: `https://www.bybit.com/en/` (crypto derivatives exchange) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/en/`, `/en/p2p/buy/USDT/INR`, `/en/copyTrade/`, `/en/tradingbot`, `/en/cards/`)

Bybit is the trader-pro pole of crypto: near-black terminal grounds, orange sign-up pills, green/red market semantics, tabular numerals, and a Radix/shadcn component engine. Where Coinbase reassures and Phantom befriends, Bybit equips — density is a feature for its audience.

## 1. Visual Theme & Atmosphere

- Mood: trading floor at night — black `#000000` grounds, glowing orange CTAs, green/red market pulses, breathing hero accents.
- Philosophy: pro-density with guardrails — Inter at 6 weights with `tnum` tabular figures, 45 breakpoints, and AA-or-better on every functional pair.
- Stack honesty: Tailwind arbitrary values + 16 Radix primitives + shadcn patterns + 8 Headless UI components — the tokens read like a component library because they are one.

## 2. Color Palette & Roles

- Grounds: black `#000000` + ink `#121214`/`#16171A`/`#17181E` (white-on-dark 17.7–21 AAA across all five pages).
- Brand: yellow `#FFB11A` (`--brand-color`) + orange CTA `#FF9C2E` (black text, 100/200px pills) darkening to `#F17402` on hover; awakened/hover/tap gold ramps (`#FAC967`/`#F9B732`/`#CF8A00`).
- Market semantics: greens `#06C167`/`#1E9254`/`#4FBE83` (buy/long) vs reds `#F63649`/`#BC3536`/`#E66566` (sell/short), with 12%-alpha tinted badges (3.5px radius, 12px/500) — the only place small colored text is allowed, sized and weighted deliberately.
- Neutrals: `#7F838A`/`#71757A` (large-only ~3.8 on light/dark), `#ADB1B8`/`#A1A5AB` disabled (2.15–2.47 fail — visibly disabled by design), hairlines `#D5DAE0`/`#DDE1E5`/`#F3F5F7`.
- Known fails: near-black-on-black 1.03–1.15 (decorative depth), disabled greys — both intentional non-text states.

## 3. Typography Rules

- Inter 300–1000 (54px H2 → 10px captions) with `tnum` tabular numerals — prices, PnL, and order books align; IBM Plex Sans 600 for select figures; PingFang SC for CJK; Arial for legacy UI.
- Logic: weight encodes conviction (800–1000 for hero/figures, 500–600 for UI, 300 for airy subheads). No display serif, no playfulness — numbers are the brand.
- Decision: tabular numerals + extreme weight range is the trading signal. Borrow for any data-dense product.

## 4. Component Stylings

- CTAs: orange pills (100/200px, 11–14×24px, black text) + green pills + orange-outline ghosts + white bordered secondary — conversion hierarchy in four fills.
- Badges: 12%-tint green/red pills for market states; orange 12%-tint for promos.
- Cards: 8/12/16px with `#DDE1E5` hairlines; 50%/100% round media controls; 3–7px utility radii; inset white glows (0.1–0.15, 50px) for premium panels.
- Inputs: dark pills (`rgba(16,15,15,.5)`, 100px, 14×24px, white text) with brand-color focus rings (Tailwind ring tokens) — terminal-native forms.
- Links: orange/white/grey default → `#F17402` hover; 7 styles across marketing and app chrome.
- Overlays: Radix-driven (arrowShow/contentShow/overlayShow keyframes) + 60s security-notice marquee — compliance as ambient motion.

## 5. Layout Principles

- 8px scale (1/2/4/5/8/9/10/11/12/14/16/20/22/24/32px) across five product verticals (spot, P2P, copy trading, bots, cards).
- Product-funnel flow: hero with breathing accents → market proof (tickers, volumes) → vertical deep-dives (P2P/copy/bots/cards) → orange sign-up conversion → compliance footer.
- Five linear gradient families stage heroes and cards; inset shadows give panels their glow.

## 6. Depth & Elevation

- Inset-glow system (white 0.1–0.15 inset 50px) + faint ink lifts (0.1, 4–24px) + gradient staging. Panels glow from within rather than floating — terminal aesthetics.
- Decision: glow-not-lift reads "powered on" — appropriate for always-live markets.

## 7. Do's and Don'ts

- Do: AAA white-on-dark pairs; orange pills with black text; green/red market semantics with tinted badges; `tnum` figures; brand-color focus rings; breathing hero motion.
- Do: keep small colored text inside 12%-tint badges at 500+ weight; keep disabled states visibly failing.
- Don't: lighten into fintech-friendly territory (dark is the pro signal); don't set small text in mid-greys (they fail); don't add serif/display type — numbers only.

## 8. Responsive Behavior

- 45-breakpoint ladder (1800→98px) — terminal grids collapse to stacked cards; pills stay tappable; P2P/copy/bot pages reflow independently per vertical.
- Touch: 100px+ pills and full-width dark inputs are thumb-first; overlays become bottom sheets.

## 9. Agent Prompt Guide

- Quick reference: `crypto / pro-trading-dark / product-grid-funnel / dark / high complexity / single CTA (Sign up)`.
- Ready-to-use prompt: "Design a pro-trading crypto page in the Bybit logic: near-black grounds with AAA white text, orange pill CTAs with black text, green/red market semantics with tinted badges, Inter at full weight range with tabular numerals, dark pill inputs with brand focus rings, inset-glow panels and gradient-staged heroes, material-ease micro-motion with breathing accents and a compliance marquee, and a 45-step responsive ladder. Density is a feature — never lighten into friendly fintech."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Breathing hero (orange sign-up pill + market proof) — power-on first impression.
2. Ticker/market bands — live-data credibility.
3. P2P (`/en/p2p/buy/USDT/INR`) — fiat on-ramp, INR-localized.
4. Copy trading — social proof as product.
5. Trading bots — automation upsell.
6. Cards (`/en/cards/`) — off-ramp to daily life.
7. Compliance marquee + footer — regulation as ambience.

### 11. Pattern Position

- Fits the pro-trading pattern: power (hero) → proof (markets) → verticals (P2P/copy/bots/cards) → convert (sign-up). Against Coinbase (first-trade simplicity) and Phantom (self-custody warmth), Bybit owns active-trader depth — the trio now spans every crypto user type: newcomer, holder, trader.
- Page-flow logic: assume the visitor already trades somewhere; win on instruments, liquidity signals, and fee clarity.

### 12. Synthesis Notes

- Unique (borrow as logic): market-semantic color system with tinted-badge small text; `tnum` tabular discipline; inset-glow terminal elevation; compliance marquee; vertical-per-page product funnels; INR-localized P2P proof.
- Combine with: Coinbase's compliance-as-design rigor (Bybit brings depth, Coinbase brings trust paperwork) and FundingPips' number-hero energy (both speak trader — cross-pollinate adrenaline with discipline).
- Avoid: copying black/orange/green-red verbatim (instant exchange clone); lightening the theme; small mid-grey text; hiding fees or risks — pro audiences punish opacity.
