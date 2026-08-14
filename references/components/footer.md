# Footer

The footer is the last thing users see — it's where they go to confirm the site is real,
find answers, and reach a human. It's also the least glamorous section, which is exactly
why good design makes it feel finished and trustworthy rather than forgotten.

## The job (what it must do)

1. **Finish the page with composure** — a footer that matches the design language signals
   the site is complete, not abandoned.
2. **Provide escape routes** — sitemap, contact, docs, legal, social.
3. **Build trust** — company info, status page, security badges, copyright.
4. **Convert late-scrollers** — a small CTA or newsletter can live at the top edge of the
   footer.

## Anatomy (typical)

```
    [Newsletter / CTA band (optional)]
[Logo + about] [Product] [Company] [Resources] [Legal]  ← 3-4 columns
[© 2026 Name] [Made in X]  [Status]  [Twitter · LinkedIn · GitHub]  ← bottom bar
```

- **Brand column:** logo + one line about the company (optional; not always needed).
- **Link columns:** 3-4 columns × 5-8 links each max. Label the columns clearly
  ("Product", "Company", "Resources", "Legal").
- **Bottom bar:** copyright, legal links (Privacy/Terms), and social icons. Keep it calm —
  it's a baseline, not a decoration zone.

## Link ordering

- Primary product paths first (Pricing, Features, Docs).
- Legal links (Privacy, Terms, Cookie, Licenses) — near-universal bottom-right.
- Social icons: only the platforms you're genuinely active on.

## Design decision logic

- **Visual weight:** quieter than the body — muted text, hairlines, smaller type. The footer
  is a background support; the CTA and content above own the page.
- **Top edge:** many sites add a footer CTA band ("Ready to start? → Get started free")
  — the strongest late-stage conversion slot on the page (see `cta.md`).
- **Background:** same surface as the body (hairline border above) or a slightly darker/tonal
  band for a clean close. Full-black footers are fine on dark themes; on light themes a
  dark footer is a deliberate "end" moment — pick one and commit.
- **Column headers:** small, uppercase + letterspacing or medium-weight title case. Muted.
- **Links:** body size, hover with the accent color. Underlines only on hover (or none).
- **Misc:** a status/sustainability/security line ("All systems operational", badges) adds
  trust. Big "brand footer" art (oversized wordmark) is a designer's touch — use sparingly;
  it can feel like filler.

## Newsletter

- Place it in the footer CTA band or brand column. Single email field + button
  (see `forms.md` for the single-field pattern).
- State the payoff ("Product updates, twice a month. No spam.").
- Provide an unsubscribe promise and working validation feedback.

## Accessibility

- Use `<footer>` semantics; link columns can be `<nav aria-label="Footer">` or plain lists.
- Real links everywhere — no `href="#"` placeholders.
- Social icons need accessible names (`aria-label="Twitter"`).
- Contrast: muted footer text still ≥4.5:1; don't dim it to illegibility.

## Responsive

- Columns collapse to 2×2 (then 1) with generous tap targets (≥44px rows).
- Newsletter field + button stack or stay side-by-side depending on width.
- Bottom bar wraps; center it on mobile, keep it aligned on desktop.

## Anti-patterns (never copy)

- A footer that looks untouched (plain black box with white 12px text — an afterthought).
- 8 columns of links nobody organized.
- Missing legal links, or copyrights that are years out of date.
- Newsletter field with no validation and no payoff.
- Social icons for platforms the company abandoned in 2022.
- Footer so visually loud it upstages the rest of the page.