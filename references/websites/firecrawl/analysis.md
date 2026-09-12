# Firecrawl — Design Analysis

> Source: `https://www.firecrawl.dev/` (web-scraping API for LLMs and agents) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/` at 462k chars, `/pricing`, `/about`, `/developer-index` with 13 menus, `/blog` at 1M chars)

Firecrawl is ember-on-paper: warm `#f9f9f9` grounds, ink `#262626` (14.37 AAA), one ember orange (`#ff4c00`, AA-large-only at 3.16) glowing through display-p3 inset shadows, Suisse International voice with GeistMono code, and 50%-round agent badges (Claude, Cursor, Windsurf, OpenAI, Gemini) as social proof. "Setup for agents" sits beside "Start scraping" — the dual-audience CTA in four words.

## 1. Visual Theme & Atmosphere

- Mood: forge with daylight — light, warm, orange-hot actions, spinning 32s ambient reverse-spin somewhere in the machinery.
- Philosophy: the scraper that shows its work — developer-index page, 1M-char blog, agent badges; depth is the moat.
- Single-hairline world: every border on the site is `#ededed` in some width/edge — unity through one grey.

## 2. Color Palette & Roles

- Grounds: `#f9f9f9` + `#ffffff` + `#efefef`; ink `#262626` (15.13 AAA on white) + `#606060` (5.97 AA) + `#747474` (4.67 AA).
- Ember: `#ff4c00`/`#ff5500` (hover `#d94100`) — AA-large-only on paper (3.16): buttons and large display only, honestly constrained.
- Hairline: `#ededed` everywhere (11 border combos, one color) + `#c2c2c2` decorative (fails 1.69) + black 6% washes.
- Ring blue `#3b82f6` focus only — accessibility without brand cost.

## 3. Typography Rules

- Voice: Suisse Int'l 450/500/700, 60→10px — neo-grotesque neutrality with a 450-weight text grade most sites skip.
- Code: GeistMono 450/500, 32→10px — mono at 32px for display-code moments.
- Decision: 450-weight grades soften the grotesque without going geometric. Borrow for infra that wants warmth without roundness.

## 4. Component Stylings

- Primary: ember 10/8px buttons with display-p3 orange glow shadows (inset + drop layered) — the button looks hot.
- Secondary: 4–6% black ghost squares + white bordered 10px cards — quiet chrome around the fire.
- Agent badges: 50%-round logos (Claude, Cursor, Windsurf, OpenAI, Gemini) — compatibility as jewelry.
- Links: orange-underlined + ink/ghost hierarchy, all hovers to white-token (dark-zone convention).
- Inputs: unstyled text + 8px buttons — forms defer to the API (signup happens in product).
- Logo: 600px inline SVG `#262626` + png/ico favicons + og-image.

## 5. Layout Principles

- 8px scale (1/2/4/6/8/10/12/15/16/20/24/28/32/40/44px) with 44px CTA air — compact confidence, dense 12–16px API core.
- Funnel: ember hero with agent badges → scrape proof → developer-index depth → pricing → about → 1M-char blog.
- 11 breakpoints (1279→389, paired 1200/1199–575/576 stops) — the most granular responsive ladder in the repo.

## 6. Depth & Elevation

- Ember glow system (orange display-p3 insets + layered 2–4% card drops up to 40px) — heat as elevation; hot things rise.
- Decision: glow reserved for ember actions and hero cards — warmth means interactivity.

## 7. Do's and Don'ts

- Do: AAA ink pairs; ember large/button-only discipline; single-hairline unity; agent-badge jewelry; glow-as-heat; 11-step responsive ladder.
- Do: keep `#c2c2c2`/`#b5b5b5` decorative (both fail); keep spin-reverse ambient (32s, never competing).
- Don't: add accent colors (ember + ring-blue-focus is the budget); don't outline what glow can heat; don't slow 0.05–0.2s micro-motion — scraping is fast, the page must feel it.

## 8. Responsive Behavior

- 11-step ladder with paired stops (996/995, 768/767, 600/576/575) — breakpoint pairs suggest container-aware tuning, not just viewport collapse.
- Touch: 8px+ ghost buttons need 44px targets on mobile — verify before borrowing densities.

## 9. Agent Prompt Guide

- Quick reference: `ai / ember-light / product-funnel / light / high complexity / dual CTA (setup for agents + start scraping)`.
- Ready-to-use prompt: "Design a scraping-API page in the Firecrawl logic: warm paper grounds with AAA ink text, one ember orange used only for large text and glowing buttons, single-grey hairline unity, Suisse-style grotesque with 450-weight grades plus mono for code, round agent-compatibility badges as jewelry, ember-glow shadows where hot means interactive, developer-index depth with a million-char blog behind it, sub-0.2s micro-motion with one slow ambient spin, and an 11-step responsive ladder. Sell speed by feeling fast."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Ember hero + agent badges — dual-audience statement.
2. Scrape-proof bands — live capability demo.
3. Developer-index (13 menus) — evaluation depth.
4. Pricing (`/pricing`, 5 menus) — packaging transparency.
5. About (`/about`) — team legitimacy.
6. Blog (1M chars) — depth moat, SEO engine.

### 11. Pattern Position

- Fits the AI-infra pattern: ignite (ember) → badge (compatibility) → prove (live scrape) → deepen (index, blog) → package (pricing). Against Context.dev (rainbow maximalism) and Context7 (stone calm), Firecrawl is warm minimalism — three temperaments, one category, complete study.
- Page-flow logic: assume the buyer compares three scrapers in one afternoon; badges + live proof must win in 60 seconds.

### 12. Synthesis Notes

- Unique (borrow as logic): ember-glow shadow system; single-hairline unity; 450-weight type grades; agent-badge jewelry; paired-breakpoint ladder; developer-index as evaluation surface; million-char blog as moat; dual-audience CTA pairing.
- Combine with: Context.dev's agent-prompt CTA (Firecrawl's "Setup for agents" is a link — a copy-prompt would convert harder) and SaaS pricing transparency for packaging.
- Avoid: copying ember + Suisse + hairlines verbatim (reads "Firecrawl clone"); ember small text; grey decorative text as content; slow motion — speed is the brand promise.
