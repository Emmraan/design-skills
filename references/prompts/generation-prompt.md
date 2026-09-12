# Generation Prompt — Build an Original Website from the Design Brain

Use this prompt (or its logic) whenever a user asks you to design or build a website,
landing page, or page section. It forces retrieval-first synthesis, not template reuse.

## The prompt

> I need a <PAGE TYPE> for a <INDUSTRY / CATEGORY> product. Here is the brief:
> - **Product / offer:** <what it is and the ONE outcome it delivers>
> - **Audience:** <who it is for>
> - **Tone / style direction:** <e.g. minimal premium, bold playful, editorial dark, warm friendly>
> - **Theme:** <dark / light / either>
> - **Page sections needed:** <hero, features, pricing, faq, testimonials, etc.>
> - **Constraints:** <framework, accessibility AA, mobile-first, speed, brand colors if any>
>
> Build an **original** design — do not copy any single reference. Follow this process:
>
> 1. Read `INDEX.md`. Then use `references/retrieval/` to pick **3+ relevant references**
>    (websites from the closest industry/style, plus the matching pattern and component files).
> 2. Read `references/processes/ui-build-playbook.md` and follow its phases
>    (Brief lock → Design-language lock → Compose → De-AI pass → Critique → Polish).
> 3. Extract **design logic** from each (layout, spacing rhythm, type pairing, color *roles*,
>    motion, accessibility), not pixel values.
> 4. **Combine** ideas so at least 2 of layout / color / typography differ from any single source.
> 5. Assemble the page with the closest `references/patterns/*` pattern, token systems from
>    `references/design-tokens/`, components from `references/components/`, and a11y rules
>    from `references/accessibility/`.
> 6. Run the **De-AI pass**: audit all copy with `references/copywriting/human-copy.md`
>    and all visuals with the review-checklist De-AI section — hard gates, not advisory.
> 7. Output **real, responsive code** (or a detailed design spec), then self-check against
>    `references/prompts/review-checklist.md`.
>
> **Rules:** never reproduce a reference verbatim; keep WCAG AA contrast + visible focus +
> keyboard navigation + touch targets >= 44px; fluid type/spacing; note briefly where your
> choices came from (which reference gave which logic).

## Short form (for quick requests)

```
Design an original <industry> landing page.
Tone: <minimal | bold | editorial | playful> · Theme: <dark|light>.
Sections: hero, features, pricing, faq, testimonials, cta.
Retrieve 3+ references (websites + pattern + components), synthesize their LOGIC,
generate a NEW design language, keep it accessible + responsive, ship real code.
```

## What NOT to do

- Do not open a single reference and mirror it.
- Do not dump hex values / px as the design language — use roles and systems.
- Do not skip the a11y or responsive pass even for "quick" designs.
- Do not use the exhausted default (centered hero + purple gradient + 3-card pricing)
  unless the user explicitly wants it.
