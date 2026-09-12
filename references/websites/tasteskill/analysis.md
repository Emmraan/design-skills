# Taste Skill — Design Analysis

> Source: `https://www.tasteskill.dev/` (agent skill, installs via `npx skills add Leonxlnx/taste-skill`) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/docs`, `/blog`, `/changelog`, `/guide`)

Taste Skill is a developer-tool landing with a paper soul: warm `#f5f4f2` grounds, a near-black hero (`#0e1011`), one safety-orange accent (`#ff6b00`), Manrope for voice and IBM Plex Mono for code. The install command is the primary CTA — docs, changelog, and guide close the trust loop. Against Linear's dark minimal-clean, this is the light editorial pole of developer-tools.

## 1. Visual Theme & Atmosphere

- Mood: printed manual meets terminal — warm paper, hairline rules, mono code, one orange spark.
- Philosophy: documentation is the marketing — `/docs` (66k chars) outweighs the landing; the site reads like a well-kept README with a hero.
- Signature: the copy-paste install block (`$ npx skills add …` + Copy) presented as a designed component, not an afterthought.

## 2. Color Palette & Roles

- Grounds: warm paper `#f5f4f2` (manifest theme + bg) + cream hero wash `#f4efe6` + card white `#fcfcfb`/`#ffffff`.
- Ink: near-black `#0a0a0a` (18.01 AAA on paper) + `#1a1a1a` blocks + neutral `#525252` (7.11 AAA) + `#737373` secondary.
- Accent: safety orange `#ff6b00` — 6.68 AA against the dark hero; used sparingly as the single spark.
- Dark zone: `#0e1011` hero background with `#c8c8cd` text (decorative on light — fails at 1.67, correctly confined to dark surfaces).
- Structure: `#e5e5e5` hairlines in three alphas (0.8/0.9/1.0) + 1px black nav rule + emerald success ring `rgba(5,150,105,0.22)` for positive states.

## 3. Typography Rules

- Voice: Manrope 500/600, 128px display → 11px UI (17 steps) — geometric warmth, never corporate.
- Code: IBM Plex Mono 500/600, 15→9px — install commands, captions, technical asides all speak mono.
- Decision: two-family split (humanist sans for persuasion, mono for proof) is the whole devtool-typography playbook in one site. Borrow the split, not the faces.

## 4. Component Stylings

- Install block: 16px dark rounded panel + inset top highlight + deep drop shadow — the product's front door, designed like a terminal card.
- Nav CTAs: tiny pills (6×14px, 12.5px Manrope 500) — black fill primary, white/hairline secondary; quiet chrome around loud content.
- Copy buttons ("Befehl in Zwischenablage kopieren", 16px) turn every code sample into a conversion point.
- Links: 5 styles resolving to ink (`#0a0a0a`) and neutrals — no blue-link convention; the site trusts hierarchy over color.
- Logo: 32px webp mark (`icontaste.webp`) + full favicon set (48/32/180px webp + png) + og-image — complete brand kit.

## 5. Layout Principles

- 8px scale (2/4/6/8/12/14/16/20/24/28/32/48/64/80/112px) — 112px hero air over a dense 12–16px docs core.
- Funnel: dark hero with install command → warm paper proof (features, stars: "86,397 stars" GitHub pill) → docs/blog/changelog/guide depth → footer.
- 14 linear gradients stage the homepage hero; inner pages go flat for reading.

## 6. Depth & Elevation

- Tailwind ring system: 1px oklab rings + 3–4% micro-drops — separation without decoration; the only dramatic shadow belongs to the install block (inset highlight + 30px drop), marking it as the one object that matters.
- Decision: flat paper + one glowing terminal — attention architecture, not decoration.

## 7. Do's and Don'ts

- Do: AAA ink-on-paper pairs; orange reserved for dark surfaces (AA 6.68); mono for all code; hairline hierarchy; copy-button on every command; docs heavier than landing.
- Do: keep orange off light grounds (unverified there — don't assume it passes); keep muted `#c8c8cd` on dark only.
- Don't: add a second accent; don't blue-ify links (ink hierarchy is the system); don't shrink docs type below 12–14px; don't decorate inner reading pages.

## 8. Responsive Behavior

- No breakpoints detected in tokens — Tailwind arbitrary values with responsive/state modifiers handle adaptation structurally rather than through named breakpoints. Verify mobile manually before borrowing layout wholesale.
- Touch: pill CTAs and full-width install block are thumb-safe; copy buttons must stay ≥44px targets on small screens.

## 9. Agent Prompt Guide

- Quick reference: `developer-tools / warm-paper / docs-led / light with dark hero / medium complexity / single CTA (install command)`.
- Ready-to-use prompt: "Design a developer-tool landing in the Taste Skill logic: warm paper grounds with a near-black install hero, AAA ink body text, Manrope-style geometric sans for voice plus a mono family for all code, the install command as a glowing terminal card with copy button, tiny pill nav CTAs, hairline rule hierarchy, one orange accent reserved for dark surfaces, ring-shadow elevation, gradients only on the hero, and docs/blog/changelog depth behind the landing. Convert on copy-paste, never on hype."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Dark install hero (command + Copy) — primary conversion.
2. GitHub stars pill (9999px) — social proof in one chip.
3. Feature bands on paper — capability scan.
4. Docs (`/docs`, 12/17 WCAG) — depth trust.
5. Guide (`/guide`) — onboarding ramp.
6. Blog + changelog — maintenance signals (alive project).
7. Footer nav — sitemap close.

### 11. Pattern Position

- Fits the docs-led devtool pattern: install → prove (stars, features) → deepen (docs, guide) → retain (blog, changelog). Against Linear (dark, product-led, dual CTA), Taste Skill is light, docs-led, single-CTA — the pair now covers both devtool postures.
- Page-flow logic: assume the developer will skim the hero and judge by the docs; the landing only needs to earn the scroll, the docs earn the install.

### 12. Synthesis Notes

- Unique (borrow as logic): install-command-as-hero-component; voice/mono two-family split; warm paper for a devtool (category usually goes cold dark); single orange spark discipline; docs-outweigh-landing content ratio; copy-button-per-command conversion pattern.
- Combine with: Linear's dark product-led drama for launch moments (paper for docs, dark for drama — theme as narrative device) and SaaS changelog patterns for the retention loop.
- Avoid: copying paper + orange + Manrope verbatim (reads "Taste clone"); orange body text on light; decorating reading pages; skipping the changelog — dead changelog kills devtool trust.
