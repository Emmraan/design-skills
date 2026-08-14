# Features

The features section is the proof section: it must convert "what it is" (hero) into "what it
does for me" (here). Boring feature grids read as laundry lists; great ones teach the user
their own job.

## The job (what it must do)

1. **Explain value, not functionality** — lead with the benefit, support with the feature.
2. **Teach the mental model** — one feature can anchor the whole page (the "hero feature").
3. **Organize** so a scan in 5 seconds surfaces the 3 things that matter.
4. **Reinforce trust** — screenshots, short descriptions, and concrete outcomes.

## Layout directions

| Direction | Structure | Best for |
|---|---|---|
| Bento grid | Irregular cards of mixed sizes on a grid | Modern SaaS/AI — ClickUp, Notion |
| Uniform card grid | 3x2 or 2x2 equal cards | Tried, calm, safe |
| Alternating rows | Feature + image, left/right alternating | Deep storytelling |
| Sticky feature list | Scrolling sticky left column, items scroll right | Feature-heavy tools |
| Tabs / segmented | One feature visible, others behind tabs | Many features, few words |
| Single anchor feature | One big feature deep-dive, rest small | One killer differentiator |

## Design decision logic

- **Copy first:** each feature = benefit headline + one-line detail. If a feature can't be
  explained in one line, it isn't ready. Lead with the outcome: "Edit like a document" not
  "collaborative rich-text editing".
- **Card anatomy:** optional icon → title → short description (→ small link). Icons add
  identity — use a consistent, restrained icon set, not 6 different illustration styles.
- **Visual anchors:** give each card a real visual (mini screenshot, mock UI, chart) where
  possible. Text-only bento grids feel flat.
- **Hierarchy:** one feature should stand out (larger cell, accent stroke, gradient edge).
  Equal cards with equal weight = no story.
- **Backgrounds:** alternate surface tone per row/cell to create rhythm; keep text contrast
  AA (see `accessibility/contrast.md`).

## The anchor/hero feature pattern

When one feature differentiates you (AI, automation, speed):

1. Give it its own large section above the grid, or the biggest cell in the bento.
2. Show it doing its job (demo gif/screenshot annotated with a caption).
3. State the outcome the user can't get elsewhere — this is your moat.

## Typography & spacing

- Card titles at h3 size, descriptions at body size with muted color.
- Consistent card padding (use the spacing scale, ~24-32px) and gap.
- Icon color can carry the accent (one hue family, tinted per card is okay) — the brand
  accent stays reserved for CTAs.

## Responsive

- Bento grids reflow: keep the anchor cell prominent at mobile, stack cards full-width.
- Tabs become stacked sections or a horizontal scroll at small widths (respect touch).
- Never shrink card text to fit — let cards grow vertically.

## Accessibility

- Real headings (`<h2>` per feature group, `<h3>` per card) — this is how screen readers
  scan features.
- Tabs: proper `tablist/tab/tabpanel` roles + arrow-key navigation
  (`interaction-patterns/navigation.md`).
- Decorative visuals `aria-hidden`; informative screenshots need alt or a text fallback
  (the description already covers most of it).
- Contrast for muted description text: keep ≥4.5:1 or bump it — muted ≠ invisible.

## Anti-patterns (never copy)

- Six identical cards with tiny, generic icons and three-word titles — a wallpaper, not proof.
- Feature names that don't mean anything ("Advanced intelligence module").
- No visuals at all — text walls read as unbuilt.
- A bento grid where every cell is a different color and nothing leads the eye.
- Feature copy that lists capabilities ("supports X, Y, Z") instead of outcomes.