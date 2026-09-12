# One Medical — Design Analysis

> Source: `https://www.onemedical.com/` (Amazon One Medical, primary care membership) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/about-us/`, `/business/` ×2, `/contact-us/`)

One Medical sells trust in healthcare: deep pine greens, warm photography, editorial serif headlines, and pill CTAs that never shout. The system reads calm-clinical — institutional credibility softened by sage, peach, and humanist details.

## 1. Visual Theme & Atmosphere

- Mood: reassuring, unhurried, quietly premium. White space + pine bands + smiling-provider photography instead of clinical coldness.
- Philosophy: reduce anxiety at every step — generous 80–160px section padding, soft pills, teal hover states that warm (never alarm), and a PWA-grade manifest for app-like reliability.
- Consumer + employer dual audience: `/business/` mirrors the consumer funnel for HR buyers without changing the visual language.

## 2. Color Palette & Roles

- Primary: deep pine `#005450` (bands, badges, primary buttons) + ink-pine `#004D49` (body text, 9.73:1 on white AAA; reversed white-on-pine 8.81 AAA).
- Grounds: white `#FFFFFF` + off-white `#F4F4F4` (8.01 AAA on pine) + mint wash `#EEF6F4`.
- Secondary: sage `#ABCC76` (accents, hairlines, 4.88 AA on pine) + peach `#FFC776` (highlights) + warm ink `#2A2927`.
- Links/CTAs: teal `#068466` (4.67 AA on white) warming to `#009E87` on hover; legacy blue `#0000EE` underlined links; bright blue `#0578FF` for app-style actions.
- Known fails (decorative): pine-on-pine 1.1 and blue-on-pine 1.07 — tonal texture, never text. Keep text on white/pine only.
- Two subtle linear gradients + one soft shadow (`rgba(0,0,0,.25) 0 2.1px 3.5px`) — restraint that keeps the clinical calm.

## 3. Typography Rules

- Pairing: GT Super Display (88/72/50/48/32px, 500–600) for editorial headlines + Ginto (20/18/16/14px, 200–600) for body/UI + Arial for micro-UI.
- Logic: serif display conveys human warmth and editorial authority; light-weight Ginto body (200–300) keeps long health explainers airy; semibold reserved for CTAs and prices.
- Decision: display serif + light body is the care signal — borrow for any trust-heavy vertical, keep body ≥14px.

## 4. Component Stylings

- CTAs: pine pills (36px radius, 12×14px, white 600 14px text) + extreme 5000px-radius buttons for fluid widths; 1px pine or `#E2E0DE` hairline borders on secondary.
- Media: 50%/100% round video-play buttons and portrait crops — providers as friendly faces, literally circled.
- Badges: pine pill badges; checkbox inputs with light-blue focus ring (`#88C0FB` glow).
- Links: 8 styles; teal default → warmer teal hover; blue links underline; white-on-pine links drop decoration on hover.
- Nav: 5–7 dropdown menus per page; color-shift hovers ("Locations", "Offices").

## 5. Layout Principles

- 8px scale with care-sized jumps (3/10/12/16/20/24/32/48/56/64/80/120/160px) — landing bands breathe at 120–160px while forms tighten to 12–24px.
- Funnel order: hero reassurance (headline + provider imagery + pill CTA) → how-it-works → insurance/employer proof → locations → membership pricing → contact.
- Business pages reuse the identical band system — one layout language, two buyers.

## 6. Depth & Elevation

- Minimal: one soft shadow + two gradients + hairline borders (`#ABCC76` underlines, pine button outlines, `#E2E0DE` secondary). Round image crops and pills create friendliness without elevation.
- Decision: flat + round + warm beats clinical-blue + glossy in healthcare — depth would read "salesy".

## 7. Do's and Don'ts

- Do: pine/white AAA pairs; teal links with warming hovers; serif headlines + light body; round provider imagery; 120px+ section air.
- Do: keep blues to app actions and legacy links — teal owns the marketing voice.
- Don't: set text pine-on-pine or blue-on-pine (both ~1.1); don't sharpen radii (squares read institutional-cold); don't add urgency patterns — healthcare converts on calm.

## 8. Responsive Behavior

- 31-breakpoint ladder (2181→99px) — editorial type scales smoothly from wall displays to 320px phones; pills stay tappable; business carousels advance (6 advances observed).
- Touch: pill CTAs and round play buttons are thumb-first; checkbox focus rings stay visible on mobile.

## 9. Agent Prompt Guide

- Quick reference: `healthcare / warm-clinical / care-funnel / light / medium complexity / dual CTA (patient signup + employer/business)`.
- Ready-to-use prompt: "Design a warm-clinical care page in the One Medical logic: white grounds with deep-pine bands, AAA pine/white pairs, serif display headlines with light humanist body, pine pill CTAs and round provider portraits, teal links that warm on hover, hairline sage dividers, one soft shadow, slow 1.4s hero fade-zoom with 0.25s functional ease, and a 31-step responsive ladder. No urgency patterns — convert on calm."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Reassurance hero (serif headline + provider imagery + pine pill CTA + slow fade-zoom).
2. How-it-works bands (membership, app, visits) — de-mystify the service.
3. Insurance/employer proof (`/business/`) — second funnel, same language.
4. Locations finder — proximity trust.
5. Provider portraits (round crops) — humanize the credential.
6. Membership/pricing band — transparent cost, calm presentation.
7. About + contact pages — institutional backing without coldness.

### 11. Pattern Position

- Fits the healthcare trust pattern: reassure → explain → prove (insurance/employers) → locate → convert. Against MavenClinic (virtual-care seed ref), One Medical adds physical-place trust (locations, offices) and employer distribution — the two together cover telehealth + clinic + B2B2C.
- Page-flow logic: calm the fear first, explain second, price transparently last. The serif display does emotional work the copy doesn't have to.

### 12. Synthesis Notes

- Unique (borrow as logic): pine/sage/peach clinical-warm palette; serif-display + light-body care voice; round-portrait humanization; dual-audience single-language system (consumer + employer); calm-as-conversion (no urgency mechanics at all).
- Combine with: MavenClinic's virtual-care flows (together = complete care-funnel reference) and fintech onboarding clarity (eligibility/insurance checks borrow well from KYC patterns).
- Avoid: copying the Amazon-owned brand tokens verbatim; pine-on-pine text; square cold-clinical aesthetics; fake urgency — it would destroy the trust the whole system builds.
