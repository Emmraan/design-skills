# FAQ

The FAQ exists to kill the last objections between the visitor and the CTA. Good FAQs feel
like a real conversation; bad ones read as legal disclaimers. It is a trust section, not a
documentation dump.

## The job (what it must do)

1. **Answer real questions** — the ones that come up right before purchase/signup, not
   support tickets.
2. **Defuse friction** — pricing, data, migration, trial, "is it for me?", refunds.
3. **Keep the user on the page** — a link to full docs is fine, but the answer lives here.
4. **Get asked less later** — this is also onboarding content in disguise.

## Writing the questions

- Use the **user's words**, not your terminology: "Can I import my existing data?" not
  "Does the platform support ETL ingestion?"
- Typical buckets for SaaS/product pages:
  - Trial & commitment ("Is there a free trial? Do I need a credit card? Can I cancel?")
  - Migration & data ("Can I import from X? Is my data exportable?")
  - Fit & limits ("How many seats/rows/workspaces? Is it for teams my size?")
  - Security & compliance ("Where is data stored? SOC 2? GDPR?")
  - Support & billing ("How does invoicing work? What support do I get?")
- **Answer-first framing:** open with the answer, then the nuance. "Yes — data is
  exportable anytime as CSV or JSON."
- 4-8 questions is the sweet spot. More than ~10 means you're hiding something elsewhere on
  the page.

## Layout directions

| Direction | Structure | Best for |
|---|---|---|
| Accordion | Collapsible rows (one open at a time) | Most SaaS pages |
| Two-column list | Q left, A right (no collapse) | Short, snappy answers |
| Single-column plain | Q + A stacked, no interactivity | Editorial, calm, a11y-simple |
| Sticky group | Category headings with items under them | Many questions (developer tools) |

## Interaction (accordion)

- First item **open by default** — signals interactivity and sets the tone.
- Only one open at a time (or allow multiple — pick one and be consistent).
- Toggle is a real `<button>` (not a heading with a click handler), `aria-expanded`,
  keyboard-openable, and the row is a full-width tap target (see `interaction-patterns/forms.md`
  for disclosure patterns; `modals.md` for focus conventions).
- Smooth height animation on open/close, but content must remain reachable with reduced
  motion.

## Design decision logic

- Section header mirrors the page rhythm: eyebrow ("Questions"), h2 ("Frequently asked"),
  short intro line (optional).
- Rows separated by hairlines (top/bottom borders) rather than heavy cards — reads as a
  list, not a wall.
- The icon (chevron/plus) is quiet; the **question text** carries the weight. When open, the
  question can go bolder or accent-colored.
- Answer text is body-size, muted, `max-width` ~60-70ch for readability.
- **CTA echo** under the FAQ ("Still have questions? → Contact/Book a call") closes the loop
  for anyone not fully convinced.

## Accessibility

- Use a `<details>`/`<summary>` native disclosure OR a properly implemented accordion —
  never both mixed. Native `<details>` gives keyboard + semantics free.
- Don't rely on the open-state color to convey "expanded".
- Content under a collapsed accordion is genuinely hidden to AT — that's fine, the question
  text is the accessible summary.

## Anti-patterns (never copy)

- Questions nobody asked ("What is a workspace?") — filler.
- Answers that are marketing ("Our industry-leading platform…") instead of facts.
- 30 collapsed rows of legal text.
- Accordion that collapses other items when you open one but is slower than scroll.
- FAQ buried at the very bottom with no CTA — the objections you just answered go nowhere.
- Icons-only expand indicators (no accessible name).