# Tavily — Design Analysis

> Source: `https://www.tavily.com/` (search API for AI agents) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 1 page — `www` resolves to `app.tavily.com/home`, no further pages discovered; single-page capture, token-rich at 70 text styles)

Tavily is a single-page instrument: cream (`#FFFCF6` manifest), ink `#3c3a39`, ember orange `#ff7300` primary, Suisse International (licensed .otf) with its Mono sibling, an 8-second aurora-flow hero, and a benchmark selector (tabs, prev/next, scroll) as the interactive proof. Links hover to `#3860BE` — the seventh site running with the web-wide trust-hover. One page, fully committed.

## 1. Visual Theme & Atmosphere

- Mood: warm laboratory instrument — cream paper, orange heat, pastel accents (periwinkle, peach, pink, sage, cyan), dark `#0b0907` zones for contrast.
- Philosophy: benchmarks are the marketing — "Select benchmark" tabs with scroll controls let engineers verify instead of believe.
- Single-page confidence: no pricing/about/blog crawl surface — the app home IS the landing.

## 2. Color Palette & Roles

- Grounds: cream `#fffcf6`/`#fefcf5` (ink-on-it 20.46 AAA) + dark `#0b0907` + `#1f1e1e`/`#101010`/`#000000` zones.
- Primary: ember orange `#ff7300` (badges, pills, heat) + yellow `#fdc211` + red `#ff272d` — warm signal trio.
- Pastels: periwinkle `#817fff`, peach `#ffc753`, pink `#f49eff`, sage `#81b09a`, cyan `#79deeb` (all AA on dark) — proof-band variety without new hues shouting.
- Supporting: plum `#6c5ce7` (ink-on-it AA-large 4.32).
- Links: ink/cream tones, ALL hovering to `#3860BE` with underline removal — trust-hover convention, seventh occurrence.

## 3. Typography Rules

- Voice: Suisse Intl 500/600/700 (licensed .otf, not Google), 75→11px — grotesque precision with real italics (BoldItalic shipped).
- Code: Suisse Intl Mono 500–700, 15→12px — same family, mono cut; brand unity across prose and code.
- Arial 500 for micro-UI fallbacks. Borrow the family-mono pairing for API products with budget for licenses.

## 4. Component Stylings

- Buttons: white-90% 26px pills (6×18px) on dark + orange 30px pills — glow-by-contrast, not shadow.
- Benchmark selector: 14px tabs + prev/next + scroll-left/right controls — evaluation as interface.
- Socials: 10px-round monochrome (X, LinkedIn, GitHub, YouTube, Discord) — quiet footer row.
- Inputs: ink-on-cream with black focus outline + blue glow shadow — explicit, accessible focus.
- Badges: orange 30px pills (16px) — heat-marked announcements.
- Logo: 362×109 full SVG + complete icon/PWA set (192/512/maskable) + og-image.

## 5. Layout Principles

- 8px scale with fractional fills (9.6/11.2/11px) — dense 11–16px instrument core, 75px display peaks.
- Single page: aurora hero → benchmark instrument → proof bands → dark CTA zone → footer. No funnel — one scroll, one decision.
- 11 gradients stage hero and bands; 23 breakpoints (1920→320, paired stops throughout) — the widest responsive ladder in the repo.

## 6. Depth & Elevation

- Single ring shadow (`rgba(11,9,7,0.1)` 1px) — nearly flat; aurora motion + dark zones carry all depth.
- Decision: motion over elevation — the page breathes instead of lifting.

## 7. Do's and Don'ts

- Do: AAA ink-on-cream; orange heat on dark; benchmark-as-proof; trust-hover links; explicit focus states; 23-step responsive ladder.
- Do: keep pastels on dark or large (verify before light use); keep aurora at 8s ambient.
- Don't: add pages the product doesn't need (single-page is the point); don't shadow what glow can heat; don't rush 0.1–0.6s instrument motion.

## 8. Responsive Behavior

- 23-step ladder (1920→320) with paired stops (1440/1439, 1025/1024/1023, 768/767, 481/480, 426/425) — continuous tuning from ultra-wide to small phone; benchmark tabs scroll horizontally on mobile.
- Touch: 26/30px pills thumb-first; tab controls need 44px targets — verify before borrowing.

## 9. Agent Prompt Guide

- Quick reference: `ai / cream-search / single-landing / light / medium complexity / single CTA (try the API)`.
- Ready-to-use prompt: "Design a search-API landing in the Tavily logic: warm cream grounds with AAA ink text, ember orange heat on dark zones, pastel proof-band accents, licensed-style grotesque with matching mono, aurora-flow hero motion, benchmark-selector tabs as interactive proof, white-glow pill buttons, trust-hover links, explicit focus states, flat surfaces with motion-carried depth, and a 23-step responsive ladder. Prove with instruments, never with adjectives."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Aurora hero (8s flow) — warm-statement entry.
2. Benchmark selector (tabs + scroll) — verify-don't-believe instrument.
3. Proof bands (pastel variety) — capability scan.
4. Dark CTA zone — commitment contrast.
5. Social footer row — ecosystem membership.

### 11. Pattern Position

- Fits the single-instrument pattern: glow → verify (benchmarks) → commit. Against Firecrawl (funnel + blog moat) and Context.dev (maximalist depth), Tavily is one page that trusts the instrument — the AI-infra set now spans funnel, maximalist, minimalist, brutalist, ledger, gate, and single-page.
- Page-flow logic: assume the engineer runs one test query; the benchmark tab must answer before the scroll ends.

### 12. Synthesis Notes

- Unique (borrow as logic): benchmark-selector as hero-proof; single-page completeness; family-mono pairing; aurora-over-elevation; trust-hover seventh occurrence (convention confirmed); 23-step ladder; pastel-on-dark discipline; licensed-type confidence.
- Combine with: Firecrawl's blog moat for the depth Tavily skips and Context.dev's agent-prompt CTA for machine onboarding.
- Avoid: copying cream + ember + Suisse verbatim (reads "Tavily clone"); pastel body text on light; pages for their own sake; static hero — motion is the depth here.
