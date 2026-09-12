# Neon — Design Analysis

> Source: `https://neon.com/` (serverless Postgres) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 2 pages: `/` at 181k chars + `/blog/an-agent-provisions-a-neon-backend-a-human-claims-it-later` — crawl surfaced one blog page; homepage carries the design reference, blog the article system)

Neon is database-brand warmth on black: mint (`#e4f1eb`, black-on-it 18.08 AAA) as the primary surface, periwinkle (`#648dff`) and mint-green (`#34d59a`) accents, Inter + GeistMono, and a 60-second infinity scroll as ambient proof. Against Dokploy's zinc severity and Coolify's amber populism, this is the friendly pole of data infrastructure — Postgres that smiles.

## 1. Visual Theme & Atmosphere

- Mood: midnight data garden — black grounds, mint clearings, periwinkle signals, endless logo/customer scroll.
- Philosophy: infrastructure approachability — rounded everything (pills + 4px), warm mint instead of cold blue, blog that teaches agents (the captured post is literally about agent-provisioned backends).
- Manifest declares white `#FFFFFF`, rendered reality is black-first — brand light, product dark.

## 2. Color Palette & Roles

- Grounds: `#000000` + `#131415` (60% panel alpha) + hairline `#303236` family (borders, dividers, inputs, code).
- Primary surface: mint `#e4f1eb` — buttons (ink text 18.08 AAA) and bands; the warm alternative to white pills.
- Accents: periwinkle `#648dff` (links/signals) + mint-green `#34d59a` (hover `#2cb583`, black text) — decorative `#00e599`-on-white fails 1.66, correctly never used that way.
- Neutrals: `#94979e` (7.18 AAA on black, underline-muted links) + `#61646b` (AA-large) + `#494b50` code borders.
- Fails: grey-on-grey 1.36 decorative only.

## 3. Typography Rules

- Voice: Inter 500/600, 80→10px — display warmth at medium weights, never shouting.
- Code: GeistMono 500/600, 20→12px — connection strings and CLI live in mono.
- ESBuild_Medium bundled display face — build-tool provenance as brand texture. Borrow the voice/mono split for data products.

## 4. Component Stylings

- Buttons: height-driven pills (0×18/16/28px padding, 9999px) — white, mint, green; plus 4px bordered squares (12×16) for secondary actions. Pill = go, square = consider.
- Email capture: dark pill input (`#131415` 60%, `#303236` border, 48px right padding for the embedded submit) — newsletter-as-component.
- Links: 8 styles (white, muted-underlined, ink, periwinkle-grey) — underline marks the quiet links.
- Code/pre blocks share the `#303236` hairline system — docs credibility inline.
- Favicon kit complete (svg + ico + 3 apple sizes + PWA) + dated social previews.

## 5. Layout Principles

- 8px scale (1/2/6/8/10/12/16/18/20/24/25/28/32/80/160px) with 160px hero air — the airiest devtool in the repo.
- Funnel: black hero with email capture → mint proof bands → customer infinity scroll (60s) → features → blog depth → footer.
- 2 gradients only — color bands do the staging work gradients do elsewhere.

## 6. Depth & Elevation

- Ring shadows (white 5%, zinc inset) — etched, not lifted; flat black with glowing mint objects.
- Decision: mint floats, black recedes — one warm color carries all elevation meaning.

## 7. Do's and Don'ts

- Do: AAA white/mint-on-black pairs; mint-as-primary-surface; pill/go vs square/consider semantics; 60s ambient scroll; blog-as-teaching (agents included); 160px hero air.
- Do: keep `#00e599`-class brights off white (1.66 fail); keep muted greys large-or-dark.
- Don't: add accent colors (mint + periwinkle + green is the budget); don't shrink code below 12px; don't rush the ambient scroll.

## 8. Responsive Behavior

- 6 breakpoints (1919/1599/1279/1023/767/413px) — ultra-wide aware (1919/1599 stops are rare in this repo) down to 413px small-phone.
- Touch: height-driven pills are naturally thumb-sized; email pill must stay full-width on mobile.

## 9. Agent Prompt Guide

- Quick reference: `developer-tools / mint-dark / product-funnel / dark / high complexity / dual CTA (email capture + start building)`.
- Ready-to-use prompt: "Design a data-infrastructure page in the Neon logic: black grounds with AAA white text, mint as the primary button and band surface with ink text, periwinkle signal accents, Inter voice plus mono for code, height-driven pill CTAs with square secondaries, dark pill email capture, hairline code-block system, a 60-second customer infinity scroll, 160px hero air, and a 6-step responsive ladder from ultra-wide to small phone. Sell the database by feeling warm, never by looking simple."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Black hero + email pill — capture-first statement.
2. Mint proof bands — warm credibility zones.
3. Infinity scroll (60s) — social proof as ambience.
4. Feature + code bands — show, don't tell.
5. Blog article system (captured post) — teaching trust, agent-era topics.
6. Footer sitemap — depth close.

### 11. Pattern Position

- Fits the data-infra pattern: capture → warm (mint bands) → prove (scroll, code) → teach (blog) → build. Against PlanetScale-style cold blues (unseen here), Neon's mint warmth is the differentiator — the dev-tools set now spans zinc, amber, aurora, paper, and mint.
- Page-flow logic: assume the developer chooses Postgres emotionally (familiarity) and justifies technically; mint handles emotion, code blocks handle justification.

### 12. Synthesis Notes

- Unique (borrow as logic): mint-as-primary-surface; height-driven pill padding; email-pill capture component; infinity-scroll ambience; 160px hero air; ultra-wide breakpoints; manifest-light/rendered-dark split; agent-topic blog as trust.
- Combine with: Dokploy's mega-nav for capability depth (Neon's nav is quiet — depth would help evaluation) and Context7's ledger tables for pricing/packaging clarity.
- Avoid: copying black-mint + Inter verbatim (reads "Neon clone"); bright-green-on-white text; rushed ambient motion; cold-blue data clichés — mint is the whole point.
