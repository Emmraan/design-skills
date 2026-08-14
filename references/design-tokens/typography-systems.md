# Typography Systems

Typography is 90% of perceived design quality. Build it from **logic** (pairing, scale,
measure) — the font choice itself is the smallest part.

## The pairing formula

Use **at most 2 families**: one **display/headline** voice + one **text/body** workhorse.

| Style direction | Display font | Body font | Feels |
|---|---|---|---|
| Editorial / premium | Serif (e.g. a high-contrast or elegant serif) | Neutral sans | Ghost, Notion, Stripe |
| Modern tech / clean | Geometric or grotesque sans | Same family (variable) | Linear, Vercel |
| Bold / expressive | Heavy display (tight tracking) | Simple sans | Ramp, Nike |
| Playful / friendly | Rounded or distinctive display | Humanist sans | Gumroad, ClickUp |

Rules:
- **1 display + 1 body.** Two is plenty. Adding a third family is a smell.
- If you must use one family, use **weight + size contrast** instead of a second family.
- Mono font = optional third accent (for code, eyebrows, labels, technical data) — use
  sparingly and deliberately (e.g. Sanity's technical eyebrows).

## Type scale

A **modular scale** keeps hierarchy coherent. Base body at 16-18px.

```
Step         Size        Usage
display      60-80+px    Hero headline (min 10:1 vs body is dramatic; 6-8:1 is safe)
h1           44-56px     Page headline
h2           32-40px     Section headline
h3           24-28px     Sub-headline / card title
body         16-18px     Paragraphs
small        13-14px     Captions, meta, footnotes
label        ~12px +     Eyebrows, buttons, tabs (often UPPERCASE + letterspacing)
             letterspacing
```

- Use **`clamp()`** for fluid type: `font-size: clamp(2.5rem, 1rem + 4vw, 4rem)`.
- Keep the *ratio* consistent (e.g. 1.25 minor third, or 1.333 major third).

## The three measures that beat typeface choice

1. **Body size 16-18px** — anything smaller hurts readability for most audiences.
2. **Measure 45-75 characters** per line (66 optimal) → `max-width: 65ch` for body text.
3. **Line-height**: body 1.5-1.7, headings 1.1-1.25 (tight display = confident).

## Hierarchy via combined levers

Combining too many levers makes everything loud. Pick **one dominant lever** per level:

- Size (bigger = more important)
- Weight (heavier = more important)
- Color/contrast (darker/brighter = more important)

Example: hero = **size**; section title = **weight + size**; body = none of these. Save
*all three* (large + bold + high-contrast) for the single most important element on the page.

## Font loading (performance)

- Variable fonts where possible (1 file, many weights).
- Target **< 200KB** total font payload.
- `WOFF2`, `preload` the critical face, `font-display: swap`.
- Self-host or use a fast CDN; avoid five separate font files.

## How to read a type system (for analysis)

- What is the **pairing** (display voice vs body workhorse)?
- What is the **scale relationship** (display:body ratio)?
- What are the **measures** (measure, line-height, body size)?
- How is hierarchy achieved (which lever)?
- Is there a mono accent, and where is it used?

## Anti-patterns (never copy)

- More than 2-3 families on one page.
- Body text below 15px for paragraphs.
- Headline tracking so tight it breaks legibility at small sizes.
- All-caps everywhere (loses its emphasis value).
- Fancy display font for body copy (unreadable).
