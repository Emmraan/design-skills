# Hero

The hero sets the entire design language in the first 2 seconds. It must state **what the
product is, who it is for, and the one thing it does better** — with the visual confidence
to make the visitor believe it.

## The job (what it must do)

1. **Answer "what is this?"** — a headline, not a tagline. Name the outcome, not the feature.
2. **Establish the design language** — type, color, and spacing identity show up here first.
3. **Give one clear next action** — a single primary CTA (secondary = "see how it works").
4. **Prove it, don't claim it** — a product shot, screenshot, or live demo beats slogans.

## Layout directions

| Direction | Structure | Feels / best for |
|---|---|---|
| Split hero | Headline left, product/shot right (7:5 or 6:6) | Classic SaaS — Ramp, ClickUp |
| Centered | Headline + CTA centered, product below | Announcement moments, AI launches |
| Text-forward | Big type only, no product shot | Premium/editorial confidence — Ghost |
| App-in-browser | Product shown inside a browser chrome frame | Familiar, credible for tooling |
| Full-bleed demo | Product UI fills the fold as the background | Bold, immersive — modern AI tools |
| Editorial split | Asymmetric headline + oversized image/card | Agency, portfolio, fashion-adjacent |

## Design decision logic

- **Hierarchy lever: size.** The headline is the largest element on the page — everything
  else recedes. Save "large + bold + high-contrast" for the headline alone.
- **Subheadline** is body-sized or one step up, muted (70% contrast of headline), and
  limited to 1-2 lines.
- **Primary CTA** is the single accent-colored object in the hero. Secondary CTA is quiet
  (ghost/outline or text link). Two equal buttons = no decision.
- **Trust line** (optional, small): "No credit card · 14-day trial · SOC 2" — place *below*
  the CTAs, not competing with them.
- **Product shot** should be cropped/conveyed to feel real but not busy. Overlays, floating
  cards, and annotation chips add depth — use 1-2 max, never a collage.

## Typography

- Headline: **clamp()** fluid size, tight line-height (1.05-1.15), near-black/dark on light
  themes; near-white on dark themes. Use weight + tracking, not pure scale.
- Balance the headline to roughly a 3:2 or 1:1 word-count with the subheadline — a wall of
  text in the hero is a lost visitor.
- Eyebrow/overline ("Built for designers", "v2.0") is optional — uppercase + letterspacing,
  small, in accent or muted color. Use it only if it adds meaning.

## Color

- Hero is often the **lightest or darkest** surface on the page to frame the product shot.
- The accent belongs to the primary CTA (and possibly one highlight word in the headline).
- Gradients: one controlled hero moment (background wash behind the product, or a headline
  highlight). Never a gradient on every button.

## Motion

- Entrance animations are brief (300-500ms), staggered by element, and **not** required for
  content (respect `prefers-reduced-motion`).
- Subtle continuous motion (slow gradient drift, floating card bob) adds life — 2-3x slower
  than you think looks right.
- The product shot can have a gentle parallax/scale on scroll, but the headline should stay
  put — moving type makes it unreadable.

## Spacing & rhythm

- Hero padding is the **largest** section padding on the page (often 96-160px top).
- Consistent gutter + max-width (~1200-1280px) keeps the hero aligned with the page grid.
- Vertical rhythm: eyebrow → headline → subhead → CTAs → trust/credit line, with clear
  breathing room between each (use the spacing scale, see `design-tokens/spacing-scale.md`).

## Responsive

- At mobile: split heroes stack (headline first, then product), padding drops to the section
  minimum, and CTA buttons go full-width or stay side-by-side if text fits.
- Text-forward heroes scale down gracefully — this is why they're popular.
- Product shots in browser frames must scale; consider showing the top 60% of the UI so it
  stays legible at small widths.

## Accessibility

- Headline + subheadline contrast against background: WCAG AA or better
  (`references/accessibility/contrast.md`).
- CTA focus state must be clearly visible (not just color — outline/focus ring).
- Decorative product imagery: `aria-hidden="true"` + empty alt. Informative overlays get real
  alt text.
- Do not rely on motion to convey meaning.

## Anti-patterns (never copy)

- Hero with 3+ CTAs (primary, secondary, "download", "learn more"… — paralysis).
- Headline that describes the product literally ("Project management software") instead of
  the outcome ("Ship work, on time").
- A giant stock photo that means nothing.
- 12 links in the nav competing with the CTA.
- Copy-pasted "AI" gradients and floating orbs — visually exhausted.
- Product screenshot so small it reads as a thumbnail at 1440px.