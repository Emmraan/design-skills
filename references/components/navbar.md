# Navbar

The navbar is the silent contract: it tells users where they are and where they can go. Good
navigations disappear when used and reappear when needed. Bad ones dominate the design or
bury the CTA.

## The job (what it must do)

1. **Orient** — brand/logo on the left (always links home).
2. **Navigate** — the 3-7 most important destinations (never everything).
3. **Convert** — one primary action (Sign up / Get started / Contact), clearly the loudest.
4. **Adapt** — collapse to a hamburger/overlay on mobile without losing any of the above.

## Anatomy (typical)

```
[Logo]  Product  Solutions  Pricing  Docs  [Log in]  [Get started]
        └──────────── links ──────────┘   └──── actions ────┘
```

- **Logo** left. **Links** center or left-of-center. **Actions** right.
- Primary CTA is the only filled/accent button; log in is a quiet text/ghost link.
- Utility items (search, theme toggle, language) sit between links and actions.

## Structure rules

1. **5-7 items max.** Every extra link dilutes the hierarchy. Drop the rest into a menu
   ("More", a "Resources" dropdown).
2. **Dropdowns for depth, not breadth.** "Product" with a mega-menu of features is fine;
   a flat nav of 12 links is not.
3. **Name pages by what users call them** ("Pricing", "Docs", "Changelog") — avoid
   invented labels.
4. **The CTA stays constant.** Don't change the primary CTA label from page to page.
5. **Sticky vs not:** sticky navbar (white/blur backdrop) is the default for long pages;
   a transparent-to-solid transition on scroll is a nice touch. Skip sticky entirely on
   short landing pages if it saves space.

## Design decision logic

- **Height:** 64-80px desktop (touch target ≥44px). Not much taller — it eats content.
- **Backdrop:** translucent + `backdrop-filter: blur()` when sticky — content scrolls under
  it, so it must stay legible. Give it a hairline bottom border (or shadow) for separation.
- **Dark/light:** on dark heroes, the navbar can start transparent and become a dark panel
  after scroll. Never lose CTA contrast during the transition.
- **Typography:** nav links ~14-15px, medium weight. Logo sits at display size. The CTA uses
  the primary button style (see `cta.md`).
- **Active state:** underline/pill/color for the current section on single-page sites —
  subtle, never a bold box that fights the CTA.

## Mobile behavior

- Collapse to a hamburger + slide-in/full-screen overlay panel.
- Overlay lists links at ~18-20px with comfortable rows (48px), then actions last, and the
  primary CTA pinned or full-width at the bottom (thumb reach).
- Keep the logo + CTA visible in the collapsed bar — hiding the CTA kills conversions on
  mobile.
- Support `escape` to close, focus trap, and body-scroll lock when open
  (`interaction-patterns/navigation.md`).

## Accessibility

- Semantic `<nav>`; `aria-current` on the active link (see `semantics-aria.md`).
- Hamburger: `aria-expanded` toggling, real `<button>`, visible focus.
- Dropdowns open on hover **and** focus; closable via keyboard; `aria-haspopup` +
  `aria-expanded` where applicable.
- Tap targets ≥44px, especially on mobile.

## Anti-patterns (never copy)

- Navbar that hides or changes the CTA on scroll (users can't find the action).
- 10+ links with no visual order.
- Hamburger-only nav on desktop.
- Dropdowns that require hover (mouse-only) — keyboard users get stuck.
- Logo + giant search bar + 8 links + 2 CTAs crammed into one row.
- Auto-hiding navbar that delays "show" on every scroll — feels broken, not minimal.