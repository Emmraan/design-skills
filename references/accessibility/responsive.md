# Responsive Design

Responsive isn't "a mobile version" — it's **one design that adapts**. Every generated site
must work from 320px phones to wide desktops without horizontal scroll or broken hierarchy.

## Breakpoints (start with 3, extend if needed)

| Range | Behavior |
|---|---|
| `< 640px` | Mobile — stacked single column, hamburger or simple nav, edge padding 16-20px |
| `640–1024px` | Tablet — 2-column layouts where sensible, nav compresses |
| `> 1024px` | Desktop — full 12-col grid, full spacing, complex hero |
| `> 1440px` | Cap container (1140-1280px) or add generous edge padding |

Design **mobile-first** (base styles = mobile, then `min-width` media queries layer up).

## What changes at each breakpoint

| Element | Desktop | Mobile |
|---|---|---|
| Grid | 12-col, 4/4/4 cards | Stacked 1-col, full width |
| Hero | Split text+media, big display type | Stacked, smaller display, media below text |
| Nav | Full links inline | Hamburger → slide-down/full menu |
| Pricing | 3 cards side-by-side | Stacked or horizontal scroll |
| Spacing | Section padding 96-128px | 48-64px |
| Tables | Full table | Cards-per-row or horizontal scroll |
| Forms | Inline rows | Single column |

## Fluid techniques (prefer over many breakpoints)

- **Fluid type:** `clamp(2.5rem, 5vw + 1rem, 4.5rem)` for display — scales smoothly.
- **Fluid spacing:** `clamp(2rem, 4vw, 6rem)` for section padding.
- **CSS Grid auto-fit:** `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` for
  card rows — no breakpoint needed.
- **`min-width: 0`** on grid children to prevent overflow.

## Hard rules

1. **No horizontal scroll** at any width — check 320px, 375px, 768px, 1440px.
2. **Text never clips** — allow wrapping, no fixed-width text boxes.
3. **Tap targets ≥44px** on touch (see `a11y-checklist.md`).
4. **Touch-friendly nav** — a burger that expands is standard; ensure keyboard/Esc support.
5. **Images** — `srcset`/responsive images, `max-width: 100%`, `loading="lazy"` below the fold.
6. **Content hierarchy preserved** — the *order* of information shouldn't jump around between
   breakpoints unless intentional.

## Mobile-specific UX

- Primary CTA **above the fold** and easy to tap (thumb reach).
- Phone number / key actions one-tap (tel: links).
- No hover-dependent interactions (menus that only open on hover break touch).
- Testimonials/stats: avoid tiny multi-column cramming — stack.

## How to read (for analysis)

- Where do breakpoints kick in, and what *changes* (not just scaling)?
- How does the hero reflow (stack order)?
- Does the nav switch to a burger?
- Are tables/tabs/form rows handled or just squeezed?
- Fluid type/spacing used?

## Anti-patterns (never copy)

- Shrinking everything to fit mobile (unreadable 11px text).
- Horizontal scroll / content overflow.
- Hover-only menus on touch devices.
- Different design "rebuilt" for mobile (inconsistent).
- Ignoring tablet widths (huge jumps between mobile and desktop).
