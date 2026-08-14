# AI Product Pattern

AI products sell a promise that feels like magic and needs proof that it isn't. The winning
pattern **shows the AI doing the work** (live, honest, useful), **sets expectations for
quality**, and **demystifies the black box** enough that users trust it with real work.

## When to use

- An AI-powered tool or feature (chat, generation, automation, analysis).
- The differentiator is intelligence, not UI chrome.
- Goal: make the AI feel *real and useful* — not hype — then get signup.

## Canonical section order

```
1. Navbar (logo · links · CTA)
2. Hero — headline + live product in action (demo/UI)
3. "What is it" line — one sentence, honest about what it does
4. Live demo / product deep-dive (the proof section)
5. How it works (steps, inputs → outputs)
6. Use cases (by role or job, not generic)
7. Quality & guardrails (accuracy, privacy, controls)
8. Testimonials (specific outcomes)
9. Pricing (usage-based if it is)
10. FAQ (data, accuracy, limits)
11. CTA band
12. Footer
```

## What makes this pattern work

- **The demo is the hero.** Show the AI doing real work with real (not cherry-picked) input.
  A live interactive playground or an animated mock output beats a screenshot of an answer.
  The best demos let the visitor *try* it in the hero.
- **Honesty is the brand.** Set expectations: what it's great at, what it can't do, when it
  needs a human. Overclaiming ("unlimited", "perfect") is instantly disbelieved — and
  compliance-sensitive.
- **Concrete outcomes, not vibes:** "Saves 3 hours/week per analyst" — anchor the magic to a
  metric. Pair AI promises with the `stats` component.
- **Guardrails reassure:** privacy ("your data isn't used for training"), controls
  ("human-in-the-loop"), audit/versioning — the AI buyer's real objections live here,
  often in the FAQ and a dedicated "trust/security" section.
- **Explain the inputs → outputs.** "Upload your docs → ask questions → get cited answers"
  demystifies the black box and makes the tool feel usable.

## Design language for AI

- **Tone:** capable and confident, *not* mystical. Avoid "the future is here" copy — it
  ages badly and reads as hype.
- **Palette:** dark-first is common (feels high-tech) but a light/editorial treatment can
  be a strong differentiator. Avoid the default "AI purple-blue gradient on everything".
  One accent, used on the interactive elements (see `color-systems.md`).
- **Visuals:** product UI, input/output pairs, before-after, annotation. Typography carries
  the intelligence — big display type + mono for technical/labels (see `typography-systems.md`).
- **Motion:** the demo can animate (typing, generation, cursor), but keep it 1.5-2x slower
  than feels natural and respect reduced motion.

## Differentiation moves (to avoid the samey AI look)

1. **Skip the purple gradient** — a distinct primary (green, orange, ink) instantly sets you
   apart from the AI-copy crowd.
2. **Lead with a real output artifact** — a generated chart, a summary card, a code diff —
   instead of a floating orb animation.
3. **Editorial/light over dark-tech** — a serif display with a calm white canvas reads
   premium and different.
4. **Show limitations in the hero** ("Best for X; not for Y") — radical honesty is a brand.
5. **Demo-first layout** — a two-pane "input → output" composition instead of centered text.

## Trust, privacy & compliance (mandatory consideration)

- AI content needs a **data/privacy answer**: is data used for training? Where does it go?
  (A "Security" or "Trust" section + FAQ entry.)
- Show **human controls**: edit, regenerate, approve, cite sources. Users want agency over
  AI output.
- Be accurate about **hallucination risk** and disclaim accordingly; don't present the
  product as infallible.
- Accessibility of AI output: generated content must still meet contrast/readability and be
  real text (not rasterized images).

## Responsive

- Two-pane demos stack; the input/output stays legible at mobile (annotate generously).
- Interactive playground needs touch support; keep primary CTA reachable above the fold.

## Anti-patterns (never copy)

- Floating purple orbs + "AI" in a gradient + "The future is here" — the exhausted template.
- A screenshot of a single, obviously-cherry-picked answer with no input shown.
- Claiming "100% accurate" or "unlimited" — instant distrust.
- No privacy/data answer anywhere on the page.
- Demo that doesn't work without JS (a blank box is worse than no demo).
- "Chat interface" as the entire product story with no explanation of what it does for the
  user's job.