# SaaS Landing Pattern

The SaaS landing page is the most competitive page in web design — thousands of companies
sell software to the same buyers. The pattern that wins **explains value in seconds, proves
it with product, and removes every reason to say no** — all without looking like the 1,000
other SaaS pages in the same template.

## When to use

- A software product sold by subscription (B2B or prosumer).
- One primary "aha" — a job done faster, easier, or cheaper.
- Goal: trial / demo signup → activate.

## Canonical section order

```
1. Navbar (logo · links · CTA)
2. Hero (headline + product shot + CTA)
3. Logo cloud (proof of adoption)
4. Problem → how it works (1-3 steps)
5. Features (bento/grid or anchor feature)
6. Product deep-dive (the "aha" demo section)
7. Stats / outcomes (proof)
8. Testimonials (voices, ideally matched to buyer)
9. Pricing (3 plans, middle highlighted)
10. FAQ (objections)
11. CTA band (promise + one action)
12. Footer
```

This order is a **default, not a cage** — rearrange by what the buyer needs most. For a
mature category, lead with differentiation ("the aha"); for a new category, lead with the
problem first.

## What makes this pattern work

- **Hero sells the outcome, not the product.** "Ship work on time" beats "Project
  management software". One clear job per page — don't advertise 8 features in the hero.
- **The product shot is the hero's second half.** Real UI in a browser frame converts
  better than abstract illustration for tooling.
- **Proof is layered and honest:** logo cloud (we're established) → stats (we're big) →
  testimonials (people like you succeed). Never all three identical claims.
- **Pricing is a decision, not a reveal:** 3 plans, a highlighted target plan, and a
  billing toggle — see `components/pricing.md`.
- **FAQ is objection-handling,** placed right before the final CTA so the last barrier
  is removed at the point of action.

## Design language for SaaS

- **Tone:** competent and calm. Confidence through whitespace, consistent grid, restrained
  palette — not decoration.
- **Palette:** light-first (near-white canvas) or dark-first (tinted near-black); one
  primary, one accent for CTAs, tinted neutrals (see `design-tokens/color-systems.md`).
- **Type:** one display + one body; a mono accent is a nice technical signature for
  developer/data products (see `typography-systems.md`).
- **Spacing:** generous section padding (96-128px) with a consistent scale — SaaS pages
  live or die on whitespace rhythm (see `spacing-scale.md`).

## Differentiation moves (to avoid the template look)

1. **Change the hero layout** — every competitor uses centered or 6/6 split; try
   text-forward, an editorial split, or product-as-background.
2. **Change the color strategy** — pick a non-purple/blue primary; use warm neutrals; make
   the accent unexpected.
3. **Lead with a different proof type** — a single featured customer story, an outcome
   comparison, or live product footage instead of a stat strip.
4. **Break one convention deliberately** — a non-sticky navbar, an asymmetric grid, a
   two-column pricing for a simpler product.
5. **Anchor on one feature** — instead of an even bento, make the differentiator a full
   section the competitors don't have.

## Responsive & accessibility

- Every section stacks cleanly; pricing and bento reorder to keep the anchor first.
- Sticky navbar collapses to a hamburger but **keeps the CTA visible**.
- Contrast AA everywhere; the product shot stays legible at mobile (crop to the meaningful
  part).
- See `accessibility/` for the full checklist.

## Anti-patterns (never copy)

- The same template: centered hero, purple gradient, 6-card bento, 3 identical pricing
  cards, gray testimonial wall. Exhausted.
- Hero with no product proof and no CTA clarity.
- Ten features when the buyer needs one story.
- Pricing hidden behind "Contact us" with no self-serve entry.
- A testimonial wall with no names or outcomes.
- Motion that announces itself (long entrances) instead of reinforcing.