# Portfolio / Agency Pattern

Portfolio and agency pages sell **craft and trust in people** — the work is the proof, and
the design must make the work look its best while convincing the visitor this team gets it.
The winning pattern is **the work first, the team close behind**, with a point of view that
says "we think about design this way".

## When to use

- Freelancers, design studios, dev agencies, creative firms, individual portfolios.
- Selling services, not a product.
- Goal: demonstrate craft → build affinity → get contacted (a meeting, an inquiry).

## Canonical section order

```
1. Navbar (logo · work · about · services · contact)
2. Hero — "who we are + what we believe" in one line (point of view)
3. Featured work (selected projects, best first — imagery-led)
4. Work grid (portfolio: thumbnails → case studies)
5. Services / capabilities (what you do for clients)
6. Process (how you work — de-risks the engagement)
7. Clients / logo cloud (who trusts you)
8. Testimonials (client voices, specific outcomes)
9. About / team (faces + humanity)
10. Blog / insights (optional — expertise proof)
11. Contact / CTA ("Let's work together" + form/email)
12. Footer
```

The portfolio is *intentionally* front-loaded: work at the top, contact at the bottom, with
proof in between.

## What makes this pattern work

- **The work is the hero.** Large, high-quality project imagery drives the entire page.
  Crop tight, let thumbnails whisper the idea, and let each case study tell a story
  (problem → approach → outcome → role).
- **A point of view beats a tagline.** "We make calm software for loud problems" tells a
  visitor what you're like; "We are a full-service agency" tells them nothing.
- **The work grid is scannable** — thumbnail + title + 1-line result (or industry). A grid
  with no labels makes visitors click blindly.
- **Process de-risks hiring you:** a clear "how we work" (discovery → design → build →
  ship) tells clients you're organized and predictable.
- **People humanize the pitch:** team photos, real names, honest bios. Clients hire
  people, not portfolios.
- **Contact is the payoff:** a prominent, warm ask ("Tell us about your project") with a
  short form or email — never a dead-end footer.

## Case study anatomy (what makes a great one)

```
Cover: project title + one-line result (+ thumbnail)
Context: the client, the problem, the stakes
Role: what *you* did (your contribution, honestly)
Approach: decisions and why (design thinking, shown not told)
Outcome: metrics or received impact ("+40% conversion", awards)
Gallery: the work itself, well-cropped and credited
```

Case studies are where portfolios actually win work — invest depth here, not just covers.

## Design language for portfolios

- **Tone:** confident, personal, editorial. The design should demonstrate skill by being
  *distinct* — but never louder than the work.
- **Palette:** neutral, often light/editorial with a strong accent or a bold signature
  color; dark/immersive galleries let imagery pop (see `color-systems.md`).
- **Type:** editorial pairings shine — a strong serif display + humanist body, or an
  expressive display voice. Typography is where creative skill reads instantly
  (see `typography-systems.md`).
- **Layout:** asymmetric/editorial grids, generous margins, deliberate negative space —
  this is the one pattern where breaking the symmetric template is the *point*.
- **Motion:** parallax, reveal-on-scroll, and hover treatments on work — creative motion
  is expected, but keep content readable and respect reduced motion.

## Differentiation moves

1. **A singular portfolio voice** — curated, "we only show our best 6" over a 30-item grid.
2. **Niche focus** — "we design for climate tech" targets better than "we design for
   everyone".
3. **Interactive/immersive case studies** — scroll-driven storytelling, embedded
  prototypes, honest process notes.
4. **Radical specificity in results** — name the client, the metric, the win.
5. **Personal editorial** — a founder essay, a design philosophy page, a strong "about".

## Contact mechanics

- Make it **effortless**: email link + short form + maybe a calendly/booking line.
- State response time ("I reply within 48 hours") to set expectations.
- Offer a clear next step ("Book a 20-min intro call").
- Accessibility: the contact form follows `forms.md` (labels, inline errors, correct types).

## Accessibility

- Portfolio imagery: alt text describes the *work*, not the file ("Homepage redesign for a
  fintech startup — clean light UI with a green accent").
- Lightbox/zoom on work needs keyboard + ARIA support (see `modals.md`).
- Case-study galleries: keyboard navigation, pause on auto-advance, no motion dependence.
- Contrast AA across editorial type; don't let creative backgrounds eat the text.

## Responsive

- Grids reflow to 1-2 columns; galleries stack; case-study imagery must remain legible
  (use srcset).
- Editorial/parallax effects degrade gracefully to static on mobile.

## Anti-patterns (never copy)

- A generic template portfolio (matching hero, 6 identical squares, "Let's work together")
  — it says "I use templates".
- Repeating the client's entire brand rather than showing *your* hand in the work.
- Hiding the price/scope of engagement entirely ("Contact for pricing" with zero signal).
- A gallery with no context, no results, no role — pretty images with no persuasion.
- Stolen/other people's work in the portfolio.
- Contact buried in a footer with a form that doesn't work on mobile.