# Stats

Stats (metrics / numbers / counters) deliver **social proof in numbers**: users trust
quantified outcomes more than adjectives. They compress a whole case study into one line.

## The job (what it must do)

1. **Prove traction** — revenue, users, uptime, ratings, speed, count.
2. **Stand alone** — a stat must be understood without context, or the context is one line.
3. **Anchor credibility** — they place the brand in a scale ("Trusted by 40,000 teams").
4. **Be honest** — numbers users can sanity-check (a 99.9% uptime is believable; "10x
   everything" is not).

## What counts as a stat

| Type | Example | Note |
|---|---|---|
| Adoption | 40,000+ teams, 2M downloads | Most common, most trusted |
| Outcome | 3.4x faster shipping, 47% less churn | Pairs with a comparison |
| Performance | 99.99% uptime, <50ms latency | Strong for infrastructure |
| Scale | 4B events/day, 120 countries | Impressive for platforms |
| Validation | 4.9/5 (2,300 reviews) | Rated by others = highest proof |
| Negative-to-positive | "From 40 hrs → 6 hrs a week" | Story in numbers |

## Layout directions

| Direction | Structure | Best for |
|---|---|---|
| Stat strip | 3-5 numbers in one row, dividers between | Compact, below hero |
| Stat band | Numbers on a colored/dark band across the page | Punchy, brand moment |
| Stat cards | Numbers in cards with labels/icons | Balanced, editorial |
| Paired comparison | "Before → After" two columns | Outcome-driven storytelling |
| Inline with quotes | Numbers embedded in testimonials | Native, unforced |

## Design decision logic

- **The number is the hero:** display size, bold, often the accent color or a strong
  contrast. The label is small, muted, all-caps or title case.
- **2-5 stats.** Fewer feels thin; more feels like a brag wall. 4 is the comfortable median.
- **Keep units legible:** "40,000+" with the "+", or round to "40k". Precision without a
  point ("1,847,203 users") looks fake.
- **Comparisons add meaning:** "vs 6 weeks before" turns a number into a claim. Use a muted
  "vs" annotation, not a second loud number.
- **No decimals unless honest:** 99.9% reads better than 99.9841%.
- Decorative dividers (thin vertical rules or dots) separate stats without boxing them.

## Motion

- **Count-up on scroll into view** is the classic — keep it fast (600-1200ms), ease-out, and
  start from a believable value (not 0 when the real number is 40k).
- Respect `prefers-reduced-motion`: show the final number immediately.
- Numbers that animate without being seen (below the fold, off-screen) are wasted effort —
  trigger on intersection, not on load.

## Typography

- Stat numbers use the **display** voice of your type system (see
  `typography-systems.md`) at large sizes — often 40-72px via `clamp()`.
- Keep the label in the body scale. Number:label ratio should be dramatic (size = proof).

## Accessibility

- **Use real text, not images** for numbers. Screen readers must read the value.
- If the number animates, the final value is the accessible value (`aria-live` not needed if
  it resolves fast; set `aria-hidden` on the animating span and provide the final text).
- Contrast: accent-colored numbers must still pass AA against their background.
- Context needed? Add a screen-reader-only full sentence ("Used by 40,000+ teams worldwide").

## Anti-patterns (never copy)

- Six identical stats with no hierarchy — a brag wall.
- Numbers with no source or anchor ("Trusted by everyone").
- Over-precise fake numbers.
- Count-up that starts at 0 and spins for 3 seconds — feels like a slot machine.
- Stats as images (unreadable, unresponsive).
- Numbers so large they break the layout on mobile (always `clamp()`).