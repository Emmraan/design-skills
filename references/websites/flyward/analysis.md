# Flyward — Design Analysis

> Source: `https://www.flyward.com/` · Baseline: `baseline.json` · Collected: 2026-09-11 (Dembrandt 0.32.2, 5 pages)
> Flyward is a private-aviation service (private-service, corporate-service, about,
> contact). The design is **quiet luxury with editorials manners**: warm cream paper,
> espresso ink at AAA, a giant serif voice (Apris up to 133px), and pill CTAs that
> adapt to their background — filled on light, outlined on dark. Nothing shouts;
> everything implies you can afford it.

## 1. Visual Theme & Atmosphere

- **Cream-paper luxury.** Warm off-white (`#FBF8F3`) canvas with deep espresso text
  (`#3D2D20`, 12–13:1 AAA) — the page feels like a heavyweight brochure: calm,
  expensive, unhurried.
- **Serif as status:** Apris display serif at enormous sizes (133/107/83px, tight
  `0.9` leading) does the selling; Founders Grotesk handles body/UI. The pairing
  says heritage + competence — exactly what private aviation needs.
- **Dark bands for gravity:** charcoal (`#1C2124`) sections (about-hero, locations,
  leadership) break the cream rhythm — white on charcoal 16.25:1, AAA. Depth through
  inversion, the luxury standard.
- Mood: discreet, assured, concierge-calm — wealth whispered, never announced.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Ink | espresso `#3D2D20` | Headlines + body (13.17:1 on white, 12.43:1 on cream — AAA); the voice |
| Canvas | cream `#FBF8F3` | Page background + button fills; warmth without color |
| Ink-2 | near-black `#222222` | Body alternate (15:1 on cream, AAA) |
| Night | charcoal `#1C2124` | Dark bands (white on it 16.25:1, AAA); gravity sections |
| Muted | warm gray `#8E857E` | Secondary on light (3.62:1 — large-only, never body) |
| Decorative gray | `#999999` / `#DBDBDB` | 490+ uses at 2.85:1 — FAILS all body roles; dividers/menus only, never text to read |
| Focus blue | `#3898EC` / `#4D65FF` | Input focus border/outline (Webflow defaults) — accessibility plumbing, not brand |
| Scrim | black fade gradient | Image overlays (2 uses) — text legibility over photography |

- **One ink, two canvases:** espresso speaks on cream AND white; night bands invert
  to white text. No second brand color — luxury through restraint.
- **Light handling:** light-first, charcoal bands for rhythm — the dark is an event,
  not a theme.

## 3. Typography Rules

- **Editorial pairing with jobs:** Apris (serif, woff2) for display/statements
  (133→26px, weight 400 only — size, not weight, creates hierarchy); Founders
  Grotesk Text for body/UI/links (26→16px, 300–400). Never swap their roles.
- **Giant display, tight leading:** 133/107/83/69px at `0.9` leading — headlines
  stack like magazine covers; confidence through scale, not decoration.
- **Body for reading:** Grotesk 24/21/18/16px at `1.2` — compact but legible; UI
  labels and links at 16–21px regular, never bold. Luxury doesn't bold.
- **Hierarchy:** display size steps (133→107→83→69→43) → 32px medium subheads →
  Grotesk body ladder → 16px UI. Weight range stays 300–500 — quiet throughout.

## 4. Component Stylings

- **Primary button:** cream fill (`#FBF8F3`), espresso text, fully pill `2133px`
  radius, generous `21px 32px` padding, 18.6px text ("Discover", 4 uses). Soft and
  substantial — a brochure you can press.
- **Outline adapts to background:** espresso-outline pill ("Contact") on light,
  white-outline pill ("Explore") on dark — same 2133px geometry, border swaps with
  context. The **tri-context CTA** (filled + light-outline + dark-outline) is the
  signature: one shape, three backgrounds.
- **Inputs:** underline-style — white fill, `0px` radius, bottom hairline border,
  espresso text; focus goes blue outline (Webflow default). Forms feel like writing
  on paper, not filling boxes.
- **Links:** espresso or white, no underline; hover shifts color/opacity/border
  (`0.2s ease`) — never underline, never movement. Feedback is tonal.
- **Nav:** espresso menu links with 0.2s color transitions; brand mark left, Contact
  pill right — the standard luxury header.

## 5. Layout Principles

- **Spacing scale:** 8px base with fine fractional steps (5/5.33/8/10.67/12.8/16/
  21.33px) — Webflow-rem precision; rhythm feels tailored, not gridded.
