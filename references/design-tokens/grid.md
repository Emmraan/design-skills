# Grid

A grid is the invisible skeleton that makes a page feel deliberate. Pick a system, use it
consistently, and break it *on purpose* only for signature moments.

## The standard: 12-column grid

```
┌────────────────────────────────────────────────┐
│   1   2   3   4   5   6   7   8   9  10  11  12 │
└────────────────────────────────────────────────┘
gutters: 16-24px desktop · 12-16px mobile
max-width: 1140-1280px container (or 1440px with edge padding)
```

- 12 columns is the most flexible (divisible by 1,2,3,4,6,12).
- Container max-width keeps lines readable on huge monitors.
- Edge padding on mobile (16-24px) so content never touches the screen edge.

## Common layout patterns

| Pattern | Columns | Use |
|---|---|---|
| Full-bleed | 12 | Hero, cinematic media, CTA bands |
| Split | 6/6 | Hero with text + media, about sections |
| Asymmetric split | 5/7 or 4/8 | Editorial heroes, feature spotlights |
| 3-card row | 4/4/4 | Features, pricing tiers, testimonials |
| 2-card row | 6/6 | Bigger features, use cases |
| 4-up grid | 3/3/3/3 | Stats, logos, small cards |
| Sidebar layout | 8/4 or 9/3 | Docs, dashboard, content+aside |

## Grid rules

1. **Breakpoints, not arbitrary widths.** Define 3-4:
   - `< 640px` mobile (stacked, 1 col)
   - `640-1024px` tablet (2 cols where sensible)
   - `> 1024px` desktop (full 12-col system)
   - `> 1440px` cap the container width
2. **Align everything to the grid.** Misaligned elements are the #1 "something's off" signal.
3. **One deliberate break.** A hero that breaks the grid (off-canvas image, oversized type
   overflow) creates the signature moment — but only once or twice per page.
4. **Baseline + vertical rhythm.** Pair grid columns with the spacing scale so blocks align
   vertically too.
5. **Mobile-first.** Stack first, add columns as space allows.

## How to read a grid (for analysis)

- Column count / container width / gutter.
- Which pattern each section uses (split, 3-card, full-bleed).
- Where the grid is deliberately *broken* (signature moments).
- Breakpoint behavior (how things stack).

## Anti-patterns (never copy)

- No container max-width (content stretches absurdly wide).
- Misaligned sections (elements not sharing column edges).
- Grid broken everywhere (chaos, no system).
- Fixed-width layout that doesn't scale down (horizontal scroll on mobile).
