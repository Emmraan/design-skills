# Vercel — Design Analysis

> Source: `https://vercel.com/` (frontend cloud / deploy platform) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/` 257k + `/pricing` 266k + `/about` 235k + `/enterprise` 279k + `/startups` 308k chars)

Vercel is monochrome confidence with one blue: ink (`#171717`) on paper (`#fafafa`, 17.18 AAA) alternating with white-on-black bands (17.94 AAA), a single product blue (`#0070F3`), GeistSans voice + Geist Mono signal, and a lifecycle color language (ship coral, preview magenta, develop blue, console purple/pink/blue). Against Neon's mint warmth, Coolify's amber populism, and Dokploy's zinc severity, this is the disciplined pole of developer-tools — the deploy funnel reduced to black, white, and one blue.

## 1. Visual Theme & Atmosphere

- Mood: precision-minimal deploy funnel — paper-white canvas, black enterprise bands, hairline dividers, zero decoration that is not a ring or a pill.
- Philosophy: the platform disappears so the deployment feels instant — color budget spent on meaning (lifecycle states, focus rings), not on backgrounds.
- Manifest declares black (`#000000` theme/bg), rendered reality is dual: light marketing canvas + black product bands. Brand dark, funnel dual.

## 2. Color Palette & Roles

- Grounds: paper `#fafafa` (98% area on light pages) + black `#000000` / ink `#0a0a0a` bands; hairlines `#ebebeb` on light, `rgba(0,0,0,0.08)` dividers.
- Ink scale: `#171717` body (17.18 AAA on paper) + `#4d4d4d` secondary (8.1 AAA) + `#7d7d7d` / `#8f8f8f` muted (large-only 3.1) — a four-step grey ladder, never a flat grey.
- Single accent: Vercel blue `#0070F3` (`--develop-text #0a72ef`, hover `#005fcf`) — links, primary signals, focus outer ring. Deliberately AA-large-only on light (4.36) and on black (3.94): blue is signal, never body text.
- Lifecycle language (CSS vars, the unique move): `--ship-text #ff5b4f` coral, `--preview-text #de1d8d` magenta, console purple `#7928ca` / pink `#eb367f` / blue `#3291ff` — deploy states get hues, marketing never does.
- Focus blue `#52a8ff` — accessible focus ring (`white 2px + #0072f5 4px` observed), the only glow in the system.

## 3. Typography Rules

- Voice: GeistSans 400/450/500, 64→11px — display 64px tight-tracked (`-3.84px`, line-height 1.0) stepping 64/56/48 for hero tiers, body 24/18/16/14/13 with relaxed 1.43–1.6 line-heights.
- Signal: Geist Mono 400/500/600, 18→11px — uppercase semibold 18px eyebrows, 16/14/12 code and labels. Mono marks the machine (commands, states, eyebrows); sans carries persuasion.
- Pairing logic: tight, large, light-weight sans display (400/450, not bold) for calm authority + mono uppercase for deploy credibility. Borrow the weight restraint — Vercel never shouts with 700+.
- Measure stays narrow on 24px ledes (`-0.96px` tracking); captions at 11–12px with 1.5–1.82 line-height stay legible.

## 4. Component Stylings

- Buttons (8 variants, two shapes): 6px squares for consideration (`Get a Demo` white/ink, `Sign Up` black/white, skip-link blue-text) vs 9999px pills for motion (`Deploy now` black/white, `Start a free trial`, `Start deploying`, `Read the blog` grey `#ededed`/ink). Pill = go, square = consider — same semantics as Neon, inverted palette.
- Inputs: light (`#ffffff`/`#171717`) and dark (`#0a0a0a`/`#ffffff`) search + text pairs with `0×12px` padding and `1px` grey-alpha focus bar; select dropdowns both themes with `36px` right chevron room and `var(--ds-focus-border)` focus shadow.
- Links: 6+ styles (white, `#0072f5` blue, ink, `#4d4d4d` muted, `#0a0a0a`, `#52a8ff` on dark) — color-shift on hover, 0.1/0.15s.
- Badges: subtle neutral pill (`#ffffff`/`#4d4d4d`, `0×12px`, 8px radius, 14px) — quiet metadata, never competing with CTAs.
- Favicon kit exhaustive (ico + 10 apple-touch sizes + 2 PWA + distinct og/twitter social images) — share-image discipline.

## 5. Layout Principles

