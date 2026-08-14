# Motion

Motion gives a page **life and hierarchy**. The goal is choreography, not decoration:
motion should direct attention, communicate state, and never annoy.

## The rules of tasteful motion

1. **Animate only `transform` and `opacity`.** Animating `width`, `height`, `top`, `color`
   causes layout thrash and jank. Transform/opacity run on the compositor.
2. **Duration by distance.** Small element = fast (150-200ms); large/hero = slower (500-800ms).
3. **Easing matters more than duration.** Custom cubic-bezier for "expo-out" feel:
   `cubic-bezier(0.16, 1, 0.3, 1)` — decelerate dramatically (fast start, slow land).
   Default `ease` reads as flat/cheap.
4. **Stagger, don't sync.** Elements enter in sequence (~80-120ms apart), not all at once.
5. **Respect `prefers-reduced-motion`.** Provide a reduced/no-motion mode; it's a11y, not an
   afterthought.

## Where motion belongs

| Element | Behavior |
|---|---|
| Hero load | Staggered reveals: headline → sub → CTA → media (each ~80-120ms) |
| Page sections | Scroll-triggered fade/slide-in (once, subtle, non-blocking) |
| Buttons | Hover: quick 150ms transform (slight lift/scale) + color shift |
| Cards | Hover: raise + shadow (elev-1 → elev-2), 200ms |
| Modals | Fade backdrop + scale/slide panel (300-400ms) |
| Dropdown/menu | Fade + slide-y, 150-250ms |
| Tabs / accordion | Height/opacity transition on the content (240ms) |
| Loading | Skeleton shimmer (not spinners everywhere); progress where long |

## Motion tokens

```
--dur-fast:   150ms   (hovers, micro-interactions)
--dur-base:   250ms   (dropdowns, tabs, toggles)
--dur-slow:   600ms   (hero, modals, big reveals)
--ease-out:   cubic-bezier(0.16, 1, 0.3, 1)   (standard entrance)
--ease-in-out:cubic-bezier(0.65, 0, 0.35, 1)  (state transitions)
--stagger:    80-120ms
```

## How to read motion (for analysis)

- What loads with choreography (hero sequence, staggered items)?
- Which interactions are instant vs eased (hover feedback speed)?
- Are there scroll reveals, and are they subtle or distracting?
- Is there a custom easing signature (expo-out, spring-like)?
- Is reduced-motion respected?

## Anti-patterns (never copy)

- Everything bouncing/animating (motion sickness, cheap feel).
- Long animations on small elements (feels slow).
- Animating expensive properties (layout jank).
- No reduced-motion support.
- Autoplaying carousels without pause controls.
