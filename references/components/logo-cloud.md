# Logo Cloud

The logo cloud is the fastest credibility device on the internet: a row of recognizable
logos implies "all of these already chose us". It needs almost no copy because the logos
are the argument.

## The job (what it must do)

1. **Anchor scale** — "if these companies trust us, we're legit".
2. **Establish the tier** — the logo set *is* the claim about who your customers are.
3. **Signal category fit** — showing logos from your target industry makes visitors
   self-select ("people like me use this").
4. **Cost nothing to read** — a subheadline line ("Trusted by 40,000+ teams") + logos.

## Anatomy

```
"Trusted by teams at"                    ← tiny, optional, muted
[Acme] [Vertex] [North] [Lumen] [Ossa]   ← wordmark-style logos
```

- **One intro line** ("Trusted by…" / "Powering workflows at") — keep it muted and small.
- Logos in **grayscale/monochrome** by default; full color on hover (or subtle opacity
  change). Colored logos compete with each other; gray logos read as one calm band.
- No logos at all = no proof; this section collapses to the intro line.

## Where it goes

- **Right under the hero** — the standard, strongest position ("we're established").
- In the footer or near the CTA for a quieter echo.
- Rarely alone mid-page — combine with a stat ("…and 40,000+ other teams").

## How many logos

- **5-10.** Fewer feels thin, more becomes a blur.
- Two rows of ~5 is fine; three rows is a brag wall.
- Scale matters more than count: a set of 6 logos you recognize beats 30 you don't.

## The honest version (real logos)

- Use **actual customers** if you have them — this is the whole point.
- Monochrome wordmarks on one row at a consistent height (~24-32px), evenly spaced with
  generous gaps.
- Logos should be legible at their displayed size — a logo shrunk so much it's a smear is
  useless.

## Design decision logic

- Keep the band on a quiet background (white/near-white or the dark surface) so the logos
  are the only content.
- Logo contrast: grayscale logos on a dark band need enough lightness to read; test AA-ish
  visibility even for non-text marks (see `contrast.md`).
- A gentle marquee (logos scrolling in a loop) is popular — see motion notes below. A static
  row is calmer and fine.

## Motion (marquee)

- If marquee: slow (20-40s per loop), pause on hover, and duplicate the set for a seamless
  loop. Start/end with a fade mask so items appear/disappear gracefully.
- Respect `prefers-reduced-motion` → show a static, wrapped grid.
- Never make marquee the only way to see logos (wrap at mobile).

## Responsive

- Logos wrap to 2-3 per row on mobile — never shrink them below legibility.
- Marquee degrades to a wrapped static grid at small widths if it can't fit.

## Accessibility

- Logos are links/`<img>` with `alt` = the company name (or wrapped in a link to their site).
  Decorative repeats get `aria-hidden`.
- If a logo is part of a marquee, ensure the accessible version is static/complete.

## Anti-patterns (never copy)

- Logos you don't actually have as customers.
- Full-color logos of wildly different visual styles crammed together — a cluttered mess.
- 40 tiny unreadable logos.
- A marquee so fast it reads as chaotic movement.
- Logo cloud with no intro line and no context — floating logos mean nothing.
- Logos on a background where gray marks disappear (no contrast).