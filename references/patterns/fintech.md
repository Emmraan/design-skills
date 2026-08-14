# Fintech Pattern

Fintech pages sell **trust before they sell features** — money, risk, and compliance make
buyers cautious. The winning pattern pairs **confidence-inspiring design** (precise,
regulated, bank-like) with **emotional clarity** (what the money does for you). It must feel
institutional *and* human at once.

## When to use

- Banking, payments, investing, insurance, accounting, lending, treasury.
- The product moves or manages money — trust is the primary asset.
- Goal: open account / signup, but with high stakes (they'll be handing over financial data).

## Canonical section order

```
1. Navbar (logo · links · CTA · trust hint: "FDIC insured / SOC 2")
2. Hero — outcome headline + product shot + CTA + trust line
3. Trust band (security, licensing, insurance, compliance) — early and visible
4. Logo cloud (institutions/companies that trust us)
5. Problem → product (what it does for your money)
6. How it works (steps, with the security/controls woven in)
7. Features (bento/grid — money-focused outcomes)
8. Pricing / fees (transparent — a fintech differentiator)
9. Stats (scale: volume, uptime, customers)
10. Testimonials (customer outcomes, matched to persona)
11. FAQ (security, fees, limits, eligibility)
12. CTA band
13. Footer (with full legal/compliance links)
```

## What makes this pattern work

- **Trust is the hero's third element.** A trust line under the CTAs ("FDIC-insured ·
  SOC 2 Type II · 256-bit encryption") is not optional decoration — it answers the first
  objection before it's asked.
- **Precision in copy and numbers.** Exact, concrete language ("0% fee on ACH",
  "3.9% APY") builds credibility; vague marketing language triggers caution.
- **Security as a section, not a footnote.** A dedicated security/compliance band
  (encryption, audits, insurance, who holds the money) near the top earns the right to be
  asked for money later.
- **Transparent pricing/fees is a differentiator** — most competitors hide them. A clear fee
  table or "no hidden fees" pledge converts careful buyers.
- **Calm, ordered visuals** — dense data is organized with a real grid, aligned numbers,
  consistent typography. Sloppy layout = sloppy handling of money.
- **Customer care:** "your money is protected" reassurance (insurance, guarantees, support)
  woven through FAQ and a trust band.

## Design language for fintech

- **Tone:** confident, precise, unshowy. Think banking lobby, not arcade. The UI itself
  should look like it handles money carefully.
- **Palette:** often a dark-primary + one crisp accent (green = growth/money, or a strong
  brand hue). Tinted neutrals; never gimmicky gradients. (See `color-systems.md`.)
- **Type:** a trustworthy pairing — geometric sans display + humanist body; tabular figures
  (`font-variant-numeric: tabular-nums`) for all money/number columns so digits align.
  Mono for codes/addresses (see `typography-systems.md`).
- **Data display:** real financial charts/tables with crisp alignment — this is where
  fintech earns its visual credibility.
- **Motion:** restrained. Subtle micro-interactions; no flashy entrances. Financial UI
  should feel deterministic, not playful.

## Differentiation moves

1. **Lead with the human outcome** — "Your money moves at 10am, not 3 days" — while
   competitors lead with feature lists.
2. **Make fees/pricing radical transparency** — a fee table with "0%" prominently.
3. **Editorial/premium calm** — a light, serif-accented fintech reads distinct from the
   dark-navy norm.
4. **Interactive money visualizer** — a live savings/trade calculator or a balance demo in
   the hero.
5. **A bold, unexpected accent** (energetic green, warm orange) against an otherwise
   institutional palette.

## Compliance, security & accessibility

- **Licensing/insurance mentions must be accurate** — never fabricate "FDIC-insured",
  "regulated by X", or "SEC-registered". This is a legal risk; state only what is true.
- **Security section:** encryption, data storage location, compliance certifications,
  incident policy. Point to the real security page.
- **Accessibility is trust:** financial numbers are text (never images of digits), charts
  have text fallbacks, tables have proper headers, contrast AA (see `accessibility/`).
- **Forms** (signup/onboarding) follow the strictest `forms.md` — correct input types,
  autocomplete, inline errors; no data loss on error.

## Responsive

- Charts/stat tables need horizontal-safety or simplification at mobile — never truncate the
  numbers.
- Trust band and fee tables stay legible (tables can become cards with header labels).
- CTA and trust line stack cleanly; onboarding CTAs remain thumb-reachable.

## Anti-patterns (never copy)

- Cryptocurrency-coin-purple + rockets + "to the moon" — a different (and riskier) register.
- Fake compliance claims or implied regulation — legal exposure.
- Hidden fees, then a "see fine print" link.
- Dense text walls with no visual order (looks like it can't organize data).
- Money values rendered as images or with mismatched alignments.
- Playful, bouncy motion in a financial product — undermines the precision the page claims.