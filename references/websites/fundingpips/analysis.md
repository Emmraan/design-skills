# FundingPips — Design Analysis

> Source: `https://fundingpips.com/` · Baseline: `baseline.json` · Collected: 2026-09-11 (Dembrandt 0.32.2, 5 pages)
> FundingPips is a prop-trading firm (buy a challenge, pass phases, get funded,
> earn rewards). The design is **trading-floor confidence in a tailored suit**:
> deep navy authority, royal-blue actions with electric glow, giant DM Sans numbers
> that shout upside, and Inter body copy that reads the fine print for you.
> Every pixel funnels to "Buy Challenge".

## 1. Visual Theme & Atmosphere

- **Institutional adrenaline.** Light pages (`#FCFCFC`) with navy ink (18.37:1 AAA)
  alternate with deep-navy bands (`#020A25`, pale blue on top at 14.94 AAA) — trust
  documents by day, trading terminal by night.
- **Numbers as heroes:** DM Sans display up to 221px, semibold-bold, tight leading —
  payouts, account sizes, and phase stats ARE the visual design. The product's math
  is the marketing.
- **Glow means live:** brand-blue outer glows on key CTAs/cards feel electric, like
  a terminal that's on and watching — energy without animation spam.
- Mood: ambitious, precise, lucrative — a firm that takes your trading seriously
  because its money is on the line too.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Authority | deep navy `#00225A` | Headers, dark fills, body on light (15.26:1 on white, AAA); the institution |
| Action | royal blue `#2C44D1` | Primary CTAs (white on it AAA); the only color that sells |
| Terminal | near-black navy `#020A25` | Dark bands (pale blue `#DBE0F8` on it 14.94:1, AAA); night-trading gravity |
| Ink | `#111114` | Body on light (18.37:1, AAA); the fine print, readable |
| Surface | pale blue-gray `#F3F5FA` | Cards, labs backgrounds — cool paper for data |
| Surface-2 | pale blue `#DBE0F8` | Tints, highlights on dark |
| Profit | green `#219653` | Success/payout semantics only — money-good, never decoration |
| Secondary light | `#9AA0B9` / `#A5AAC3` | Meta on dark (7.5–8.5:1, AAA) — the safe grays |
| Large-only traps | `#6A7280` on dark (4.04), `#7B8DAA` on light (3.17) | Large text only — never body |
| Fails (avoid) | `#6A6C6E` on `#2B2D31` (2.62), white on `#FCFCFC` (1.03) | Baked-in source failures — animation/disabled states, not copyable patterns |

- **Two blues, two jobs:** navy authorizes (backgrounds, headlines), royal converts
  (buttons, glows). Never swap them — authority doesn't shout, action doesn't mumble.
- **Green is earned:** the profit green appears only where money-good news lives
  (payouts, rewards) — semantic color with a contract.

## 3. Typography Rules

- **Two-family workhorse split:** DM Sans for display/statements (221→16px, 400–800 —
  the voice of upside), Inter for body/UI (72→8px, 400–700 at roomy `1.5–1.63`
  leading — the voice of terms). Display excites, body reassures.
- **Display ladder:** 221/150px hero statements → 92/90/80px section claims → 50–28px
  card/feature heads → 20–12px labels. Tight `1.0–1.14` leading up top — numbers
  stack like a leaderboard.
- **Body for terms:** Inter 18/16/15/14px at 1.5+ leading carries objectives, rules,
  FAQs — a trading firm's fine print must be genuinely readable, and it is.
- **Hierarchy:** size + weight both work hard (400→800 display range); tabular
  figures implied for stats/pricing — sloppy numbers would read as sloppy money.

## 4. Component Stylings

