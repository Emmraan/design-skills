# CTA (Call to Action)

The CTA section is the entire page distilled into one ask. Every page is built to end here
(or to point here), so this section must be **the loudest, most confident moment on the
page** — while still feeling like a natural invitation, not a shout.

## The job (what it must do)

1. **Repeat the core promise** — remind the user what they get in one line.
2. **Lower the last barrier** — the friction killer ("free", "no card", "2-minute setup",
   "cancel anytime") lives here.
3. **Ask once, clearly** — one primary CTA with an obvious destination.
4. **End the page with energy** — the last impression drives the return visit.

## Anatomy

```
        "Start shipping faster today"          ← promise line (display size)
   "Free 14-day trial · No credit card · Cancel anytime"
          [Start free]  [Talk to sales]        ← primary + optional secondary
```

- **Headline** (1 line): the same promise as the hero, rephrased for someone who's read
  the whole page. Big, display type.
- **Subline** (optional): the guarantee/friction line — this is where trust wins.
- **Primary CTA:** the strongest button on the page. Consider making it larger than any
  earlier button.
- **Secondary CTA** (optional): "Book a demo", "View docs" — ghost/outline, lower weight.

## Positioning on the page

- **Final section** — the classic: ends the page, sits above the footer.
- **Repeated mid-page** — after the 2nd or 3rd proof block, a slim CTA band
  ("Want to see it in action? → Book a demo") keeps momentum.
- **In the navbar/footer edges** — persistent mini-CTAs (see `navbar.md`).
- For long-form pages: interleave, don't only put the CTA at the very bottom.

## Design decision logic

- **Make it a moment:** give the CTA its own full-width band with a distinct background
  (accent-tinted, dark panel, or a subtle gradient) so the page clearly "pivots" into the ask.
- **The accent color owns this button.** If the page has been careful with accent, this is
  where it spends itself. No competing buttons or colors in the band.
- **Background drama is allowed here** more than anywhere: a gradient wash, an oversized
  wordmark watermark, or a product UI edge — it's the climax, decoration is permitted.
- **Button copy = outcome, not verb.** "Get started free" > "Submit". Add a micro-copy under
  the button if needed ("Free forever plan available").
- **Visual hierarchy in the band:** headline (largest) → subline → button. Nothing else
  competes.

## Friction-killer patterns

- Free trial + no credit card ("Start free — no credit card required").
- Immediate gratification ("Get your first report in 5 minutes").
- Reassurance stack as a single muted line, never a bullet list.

## Motion

- A gentle entrance (fade/slide) on scroll into view — one moment, not continuous animation.
- Optional hover glow/scale on the button (see `interaction-patterns/feedback-loading.md`).
- Respect `prefers-reduced-motion` — static but still styled boldly.

## Accessibility

- The button is a real `<button>` or an anchor with a real href and `aria-label` if the
  visible text is insufficient.
- Contrast: accent button text vs button fill must be AA (a bright accent with white text
  often fails — test it, see `contrast.md`).
- Focus ring clearly visible against the CTA band background.

## Responsive

- Band padding scales down; headline uses `clamp()`.
- Buttons: primary full-width on mobile, or keep two side-by-side if copy is short.
- No horizontal scroll from oversized watermark/decoration — `overflow: hidden` on the band.

## Anti-patterns (never copy)

- A CTA band with no contrast from the rest of the page — if it doesn't feel like a moment,
  it's just another section.
- Two equal primary buttons.
- Button copy that says nothing ("Click here", "Learn more").
- Asking for the email before offering anything ("Sign up" with no promise above it).
- A CTA with 3 paragraphs of copy — the ask should fit in 2 lines.
- Decorative elements that obscure the button or its focus state.