# Coolify — Design Analysis

> Source: `https://coolify.io/` (open-source self-hostable deployment platform) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/pricing`, `/docs`, `/philosophy`, `/contributors`)

Coolify is self-hosting populism: near-black marketing (`#101010`) with an amber spark (`#fcd34d`) and violet depth (`#ad46ff`/`#6b16ed`), Inter throughout, Phosphor duotone icons, and a philosophy page as trust infrastructure. Caveat: `/docs` redirected into a separate docs app ("Jean Docs" manifest, violet `#6b16ed` theme, diff-token system) — its tokens are documented here but belong to the docs deployment, not the marketing system.

## 1. Visual Theme & Atmosphere

- Mood: homelab pride — dark, amber-lit, contributor faces on the wall, "own your stack" energy.
- Philosophy: open-source legitimacy — philosophy page + contributors page + transparent pricing do the persuading; the hero only needs to say "deploy anywhere."
- Two systems, honestly separated: marketing dark-amber vs docs-app violet — note the seam, don't blend them.

## 2. Color Palette & Roles

- Marketing: `#101010` ground + `#ffffff` text + amber `#fcd34d` primary (decorative-only on light — 1.44 fail, correctly confined to dark) + violet `#ad46ff` depth accent + `#ededed` secondary surfaces.
- Neutrals: `#202020` (70% alpha panels), `#242424` hairlines, `#a3a3a3` (fails on white 2.52 — dark-zone only), `#737373` (AA-large on `#f5f5f5`).
- Docs app (separate): violet `#6b16ed` (hover `#801aff`) + diff greens `#0ac864`/`#0eb464` + diff pinks `#c80a64`/`#e60a64` + idea-orange `#ef7e00` + Discord-blurple `#5865f2` community buttons.
- AAA anchors: ink-on-light 17.53, white-on-`#202020` 16.29, white-on-`#242424` 15.52.

## 3. Typography Rules

- Single family: Inter 500/600/700, 60px display → 12px captions — no display face, no mono; confidence through restraint.
- Phosphor Duotone icon font (24/20/16px) as the visual spice type can't provide.
- Decision: one neutral sans + rich icon layer — borrow when the product (not the page) should shine.

## 4. Component Stylings

- Buttons: small and quiet (6–8px padding, 12/8/6px radii) + quirky 9999px pills with 2px borders (ink 24%, blurple 32% with tinted glow shadows) — pills signal community/social, squares signal product.
- Cards: violet-tinted 1px borders (`#6b16ed` at 35%) + 4.8/12px radii + slideInUp 0.6s entrances.
- kbd elements share the bordered-chip language — CLI credibility in miniature.
- Links: 6 styles (white underlined, amber underlined, ink, blurple) — underline = external/emphasis convention.
- Logo: 48px launcher icon + full PWA set (48→512px) + safari mask + CDN og-image.

## 5. Layout Principles

- 8px scale (4/6/8/10/12/16/20/24/32/36/40/48/64/80/96px) with 96px hero air.
- Funnel: dark hero → self-host proof → pricing → philosophy → contributors wall → footer. Contributors as a page (not a section) is the open-source trust signature.
- 6 breakpoints (1280/1279/1024/768/767/640) — desktop-first collapse with explicit tablet stops.

## 6. Depth & Elevation

- Nearly flat: one sm ring-shadow + blurple glow pills + violet card borders — depth comes from color-on-dark, not elevation.
- Shimmer (`coolify-switcher-shimmer` 2.5s) on the switcher is the single "alive" surface.

## 7. Do's and Don'ts

- Do: AAA white-on-dark pairs; amber confined to dark; pill-vs-square button semantics; contributors-as-page; philosophy-as-trust; kbd styling for CLI.
- Do: keep amber and `#a3a3a3` off light grounds (both fail); keep docs-app violet out of marketing.
- Don't: add gradients-as-brand (one linear + one conic, both restrained); don't slow the 0.1–0.3s micro-motion; don't hide pricing — transparency is the moat.

## 8. Responsive Behavior

- 6-step ladder (1280→640) with explicit 1279/767 sub-stops — fine-tuned tablet behavior, not just mobile collapse.
- Touch: small-padding buttons need 44px targets on mobile — verify before borrowing densities.

## 9. Agent Prompt Guide

- Quick reference: `developer-tools / amber-dark / product-funnel / dark / medium complexity / dual CTA (self-host + pricing)`.
- Ready-to-use prompt: "Design an open-source devtool page in the Coolify logic: near-black grounds with AAA white text, one amber spark confined to dark surfaces, violet depth accents, single Inter family at medium-plus weights, Phosphor-style duotone icons as decoration, small quiet buttons with pill-vs-square semantics (pills for community, squares for product), violet-tinted cards with slide-up entrances, kbd-styled CLI hints, a contributors wall page and a philosophy page as trust infrastructure, and a 6-step responsive ladder. Convert on ownership, never on lock-in."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Dark amber hero — ownership statement.
2. Self-host proof bands — capability scan.
3. Pricing (`/pricing`) — transparency moat.
4. Philosophy (`/philosophy`) — values trust.
5. Contributors (`/contributors`) — community proof.
6. Docs app (separate deployment) — depth, violet system.

### 11. Pattern Position

- Fits the open-source-devtool pattern: own → prove (community) → believe (philosophy) → price → docs. Against Linear (proprietary polish), Taste Skill (skill install), Openship (infra drama), Coolify is self-host populism — the dev-tools set now covers four distinct postures.
- Page-flow logic: assume the developer fears vendor lock-in; every page answers "you keep the keys."

### 12. Synthesis Notes

- Unique (borrow as logic): contributors-as-dedicated-page; philosophy-as-trust-infrastructure; pill/square button semantics; kbd-as-credibility; amber-on-dark-only discipline; honest two-system split (marketing vs docs app).
- Combine with: Openship's ambient motion for launch drama (Coolify is statically confident — motion would add vitality) and Taste Skill's install-command hero for the conversion moment.
- Avoid: copying amber-dark + Inter verbatim (reads "Coolify clone"); amber body text on light; blending docs-app violet into marketing; hiding the community — faceless open-source doesn't convert.