- **Primary button:** royal-blue fill (`#2C44D1`), white 14px/500 text, sharp `6px`
  radius, `1px` lighter-blue border, subtle white inset top-highlight ("Buy
  Challenge", 5 uses). Precision instrument, not pillow — 6px says fintech.
- **Navy button:** deep-navy fill, white text, `8px` radius, roomy `0×40` padding
  ("Buy Evaluation") — the institutional sibling for the flagship action.
- **Outline button:** transparent, navy text, hairline navy-20% border, 8px radius
  ("Free Trial") — risk-reversal CTA, visually quieter than the paid actions.
- **Pill toggles:** white/navy 14–18px pills ("Phases", dual "Buy Challenge" pills)
  for phase selectors and compact placements — pills navigate, rectangles convert.
- **Inputs:** white fill, hairline border, `8px` radius, navy text — quiet boxes that
  let the CTAs dominate.
- **Glow system:** brand-blue outer glows (`16px/8px` at 45%, `37px` insets) on
  hero/action elements — the signature: electricity as elevation.

## 5. Layout Principles

- **Spacing scale:** 8px base with fine steps (1/2/3/3.5/4/6/8/10px) — dense,
  data-forward rhythm; a trading dashboard's density applied to marketing.
- **Section rhythm:** nav (logo + links + Buy Challenge) → giant-number hero →
  challenge pricing → phases/objectives → rewards/payouts → labs → blog → footer.
  Every band answers one trader question: how much, what rules, what do I get.
- **Funnel discipline:** "Buy Challenge" (5 placements) + "Buy Evaluation" (3) +
  one "Free Trial" risk-reversal — three actions, one hierarchy, repeated until
  conversion.
- **Light/dark pacing:** light proof pages alternate with terminal-dark excitement
  bands — documents by day, terminal by night.

## 6. Depth & Elevation

- **Glow, not shadow:** brand-blue outer + inset glows electrify CTAs and hero cards
  — elevation in the brand hue, visible on both light and dark. Neutral shadows are
  nearly absent (one soft low-opacity use).
- **Inset highlights:** white 12% top-inset on primary buttons gives a lit-from-above
  finish — tactile precision on a 6px radius.
- **Motion system:** full easing vocabulary — `0.15/0.2/0.3s` with
  `cubic-bezier(0.4,0,0.2,1)` (805 uses) for UI response; a 7.6s linear
  `labs-hero-train-run` animation (84 uses) as the showpiece — deterministic UI,
  one cinematic moment. Financial UI feels instant, not playful.

## 7. Do's and Don'ts

- **Do:** navy-authority + royal-action role split; giant DM Sans numbers for upside;
  Inter roomy body for terms; 6–8px fintech radii (pills only for toggles);
  brand-blue glow elevation; green reserved for profit semantics; AAA body contrast
  both themes.
- **Don't:** use `#6A7280`-on-dark or `#7B8DAA`-on-light for body (large-only);
  copy the white-on-`#FCFCFC` or `#6A6C6E`-on-`#2B2D31` failures; round primary CTAs
  into pills (sharp = precise); let green decorate — it must mean money-good;
  animate UI beyond 0.3s ease (one showpiece animation per page max).

## 8. Responsive Behavior

- No explicit breakpoints captured (fluid Next.js build) — giant DM Sans display
  scales fluidly; 6–8px CTA radii and glow system hold at small widths; dense
  data bands stack.
- Sticky "Buy Challenge" survives header collapse; phase pills stay tappable;
  pricing/objective tables linearize without losing hierarchy.
- Dark terminal bands keep pale-blue AAA at all widths; glows stay subtle on mobile
  (no heavy blurs observed).

## 9. Agent Prompt Guide

> Build a landing page with a **prop-trading fintech aesthetic**: light paper
> (`#FCFCFC`) with near-black ink (AAA 18:1) alternating with terminal-navy bands
> (`#020A25`, pale blue text AAA). Deep navy (`#00225A`) for authority, royal blue
> (`#2C44D1`) for every converting action, profit green (`#219653`) only for
> money-good semantics. DM Sans display (221→28px, 600–800, tight 1.0–1.14) for
> upside numbers; Inter body (18→14px, 1.5+ leading) for terms. Sharp 6–8px CTA
> radii — royal primary with inset highlight, navy flagship, hairline outline for
> risk-reversal; pills reserved for toggles. Brand-blue glow elevation, instant
> 0.15–0.3s easing, one cinematic animation max. Tone: ambitious, precise,
> lucrative — trading-floor confidence in a tailored suit.

## 10. Component Map

1. Header — logo left, challenge/objectives/rewards nav, royal "Buy Challenge" pill-button right.
2. Hero — giant DM Sans number-claim (221px) + primary CTA over light or terminal-dark.
3. Challenge pricing — account-size cards with stats + Buy Evaluation/Challenge CTAs.
4. Phases band — pill toggles + trading-objectives rules in readable Inter body.
5. Rewards band — payout proof with profit-green semantics.
6. Labs band — cinematic animated showpiece (train-run) for brand energy.
7. Blog + footer — trust depth and closure.

## 11. Pattern Position

Best fits a **fintech landing** (extends `patterns/fintech.md` + the repo's fintech
collection): trust hero → transparent pricing → rules/objectives → payout proof →
risk-reversal (free trial) → footer. Against Ramp (institutional restraint) it adds
high-energy conversion mechanics — the genre markers to codify are giant-number
heroes, phase/objective transparency bands, and glow CTA systems.

## 12. Synthesis Notes

- **Unique:** numbers-as-design (display sizes ARE the pitch); navy/royal role split;
  brand-blue glow as elevation language; pill-toggles vs rectangle-converters
  discipline; labs showpiece animation inside a deterministic UI; green-with-a-
  contract semantics.
- **Combine with:** Ramp's institutional restraint for trust bands; Linear's dark
  precision for terminal sections; Udemy's fixed-hierarchy cards if challenges need
  listing at scale; Ghost's editorial calm for blog/education content.
- **Weaknesses / avoid:** several contrast failures baked into states/disabled roles —
  audit, don't copy; giant numbers need real figures — placeholder stats look scammy
  in this genre; the navy + royal-glow look is strongly "FundingPips" — lift the
  *system* (role-split blues, number heroes, glow elevation) with different hues,
  never the exact palette; compliance claims must stay true (per fintech collection
  rule).