- 8px scale (1/2/5/6/8/9/12/16/18/24/32/40/56/96/120px) — micro 1/2px hairline steps plus macro 96/120px section air. Rhythm: dense UI (2/6/12/16px) inside airy sections (56/96/120px).
- Funnel: black-and-white hero with dual CTA (Deploy + Demo) → logo carousel → lifecycle/state bands → feature + code bands → audience splits (`/enterprise`, `/startups`) → pricing → footer sitemap.
- 5-page crawl shows audience segmentation as pages, not tabs — enterprise and startups get full narratives, pricing stays separate for evaluation.

## 6. Depth & Elevation

- Ring shadows, not drop shadows: `1px` rings (`#ebebeb`, `rgba(0,0,0,0.08)`, `#2e2e2e` on dark) etch surfaces; the only layered shadow is the subtle CTA lift (`0.08 ring + 2px 4% + paper 1px`).
- Decision: monochrome floats on rings, blue floats on focus — elevation means interactivity (focus ring) or containment (hairline), never decoration.
- 7 linear + 1 radial gradients observed but visually restrained — ambient staging behind mono surfaces, not color storytelling.

## 7. Do's and Don'ts

- Do: AAA ink-on-paper and white-on-black body pairs; one-blue discipline; pill/go vs square/consider semantics; lifecycle hues confined to state contexts; mono for machine voice; 96/120px section air; dual-theme inputs.
- Do: keep blue large-or-interactive (4.36/3.94 fail body use — correctly never body); keep `#8f8f8f`-class muted greys large or on dark; keep decorative dark greys (`#454545`/`#292929` on black, 2.19/1.44) decorative only.
- Don't: add a second marketing accent (the lifecycle hues are state, not brand); don't bold the display (450 carries it); don't lift cards with soft shadows — ring them.

## 8. Responsive Behavior

- 23 breakpoints (2300→370px) — the widest ladder in the repo: ultra-wide 2300/1200/1080 stops plus dense mobile 500/480/470/440/400/380/370. Designs from cinema to small phone without reflow jumps.
- Collapse strategy: Tailwind arbitrary values + Headless UI — fluid type (64→48→56 tiers collapse), pills stay thumb-sized, mega-menus (3 revealed per page) collapse to disclosure.
- Touch: pill CTAs (`0×12px`, 14–16px type) are naturally 44px+ targets; hairline tables must scroll, not squash.

## 9. Agent Prompt Guide

- Quick reference: `developer-tools / mono-minimal / product-funnel / dual / high complexity / dual CTA (Deploy now + Get a Demo)`.
- Ready-to-use prompt: "Design a deploy-platform page in the Vercel logic: paper-white canvas with black product bands, ink four-step grey ladder with AAA body pairs, one product blue reserved for links and focus rings, lifecycle accent hues confined to ship/preview/develop states, Geist-style tight-tracked light-weight sans display plus uppercase mono eyebrows and code, pill CTAs for go and 6px squares for consider, ring-etched surfaces with no decorative shadows, 96–120px section air on an 8px scale, and a 23-stop responsive ladder from ultra-wide to small phone. Sell speed by removing color, never by adding it."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Dual-CTA hero (Deploy pill + Demo square) — commitment split above the fold.
2. Logo carousel (16s ambient) — social proof as motion, not grid.
3. Lifecycle/state bands (ship/preview/develop hues) — deploy narrative in color.
4. Feature + code bands (mono blocks, hairline system) — show, don't tell.
5. Audience pages (`/enterprise`, `/startups`) — segmentation as full narratives.
6. Pricing page — evaluation depth kept off the homepage.
7. About page — company trust close.
8. Footer sitemap — docs-depth close.

### 11. Pattern Position

- Fits the deploy-funnel pattern: hero split → ambient proof (carousel) → state storytelling (lifecycle) → code proof → audience split → pricing → docs. Against Dokploy's landing-as-dashboard density and Neon's capture-first email pill, Vercel's funnel is the most segmented — each audience gets a page, each deploy state gets a color.
- Page-flow logic: assume the developer chooses emotionally (speed, taste) and justifies with deployment semantics; monochrome handles taste, lifecycle hues + mono handle justification.

### 12. Synthesis Notes

- Unique (borrow as logic): single-blue discipline on monochrome; lifecycle color language (ship/preview/develop/console hues as state, not brand); pill/go vs square/consider button semantics; tight-tracked light-weight display (450, not bold); ring-etched depth; 23-stop responsive ladder; audience-as-pages segmentation; galaxy-pulse + logo-carousel ambient motion pair.
- Combine with: Neon's email-pill capture for newsletter depth (Vercel has no inline capture component) and Dokploy's mega-nav for capability density (Vercel reveals 3 menus — depth is there but quieter).
- Avoid: copying black-white-plus-`#0070F3` verbatim (reads "Vercel clone"); blue body text (fails AA); a second marketing accent; bold display type; soft-shadow cards — rings are the whole point.
