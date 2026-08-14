# Collection: Ecommerce

Ecommerce design is product-first: the merchandise is the hero, and the UI is quiet chrome
that makes it irresistible and instantly buyable. This collection maps the repo's
commerce-adjacent references and the conversion mechanics that make them work.

## Category definition

Selling physical goods, digital products, or subscriptions with a checkout. The page must
move interest → cart → checkout. See `patterns/ecommerce.md` for assembly.

## Repo references (analyzed in `references/websites/`)

| Site | Slug | What to borrow as logic |
|---|---|---|
| Gumroad | `gumroad` | Creator commerce: selling digital goods with personality and minimal friction |

Gumroad is the seed commerce reference; pair it with **retail/consumer references from the
external galleries** below, since most of the repo's seed sites are SaaS/fintech. When
synthesizing, borrow *photo-forward product storytelling* from retail galleries and
*friction-removal mechanics* from SaaS pages.

## External galleries (inspiration, not sources to replicate)

- Godly / Land-book (filter: ecommerce, stores)
- Webflow Ecommerce Showcase — real store builds
- Awwwards "Shop" tag — high-craft storefronts
- DTC brand sites (subscription & direct-to-consumer) — hero campaigns, product shots

> Rule: the brand often lives in the *photography art direction*, not the UI. Consistent
> product shots are a design system too.

## What to retrieve together

- Pattern: `patterns/ecommerce.md`
- Components: `hero.md`, `features.md` (product deep-dive), `testimonials.md`, `cta.md`,
  `navbar.md` (search + cart)
- Interaction: `feedback-loading.md` (add-to-cart feedback), `forms.md` (checkout)
- Tokens: `color-systems.md`, `grid.md`

## Synthesis guidance

- The image is the pitch: multiple angles, zoom, lifestyle context; keep the UI neutral so
  product colors read true.
- Keep the buy box visible (price, variants, add-to-cart) without scrolling.
- Be explicit about shipping, returns, and payments — friction killers convert.
- Use honest urgency only (real stock/shipping info), never fake countdowns.