- **Section rhythm:** nav → giant serif hero → service bands (private/corporate) →
  charcoal proof bands (about-hero, leadership, locations) → contact → footer.
  Every band answers one client question: what, for whom, who, where, how.
- **Service split:** private-service vs corporate-service as separate pages — the
  two audiences never share a band; same system, different proof.
- **Band inversion:** charcoal sections pace the cream — pacing through tonal weight.

## 6. Depth & Elevation

- **Hairlines, not shadows:** 494 hairline rings (`1px`, gray/black 15%) define
  structure; only one soft shadow (`1px/4px` at 20%) observed. Elevation is nearly
  flat — paper, not glass.
- **Scrim for photography:** a single black-fade linear gradient over images keeps
  white display type legible — depth serves the photo, never decorates chrome.
- **Motion as polish:** uniform `0.2s ease` (113 uses) across links (15), buttons,
  nav, inputs — color/background/border transitions only. Everything responds, but
  nothing performs.

## 7. Do's and Don'ts

- **Do:** cream + espresso AAA foundation; serif-display/grotesk-body role split;
  one pill radius for all CTAs with context-adaptive fills; charcoal inversion bands;
  hairline structure; uniform 0.2s ease; underline inputs with blue focus.
- **Don't:** set readable text in `#999999` (2.85:1, fails everything — 490 uses in
  source, copy the palette not the mistake); put white text on cream (1.06:1);
  bold luxury UI (weight ceiling 500); add colored CTAs — espresso/cream/white carry
  all actions; shadow-lift cards on cream (hairlines suffice).

## 8. Responsive Behavior

- Full ladder (300 → 400 → 480/479 → 600 → 640/639 → 768/767 → 992/991) — giant
  Apris display scales down the ladder; pill CTAs keep radius and padding at thumb
  sizes; service pages stack single-column.
- Nav collapses to menu; Contact pill survives as the sticky action.
- Charcoal bands keep white AAA at all widths; scrims preserve display legibility
  over photography on small screens.

## 9. Agent Prompt Guide

> Build a landing page with a **quiet-luxury hospitality aesthetic**: warm cream
> canvas (`#FBF8F3`), espresso ink (`#3D2D20`, AAA 12–13:1), charcoal (`#1C2124`)
> inversion bands with white AAA text. Serif display (Apris-like) at enormous sizes
> (133→43px, weight 400, tight 0.9 leading) for statements; grotesk body/UI
> (26→16px, 300–400, never bold). Fully pill CTAs (2133px) — cream-filled primary
> with generous 21×32 padding, outline variants that adapt to background (espresso
> on light, white on dark). Underline-style inputs with blue focus. Hairline rings
> for structure, one soft shadow max, black-fade scrims over photography. Uniform
> 0.2s ease tonal hovers — no underlines, no movement. Tone: discreet, assured,
> concierge-calm — wealth whispered.

## 10. Component Map

1. Header — brand mark left, espresso menu links, outline "Contact" pill right.
2. Hero — giant Apris display statement (133px) + cream "Discover" pill on light.
3. Service bands — private-service and corporate-service pages, same system, separate proof.
4. About-hero band — charcoal inversion with white display type.
5. Leadership grid — team proof on dark with muted secondary text.
6. Locations band — charcoal, place proof.
7. Contact — underline inputs + pill submit, footer closure.

## 11. Pattern Position

Best fits a **hospitality/service landing** (no `hospitality` pattern file exists yet —
this analysis is the seed): statement hero → audience-split services → dark proof
bands (people, places) → contact. It borrows the SaaS skeleton but replaces feature
grids with audience pages and photo-scrim statements — the genre markers to codify
are audience-split service paths and inversion bands as the proof rhythm.

## 12. Synthesis Notes

- **Unique:** tri-context pill CTA (filled + light-outline + dark-outline, one
  geometry); serif-at-133px as the whole pitch; cream/espresso/charcoal triad with
  zero supporting colors; underline inputs on a luxury page; hairline-only depth.
- **Combine with:** Vita Travel's dark immersion for a "night" premium tier;
  Ghost's editorial calm for long-form brand storytelling; Udemy's fixed-hierarchy
  cards if services need listing at scale; Maven's serif warmth for human narratives.
- **Weaknesses / avoid:** `#999999` body text is baked into the source at 490 uses —
  flag it, never copy it; the cream + giant-serif look is strongly "Flyward" — lift
  the *system* (role-split type, adaptive pills, inversion rhythm) with a different
  serif and ink hue, never the exact cream-espresso combo; sparse content makes
  giant display feel empty — this system needs confident, short headlines.
