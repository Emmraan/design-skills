# Spacing Scale

Spacing is what separates professional design from amateur design. Consistency beats
precision: **a constrained scale, applied rhythmically.**

## The scale

Use a **base unit** (4px or 8px) and multiples. Two proven scales:

```
4px scale:  4  8  12  16  20  24  32  40  48  64  80  96  128
8px scale:  8  16  24  32  40  48  64  80  96  128  160  192  256
```

Rarely do you need more than ~10 steps. Define them as tokens, never raw numbers scattered
in code.

## Spatial tokens (semantic, not numeric)

Name spacing by *use*, so decisions stay consistent:

| Token | Value (example) | Used for |
|---|---|---|
| `space-1` | 4px | Icon-to-text gap inside buttons |
| `space-2` | 8px | Compact element gaps, table cell padding |
| `space-3` | 12-16px | Card padding (small), form field spacing |
| `space-4` | 24px | Default card padding, grid gutter |
| `space-5` | 32-40px | Section inner padding (comfortable) |
| `space-6` | 64px | Between major blocks on a section |
| `space-7` | 96-128px | Between full sections (vertical rhythm) |
| `space-8` | 160-192px | Hero / full-bleed section padding (desktop) |

## Rules of rhythm

1. **Space between groups > space within groups.** Cards' content is tightly grouped; cards
   themselves sit apart. This single rule creates most perceived "cleanliness".
2. **Sections breathe on desktop, compress on mobile.** Desktop sections often use 96-128px
   vertical padding; mobile roughly halves it (48-64px) — fluid with `clamp()` or tokens.
3. **Bump in pairs.** When increasing a step, usually adjacent elements also shift; a single
   lone gap reads as a mistake.
4. **Consistency across pages.** The same component always uses the same token.
5. **8px grid for layout, 4px for micro.** Large layout = 8px rhythm; tiny in-button detail
   can step at 4px.

## How to read spacing (for analysis)

- What is the **base unit** (4 or 8)?
- What is the **section rhythm** (how much vertical padding between sections)?
- How much **breathing room** does the hero have vs content sections?
- Is spacing **consistent** (same component, same gaps everywhere)?
- **Mobile vs desktop** — does spacing compress fluidly?

## Anti-patterns (never copy)

- Random spacing values (17px, 23px) — no system.
- Everything glued together (no section rhythm).
- Huge gaps everywhere (design feels empty, hard to scan).
- Inconsistent card padding across the page.
