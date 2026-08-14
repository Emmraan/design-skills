# Color Systems

How to build a color system that gives a website a distinct identity — based on **roles**,
not arbitrary hex codes. Applies to any industry.

## Core concept: roles, not colors

A color palette works when every color has a **job**. The five core roles:

| Role | Job | Example sites |
|---|---|---|
| **Primary / Brand** | Identity + main actions | Wispr's violet-blue, ClickUp's purple |
| **Neutral / Base** | Backgrounds, text, structure | near-white surfaces, off-black text |
| **Surface** | Cards, panels, elevations | white/near-white, dark variants |
| **Accent** | Emphasis — one point of energy | Ramp's green CTA on navy |
| **Semantic** | Status: success / warning / danger / info | form validation, badges |

> A strong design limits its palette: **1 primary, 1-2 neutrals, 1 accent, 3-4 semantic**. If
> every color competes, nothing leads the eye.

## The three most common systems

### 1. Dark-first (modern SaaS / AI)
- Near-black base (not pure `#000` — tint it: `#0a0a0a`, `#0d0d12`, `#111`).
- Light text on dark: `#f5f5f7` / `#e5e5e7` (soft white, never pure).
- One bright accent for CTAs (the single luminous element).
- Surface hierarchy via dark shades, not opacity alone.
- Sites: Wispr, Linear, Vercel, Ramp.

### 2. Light-first / clean (productivity, editorial)
- Near-white canvas with a warm or cool tint (`#fafafa`, `#f8f9fb`).
- Off-black text (`#111827` family) — never `#000`.
- A single saturated primary for interactive elements.
- Lots of whitespace; color used sparingly.
- Sites: Notion, Gumroad, Ghost.

### 3. Bold / vibrant (consumer, playful, ecommerce)
- Saturated primary + playful secondary, high energy.
- Frequently paired with a dark or bold type for contrast.
- Gradients used deliberately (brand moments), not everywhere.
- Sites: ClickUp, Shopify, Framer.

## Rules that always hold

1. **Contrast before beauty.** Text must pass WCAG AA (4.5:1 body, 3:1 large text) against its
   background — always validate (`references/accessibility/contrast.md`).
2. **Tint your extremes.** Avoid pure `#000` and pure `#fff`; use near-blacks/near-whites so
   shadows, overlays, and edges stay visible.
3. **One accent.** Reserve accent color for primary CTAs + active states. If two elements both
   want the accent, one of them is decorative.
4. **Dark/light parity.** If you ship both modes, the *roles* stay the same; only the values
   change. Don't redesign between modes.
5. **Text colors are not brand colors.** Text neutral should be a gray scale (tinted toward
   your brand hue) — never your primary.
6. **Gradients: one hero moment.** A signature gradient on the hero/product shot is memorable;
   gradients on every button dilute the brand.

## How to read a palette (for analysis)

When analyzing a reference site, extract:
- What are the **roles** (which color is primary, neutral, accent, surface)?
- What is the **neutral strategy** (warm gray? cool gray? green-tinted?).
- How many colors carry the design (economy = confidence).
- Dark/light handling.
- Which color owns the CTA — and why that works.

## Anti-patterns (never copy)

- Default "AI purple-to-blue gradient" on everything — visually exhausted.
- Too many colors competing (no clear primary).
- Low-contrast text (gray on light gray) for body copy.
- Pure black background with pure white text (harsh; prefer tinted).
- Accent color used for both primary buttons and decorative backgrounds.
