# Framer — Design Analysis

> Source: `https://www.framer.com/` (website builder / design-to-site tool) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/pricing`, `/enterprise/`, `/contact/`, `/startups/`)

Framer is the canvas selling itself: black grounds, Framer-blue (`#0066ff`) actions, Inter Variable set with optical sizing, organic radii (24 values, 3–100px), and a film-grain keyframe over everything. The product builds the page — so the page must feel designed, not templated. Against SaaS siblings (ClickUp's utility, Ghost's editorial, Juno's fintech calm), this is the craft pole.

## 1. Visual Theme & Atmosphere

- Mood: design-studio screening room — black, blue glow, grain, template gallery as art wall.
- Philosophy: template proof — the gallery IS the persuasion; copy stays minimal because the work speaks.
- Segmented funnel: startups and enterprise get dedicated pages, not just pricing tiers — sell the segment, not the seat.

## 2. Color Palette & Roles

- Grounds: `#000000` + `#111111` + `#242424` (white-on-`#242424` 15.52 AAA).
- Primary: Framer blue `#0066ff` + sky `#0099ff` (hover `#0082d9`) for actions, focus rings, and code accents.
- Signal green `#4cd963` (hover `#41b854`) for success/positive states.
- Neutrals: `#999999` (7.37 AAA on black, 6.63 AA on `#111111`) + `#666666` (AA-large on `#111111`) + `#cccccc`.
- Known fails: `#0000ee` links on black 2.23, black-on-`#111111` 1.11 — legacy/edge tokens, never body text.

## 3. Typography Rules

- Voice: Inter Variable (wght 400–760, opsz 14–32), 24→6px — optical sizing keeps micro-copy legible and display crisp from one file.
- Code: Input Mono 700 for 12px technical captions — tool-credibility in miniature.
- OpenType richness (dlig, cv01–cv13) — typographic craft as brand signal. Borrow variable-font discipline, not the stack.

## 4. Component Stylings

- Buttons: 8px-radius system — white 10×14, white-10% glass, dark `#1f1f1f` — quiet chrome; the canvas content provides the color.
- Inputs: token-driven (`--framer-input-*` vars) textareas, 4px checkboxes on white-7%, selects — form system built like a design system, because it is one.
- Links: 5 styles with var-resolved hovers (`--framer-link-hover-*`) — theming without overrides.
- Radius: 24 values (3/4/5/6/8/10/12/15/18/20/25/100px) — organic, per-component radii instead of a scale; the anti-system system.
- Logo/assets: framerusercontent CDN images (50×37 logo) + full favicon/og set.

## 5. Layout Principles

- 8px scale with 120/100/60/40px air — gallery-scale whitespace, dense 12–16px UI core.
- Funnel: black hero → template gallery → feature proof → pricing → segment pages (startups, enterprise) → contact.
- 4 gradients, restrained — glow accents, never gradient-as-brand.

## 6. Depth & Elevation

- 1px ring shadows (`#111111`, white-10%) + two micro-drops — separation without lift; content floats on black, chrome stays etched.
- Film grain (`betterGrainWebpFramesV22`, 0.75s) over hero/media — texture as depth, the site's most borrowable trick.

## 7. Do's and Don'ts

- Do: AAA white-on-black pairs; blue actions; variable font with opsz; organic per-component radii; grain texture; segment-specific pages; token-var links/inputs.
- Do: keep `#0000ee`-legacy tokens out of new work; keep grain subtle (0.75s loop, never competing with text).
- Don't: add a second brand color (blue + sky + green is the budget); don't systematize radii into 3 steps (organic is the point); don't out-shout the gallery.

## 8. Responsive Behavior

- 4 breakpoints (1199/810/809/98px) — gallery grids reflow, hero air compresses 120→40px; 809/810 double-stop suggests fine-tuned tablet handoff.
- Touch: 10×14px buttons need 44px targets on mobile — verify before borrowing densities.

## 9. Agent Prompt Guide

- Quick reference: `saas / blue-canvas / product-funnel / dark / high complexity / dual CTA (start free + enterprise)`.
- Ready-to-use prompt: "Design a website-builder page in the Framer logic: black grounds with AAA white text, one Framer-blue action color with sky hover states, Inter Variable with optical sizing plus a mono for technical captions, organic per-component border radii, 1px ring-shadow depth, a subtle film-grain texture over hero media, quiet 8px buttons, token-variable links and inputs, a template gallery as the persuasion core, and dedicated segment pages for startups and enterprise. Sell the canvas by showing the canvas."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Black hero + grain — craft statement.
2. Template gallery — proof that replaces copy.
3. Feature bands — capability scan.
4. Pricing (`/pricing`) — packaging transparency.
5. Startups (`/startups/`, 17/24 WCAG) — segment capture.
6. Enterprise (`/enterprise/`) — procurement trust.
7. Contact (`/contact/`, token inputs) — capture close.

### 11. Pattern Position

- Fits the canvas-tool pattern: inspire (gallery) → try (free CTA) → package (pricing) → segment (startups/enterprise). Against ClickUp (utility-led) and Ghost (editorial-led), Framer is gallery-led — the SaaS set now covers utility, editorial, and craft.
- Page-flow logic: assume the visitor is a designer judging taste in 3 seconds; the hero must pass the taste test before any feature is read.

### 12. Synthesis Notes

- Unique (borrow as logic): gallery-as-persuasion (copy minimalism earned by proof); film-grain texture as brand; organic anti-scale radii; variable-font opsz discipline; segment pages over pricing tiers; token-var form/link systems; product-builds-page meta-proof.
- Combine with: SaaS pricing transparency for packaging (already present — study its restraint) and agency portfolio patterns for gallery curation.
- Avoid: copying black + Framer-blue + Inter verbatim (reads "Framer clone"); gradient-as-brand; systematized radii; copy-heavy hero — if the gallery can't carry it, the product can't either.
