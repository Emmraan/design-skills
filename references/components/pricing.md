# Pricing

Pricing is the highest-stakes section: users arrive skeptical and ready to compare. It must
make the **decision obvious** in seconds and justify the price with confidence, not
apology.

## The job (what it must do)

1. **Show the decision clearly** — plans, prices, and what you get at a glance.
2. **Make the "right" plan obvious** — most users should land on your target plan without
   thinking (usually highlighted).
3. **Remove fear** — trial, no-credit-card, cancel-anytime signals directly under the CTAs.
4. **Fit the pricing model** — usage-based, seats, flat tiers, or custom, presented honestly.

## Structure (the canonical pattern)

```
Headline + billing toggle (Monthly/Annual)        ← set expectations
┌──────────┐  ┌─────────────┐  ┌──────────┐
│ Starter   │  │ Pro ★       │  │ Enterprise │
│ $9/mo     │  │ $29/mo      │  │ Custom     │
│ feature   │  │ feature     │  │ feature    │
│ list      │  │ list        │  │ "Contact"  │
│ [Start]   │  │ [Start]     │  │ [Contact]  │
└──────────┘  └─────────────┘  └──────────┘
        "Everything in Starter, plus…"
```

- **3 plans** is the comfortable default (2 feels thin, 4+ splits attention).
- **Highlight the middle** ("Most popular") with scale + accent edge + a slightly larger
  presence. It's your target plan.
- **Enterprise/custom** gets its own card with "Contact sales" — never pretend a price.
- **Billing toggle** (monthly/annual): annual highlighted ("save 20%"), and the toggle is a
  real, working control with the savings badge attached.

## Feature lists

- Group bullets: **"Everything in Starter, plus…"** laddering builds upgrade desire. Avoid
  repeating the full list per plan.
- Each bullet = concrete outcome or feature name users recognize. Avoid vague rows
  ("Advanced features").
- Include honest limits: "3 seats", "10,000 rows/mo" — users trust you for stating them.
- Checkmarks (✓) are fine and standard; keep them consistent and high-contrast.

## Design decision logic

- **Price typography:** the price is the loudest text in the card — large (display-ish),
  right-aligned to the "/mo" unit. Show the effective annual price subtly under the monthly
  number when annual is discounted.
- **Card surface:** the highlighted card breaks the pattern (different background, accent
  border/shadow, or slight lift). Everything else stays quiet so the star stands out.
- **CTA:** one primary CTA per card (accent). Non-highlighted cards get secondary/gradient
  CTAs of lower visual weight. "Start free" = lower commitment phrasing than "Buy now".
- **Guarantee strip** below the grid: "7-day free trial · No credit card · Cancel anytime"
  — small, single line, high trust value.

## Responsive

- Cards stack full-width on mobile; the highlighted card goes **first or second**, never last
  (users see the middle plan last on a stack → reorder).
- Toggle and price scale with `clamp()`; the grid gap compresses before text shrinks.

## Accessibility

- The highlighted plan is **not** communicated by color alone — add a visible label/badge
  ("Most popular") with text (see `a11y-checklist.md`).
- Real tables or proper list markup; `<button>` (not `<div>`) for the billing toggle with
  `aria-pressed`.
- Contrast on the accent card and its text — a dark plan card needs light text at AA.

## Anti-patterns (never copy)

- Prices that need JS to render (no-JS users see nothing).
- 5+ plans or a scrollable pricing row.
- The "Most popular" plan is the cheapest one (you're telling users to pay less).
- Hidden pricing entirely ("Contact us" for everything) with no entry point.
- Annual/monthly toggle that's fake or changes the feature set (not just price).
- Cards of equal weight — nobody knows which to pick.