# Collection: Education

Education design sells **outcomes through discovery** — learners arrive with a goal,
not brand loyalty. The page must make search effortless, prove quality with ratings
and completions, and turn browsing into enrolling. This collection maps the repo's
education references.

## Category definition

Course marketplaces, cohort learning, tutoring, and learning benefits (business).
Goal: search → trust (ratings, instructors, outcomes) → enroll / subscribe. Catalog
density is the product — the UI is quiet chrome around it.

## Repo references (analyzed in `references/websites/`)

| Site | Slug | What to borrow as logic |
|---|---|---|
| Udemy | `udemy` | Search-led marketplace; one action color; fixed-hierarchy course cards; tint-band campaigns |

Udemy is the seed education reference; pair it with **SaaS proof patterns** (pricing
transparency, outcome stats) for buyer-facing business bands and with editorial
references (Ghost) for instructor storytelling and long-form learning content.

## External galleries (inspiration, not sources to replicate)

- Webflow Education Showcase — real course-site builds
- Godly / Land-book (filter: education, courses)
- Awwwards "Education" tag — high-craft learning experiences
- Cohort/DTC learning brands — outcome-led hero campaigns, curriculum presentation

> Rule: the catalog is the pitch — fixed card hierarchy repeated at scale beats
> bespoke section design. Ratings are the trust currency; show them everywhere.

## What to retrieve together

- Pattern: `patterns/saas-landing.md` (skeleton: hero → proof → features → pricing → CTA)
- Components: `hero.md` (search-led), `features.md`, `testimonials.md` (learner outcomes), `pricing.md`, `cta.md`, `footer.md`
- Tokens: `color-systems.md` (single-accent marketplaces), `typography-systems.md` (single-family weight grades), `spacing-scale.md`
- A11y: `semantics-aria.md` (search labels, rating announcements, form contrast)

## Synthesis guidance

- Lead with search in the hero (statement + autocomplete), follow with catalog carousels.
- Fix the card hierarchy once (image → title → instructor → rating → price) and repeat it everywhere.
- Categorize campaigns with flat tint bands and AAA text — never gradient promos.
- Prove twice: star ratings for learners, completion/outcome stats for buyers — separate bands, one language.
