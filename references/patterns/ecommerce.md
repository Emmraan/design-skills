# Ecommerce Pattern

Ecommerce pages live or die on **the product itself** — the design's job is to get out of
the way and make the product irresistible and instantly buyable. The winning pattern
balances **rich, appetite-whetting product storytelling** with **ruthless purchase friction**
removal.

## When to use

- Selling physical products, digital goods, or subscriptions with checkout.
- The page must move the visitor from interest → cart → checkout.
- Goal: conversion, AOV, repeat purchase.

## Canonical section order

```
1. Navbar (logo · search · cart · account · promo bar optional)
2. Hero (campaign/hero product — or clean landing for a single product)
3. Collection / category highlights (for storefronts)
4. Product grids (cards: image · name · price · rating)
5. Featured product deep-dive (hero product story)
6. Trust: shipping, returns, payment, reviews
7. Testimonials / reviews (social proof with photos)
8. FAQ (shipping, returns, sizing, fit)
9. Newsletter / promo CTA
10. Footer (with shipping/returns/legal links)
```

A **single-product page** collapses this: gallery → buy box (price, options, add-to-cart) →
details → reviews → guarantee → related products.

## What makes this pattern work

- **The image is the pitch.** Products are photographed/crafted to look desirable — first
  impressions come from the product, not the copy. Multiple angles, zoom, and a lifestyle
  context shot.
- **The buy box does the work:** price + variant selector + add-to-cart, all visible
  without scrolling, with stock/shipping hints beside it.
- **Friction killers are explicit:** free shipping threshold ("Free shipping over $50"),
  easy returns ("30-day returns"), secure payment icons ("Visa · PayPal · Apple Pay").
- **Urgency that's honest:** "Only 3 left", "Ships in 24h" — only if true; fake countdown
  timers erode trust and can be legally dicey.
- **Reviews with specifics** ("Runs true to size, comfy for 8-hour days") convert better
  than star-only aggregates. Show photos and verified badges.
- **Category clarity:** obvious collections/navigation so shoppers self-serve — ecommerce
  users browse, so the map matters more than the story.

## Design language for ecommerce

- **Tone:** the product is the hero — the UI should be clean, quiet chrome that lets goods
  shine. Loud decoration competes with the merchandise.
- **Palette:** neutral canvas (white/near-white) so product colors read true; one accent
  for CTAs/buy buttons. Seasonal/campaign color is fine in the hero only
  (see `color-systems.md`).
- **Type:** large, clean display for product names + a highly legible body; prices use
  tabular figures and sit clearly next to names (see `typography-systems.md`).
- **Cards:** consistent aspect ratios, generous whitespace, hover = image swap/quick-add.
  Grid is king; don't break the grid for decoration.
- **Motion:** hover reveals and micro-transitions on add-to-cart; a subtle cart flyout
  reinforces the action (see `feedback-loading.md`).

## Differentiation moves

1. **Editorial product storytelling** — hero campaigns, look-books, and long-form product
   narratives (fashion/beauty) instead of a plain grid.
2. **A signature product shot style** — consistent photography art direction (lighting,
   backdrop, angle) is the brand.
3. **Trust as a differentiator** — radical shipping/returns transparency, sustainability
   badges, founder notes.
4. **Personalization touch** — "Complete the look", size/fit recommendations, recently
   viewed (honest, not creepy).
5. **Campaign-led design** — seasonal/brand-moment pages with their own art direction
   (bold type, campaign photography) that still sell.

## Conversion mechanics (checkout-adjacent)

- **Add-to-cart feedback** is instant and visible (flyout, count bump, confirmation).
- **Mini-cart/cart summary** is always reachable; keep checkout 1-3 steps, guest checkout
  available.
- **Exit-interested signals:** cart abandonment recovery, "back in stock" waitlists — 
  functional, not dark patterns.
- **Promo codes** work without a scavenger hunt; a promo bar communicates current offers.

## Accessibility

- Product images need **descriptive alt text** ("Navy merino crewneck sweater") — this is
  also good SEO and helps text-only users.
- Variant selectors: real `<select>` or proper radiobuttons with labels; focus states on
  every buy control (see `a11y-checklist.md`).
- Color/size is never communicated by color alone (add text labels).
- Ensure the whole purchase flow is keyboard-operable.

## Responsive

- Grids go 2 columns → 1 on mobile; buy box stays sticky or above-the-fold at small widths.
- Tap targets ≥44px on add-to-cart, nav, and filter controls.
- Product images use responsive srcset — never one huge file for all widths.

## Anti-patterns (never copy)

- Dark-pattern urgency (fake countdowns, hidden unsubscribe, trick buttons) — legally and
  ethically out of bounds.
- Gigantic hero carousels that slow the page and bury the buy button.
- Grids with inconsistent image aspect ratios (jumpy layout).
- Text-only product pages (no imagery) — a lost sale.
- Reviews hidden or only aggregate stars with no details.
- Copying competitor product photography art direction wholesale — the images are often
  the brand.