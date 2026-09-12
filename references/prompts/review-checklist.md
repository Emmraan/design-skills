# Review Checklist — Validate a Generated Design

Run this self-check before presenting any design. Every item must pass. If any fail,
fix them before showing the result.

## Originality (non-negotiable)

- [ ] At least **3 references** were retrieved and used.
- [ ] At least **2 of {layout, color, typography}** differ from each single reference.
- [ ] The page does **not** reproduce any one site's structure, colors, and type together.
- [ ] No exhausted clichés unless deliberately inverted (purple gradient, floating orbs,
      3-card pricing with highlighted middle, "the future is here" copy).
- [ ] There is **one coherent design language** (single spacing scale, one type system,
      consistent color-role grammar) — not a patchwork.

## De-AI gates (non-negotiable — see playbook Phase 4)

- [ ] **Copy pass:** `references/copywriting/human-copy.md` audit gate passes —
      zero negation pivots, zero placeholder copy, every section anchored in specifics.
- [ ] **Design pass:** no synthesis-rules design AI-tell ships (centered-default,
      generic gradient, template grid, system-font flatness, stateless components,
      placeholder visuals, symmetric monotony, missing states).
- [ ] **Uniqueness statement written:** varied layout levers recorded with why they
      fit THIS surface — result is not describable as "like X but reskinned".

## Accessibility (WCAG AA minimum)

- [ ] Text contrast >= 4.5:1 (large text >= 3:1) on all surfaces, including on-color buttons.
- [ ] Visible **focus states** on every interactive element (not color-only).
- [ ] Full **keyboard navigation** works: tab order logical, no focus traps, skip link present.
- [ ] **Semantic HTML + ARIA**: landmarks, headings in order, `aria-label` on icon-only
      controls, decorative images `aria-hidden` or empty alt.
- [ ] Touch targets >= **44x44px** on mobile.
- [ ] No motion conveys meaning; `prefers-reduced-motion` respected.

## Responsiveness

- [ ] Works from **mobile (320-375px) to desktop (1440px+)** with no horizontal scroll.
- [ ] **Fluid type and spacing** (clamp / relative units), not fixed px everywhere.
- [ ] Defined **breakpoints**; split/centered heroes collapse sensibly; grids stack.
- [ ] Nav collapses (hamburger or equivalent) with CTA preserved.
- [ ] Images/visuals scale; product shots stay legible at small widths.

## Content & structure

- [ ] Hero answers "what is this / who is it for / one thing it does better".
- [ ] **One primary CTA** per view (secondary CTAs are quiet).
- [ ] Section order matches the closest pattern; each section has a clear job.
- [ ] Trust/proof appears early for trust-heavy industries (fintech, commerce, enterprise).

## Code hygiene

- [ ] Valid, semantic HTML; accessible form labels; buttons vs links used correctly.
- [ ] No orphaned styles; tokens/theming reused, not repeated inline values.
- [ ] Performance sane (no massive unoptimized imagery, no render-blocking bloat).

## Final gate

- [ ] Recorded synthesis note: which reference contributed which logic.
- [ ] The design would not be mistaken for any single reference site.