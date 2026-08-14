# Wispr — Design Analysis

> Source: `https://wisprflow.ai/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Wispr Flow is an AI dictation product. The page is a dark, editorial, almost literary
> interpretation of an AI tool — a deliberate counter to the "techy" AI look.

## 1. Visual Theme & Atmosphere

- Dark-first but **not cold**: a near-black canvas tinted warm, with cream/paper whites for
  text. Feels like a well-printed book in low light, not a terminal.
- **Editorial + human.** Big serif display (EB Garamond) at huge sizes, tight leading,
  italic flourishes. The product is framed as *writing*, not typing.
- Playful accents — pink, warm orange, lavender — keep it friendly; a single bright element
  (coral CTA) is the energy point.
- Overall mood: premium, calm, confident, quietly distinctive.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / CTA | coral `#FF6C4C` | The one bright action color (CTAs, highlights) |
| Surface / canvas | dark, near-black tinted | Page background |
| Text on dark | cream `#FFFFEB` | Headlines/body on dark |
| Accent wash | lavender `#F0D7FF` | Soft secondary surfaces, highlights |
| Accent | pink `#FFBCF2` | Playful secondary accent (tertiary) |
| Text accent | berry `#7F1C34` | Accent text on light washes |

- **Economy:** very few colors; dark canvas + cream text + one coral accent carries the
  whole identity. Lavender/pink are used in small moments, not floods.
- **Dark/light handling:** dark is the base; light cream surfaces are used as inset cards so
  content "pops" against the dark.

## 3. Typography Rules

- **Pairing:** EB Garamond (display serif) for headlines + Figtree (humanist sans) for body.
  Mono accents (Monaspace/Inter) appear for technical/label moments.
- **Display scale is enormous:** 120px / 96px / 75px / 64px headlines at `line-height ~0.85-1`
  — tight, confident, editorial. This is the dominant design lever.
- **Body:** Figtree at 14-18px, `1.3` leading, comfortable measure.
- **Hierarchy levers:** size first, then weight (500/600), then color (cream vs muted).
  Headlines rely on *scale + tight leading*, not boldness.
- **Italics** used deliberately (Garamond italic) for emphasis words — a literary signature.

## 4. Component Stylings

- **Primary button:** pill/full radius, coral fill or dark with cream text, generous padding
  (16px × 24px observed). One loud action per viewport.
- **Secondary button:** ghost/outline, quiet.
- **Inputs:** pill, cream/soft fill on dark, 12px × 16px padding.
- **Cards:** soft lavender/cream washes, small radius, hairline borders; content-first with
  generous padding.
- **Nav:** transparent on dark hero, becomes a blurred dark bar on scroll; links muted,
  CTA stands out.

## 5. Layout Principles

- **Spacing scale:** 8px base (xs 2 → xxxxl 8 in Dembrandt tokens), but sections breathe with
  large paddings — hero headline is enormous and the layout is centered/split with ample
  negative space.
- **Grid:** centered column with wide max-width; split hero pairs a big headline with a
  product/visual half. Rows separated by generous vertical rhythm.
- **Whitespace is the luxury:** the layout rarely fills every column — it lets the serif
  type and dark canvas do the work.
- **Breakpoints:** ~1280/1200/992/991 (desktop → tablet → mobile collapse).

## 6. Depth & Elevation

- **Flat by design:** subtle shadows only (small, low-opacity), hairline borders, and
  inset color washes instead of heavy elevation.
- Surfaces are distinguished by *tone* (cream/lavender washes) more than by shadow — keeps
  the literary calm.

## 7. Do's and Don'ts

- **Do:** lead with enormous editorial type; keep one bright accent; use italics and warm
  neutrals for humanity; let dark canvas breathe.
- **Don't:** flood with gradients; add multiple bright colors; make the type small and
  techy; use default "AI purple" gradients.

## 8. Responsive Behavior

- Display type scales down via `clamp()`-style fluid sizes; the huge hero (120px) compresses
  at tablet/mobile.
- Split hero stacks to headline-first, visual below.
- Nav collapses to hamburger; CTA remains visible; touch targets ≥44px.

## 9. Agent Prompt Guide

> Build a landing page with a **dark, warm, editorial aesthetic**: near-black tinted canvas,
> cream paper-white text, a single coral accent for the primary CTA. Use a large serif
> display (EB Garamond-style) at 80-120px with tight leading and italic emphasis; pair with a
> humanist sans body at 16-18px. Keep the palette to dark + cream + one accent. Generous
> whitespace, flat surfaces with subtle tone washes, pill buttons. Lead with a product/demo
> visual beside the headline. Content tone: calm, human, confident — like a well-designed
> book, not a tech pitch.

## 10. Component Map

1. Nav — transparent → blurred dark on scroll; CTA visible.
2. Hero — giant serif headline + product/demo visual + coral CTA + trust line.
3. Social proof — logo row / stats on dark.
4. Product feature — how dictation works (split, visual-led).
5. Feature grid — lavender/cream inset cards.
6. Testimonials — editorial quotes on dark.
7. CTA band — cream or accent moment, single action.
8. Footer — muted links on dark.

## 11. Pattern Position

Best fits the **AI product** pattern (`patterns/ai-product.md`): demo-in-hero, honest
expectations, trust answers. It executes the "editorial over techy" differentiation move —
the strongest counter to the default AI look.

## 12. Synthesis Notes

- **Unique:** the literary serif display at 120px on a dark warm canvas; the
  book-not-terminal mood; coral-as-only-accent discipline; italic emphasis.
- **Combine with:** a light/editorial fintech's precision (Ramp) for contrast pairing; a
  clean SaaS grid (Ghost) for section rhythm; playful accent logic (Gumroad) for the single
  bright moment.
- **Weaknesses / avoid:** can feel sparse for feature-heavy products; the huge type needs a
  strong demo visual to carry mobile; avoid copying its exact coral-on-dark recipe without
  changing the type/color roles.