# Radius & Shadows

Radius and shadows define a surface's **physicality** — how the page feels (sharp/technical,
soft/friendly, floating/premium). Both need scales, never random values.

## Border radius

| Token | Value | Use |
|---|---|---|
| `radius-sm` | 6-8px | Inputs, small buttons, badges |
| `radius-md` | 12-16px | Cards, modals, large buttons |
| `radius-lg` | 20-28px | Big surfaces, feature panels, app-like cards |
| `radius-pill` | 999px | Pills, tabs, search bars, avatar |

Rules:
- **Pick a consistent family** (mostly sm+md, or mostly md+lg) and stick to it.
- **One accent radius** — a hero image or product card can be dramatically rounded; don't
  round everything.
- Rounded = friendly/consumer; sharp = technical/premium. Match to brand personality.
- 0 radius is a valid choice (tech, editorial) — just be intentional.

## Shadows (elevation)

Use **layered shadows** for depth, mapped to a small elevation scale:

| Elevation | Usage |
|---|---|
| `elev-1` | Resting cards (subtle): `0 1px 2px rgba(0,0,0,.04), 0 1px 3px rgba(0,0,0,.08)` |
| `elev-2` | Hovered/interactive cards, dropdowns: `0 4px 8px ..., 0 8px 24px ...` |
| `elev-3` | Modals, popovers, floating elements: `0 8px 16px ..., 0 24px 48px ...` |

Rules:
- **2-layer shadows** (tight + soft) look far better than one big blur.
- **Tint shadows toward your brand/neutral** (`rgba(15,23,42,.08)` cool, or warm `rgba(17,24,39,.08)`).
- **Elevation must mean something** — an element rises when it's interactive or layered.
- **Borders beat shadows for structure.** In light UIs, a subtle 1px border on cards + one
  soft shadow reads cleaner than a heavy shadow.
- Dark themes: use **light-on-dark shadows** sparingly — depth often comes from surface
  brightness differences instead (elevated surfaces get lighter, not more shadowed).

## How to read (for analysis)

- Radius family (sharp vs rounded) and any single accent radius.
- Shadow scale: how many elevations, are they 2-layer, cool/warm tint.
- Does elevation map to interaction (hover raises)?
- Dark theme: shadows vs surface-brightness approach.

## Anti-patterns (never copy)

- One giant blur shadow on everything (muddy, outdated).
- Radius values that don't belong to a family (5px here, 18px there).
- Heavy shadows in dark themes (looks off — prefer surface lightness).
- Hover raising every element (no hierarchy of motion).
