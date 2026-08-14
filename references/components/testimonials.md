# Testimonials

Testimonials are the most powerful persuasion tool on a page because they are **someone
else's voice**, not yours. Their job is to feel real, specific, and quietly confident —
not like a wall of advertorials.

## The job (what it must do)

1. **Sell through other people** — the customer's words, not the company's claims.
2. **Be specific** — a concrete outcome ("cut reporting from a day to an hour") beats praise
   ("amazing product").
3. **Match the visitor's identity** — show users like the visitor (role, company size,
   industry) so they self-select.
4. **Add credibility** — real names, roles, companies, and photos/logos where honest.

## Anatomy of a good quote

```
"Replaced our entire spreadsheet stack. Month-end now takes 2 hours, not 3 days."
                                                              — Priya S., Head of Ops, Acme
```

- **Specific outcome** > generic adjective. Any number/measure/tool name you can swap in
  makes it believable.
- **Speaker attribution** — name + role + company. A photo and/or company logo adds weight.
- **Short** — 1-2 sentences. Long testimonials get truncated and lose punch.
- **Voice consistency** — quotes should sound like customers, with imperfect phrasing,
  contractions, and the occasional em-dash. Too-perfect quotes read as fabricated.

## Layout directions

| Direction | Structure | Best for |
|---|---|---|
| Single featured quote | One large pull-quote, big type | Editorial confidence |
| 3-up card grid | 3-6 cards with quote + attribution | Balanced, standard |
| Carousel | One quote at a time, arrows/dots | When space is tight (mobile) |
| Logo-wall + quotes | Company logos, hover/scroll reveals quotes | Enterprise/B2B credibility |
| Video thumbnails | Play buttons over faces | High-trust (testimonials with faces) |
| Two-column magazine | Long-form editorial quotes, big pull | Premium brands |

## Design decision logic

- **The quote is the loudest text** (h3-ish or larger, strong contrast). The attribution is
  small and muted. Rating stars (if any) sit above, quiet.
- **Real attribution with a real name** beats anonymous ("— Happy Customer"). If you can't
  show a name, it's a weak quote.
- **Star ratings:** only use for B2C/consumer contexts where reviews are expected; B2B pages
  prefer narrative quotes.
- **Avoid gradients/decoration behind quotes** — this section should feel *understated* and
  truthful. Clean cards or a simple band reads most authentic.
- **Quotation-mark styling** (a large serif `"`) is a small identity moment — one accent,
  not a pattern of ornaments.

## Social proof combos (stacking)

- Pair with **stats** ("4.9/5 from 2,300 reviews") and **logo-cloud** (see `logo-cloud.md`)
  for a trust sandwich: logos → featured quote → stat strip.
- Interleave one testimonial after each feature row for "proof as you go" instead of one big
  testimonial wall.

## Responsive

- Grid stacks to 1 column; carousels become swipeable (touch-friendly arrows at ≥44px).
- Pull-quote type scales with `clamp()` — never let a long quote overflow its container.

## Accessibility

- Use blockquote markup; quote text must pass AA contrast even when muted.
- Carousels: arrow buttons with accessible names, dot indicators with `aria-current`,
  keyboard control, and no auto-advance that traps users (see `navigation.md`).
- Attribution is real text (not an image of text).
- Avoid auto-rotating quotes — let the user control pace.

## Anti-patterns (never copy)

- Perfect, sterile quotes that all sound like the marketing team wrote them.
- Anonymized attribution ("Verified user" with no name).
- 20 stacked testimonials — it becomes noise; pick your 3-6 best.
- Quotes with no outcome ("It's great, I love it").
- Fake logos or real logos the company doesn't actually work with (reputation risk).
- Auto-rotating carousel with no pause — users get motion sickness, not trust.