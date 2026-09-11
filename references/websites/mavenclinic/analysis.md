# Mavenclinic — Design Analysis

> Source: `https://www.mavenclinic.com/` · Baseline: `baseline.json` · Collected: 2026-09-11 (Dembrandt 0.32.2)
> Maven Clinic is virtual care for women's and family health (fertility, maternity,
> parenting, menopause), sold to employers/health plans and used by members. The site is
> **warm clinical editorial**: deep pine green on warm bone, serif display emotion plus
> grotesk body clarity — trust through warmth, not sterile hospital blue.

## 1. Visual Theme & Atmosphere

- **Warm care, not cold clinic.** Bone paper (`#EDE9E3` / `#F8F5F1`) with deep pine ink
  (`#013126`). The page feels like a premium editorial magazine about care — calm,
  human, competent.
- **Editorial emotion + operational proof:** huge serif headlines promise empathy;
  program cards, employer proof, and pricing pages prove it operates at scale.
- **Dual-audience calm:** speaks to members (warmth, stories, programs) and buyers
  (employers/plans: outcomes, predictable costs, solutions) without splitting the design
  language — same palette and type, different proof blocks.
- Mood: trusted, inclusive, premium-but-accessible — healthcare that lowers anxiety.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Ink / canvas-dark | pine `#013126` | Headlines, body text, dark section backgrounds (14.3:1 on white, AAA) |
| Canvas-light | bone `#EDE9E3`, paper `#F8F5F1` | Page background, alternating sections (pine on bone 11.8:1, AAA) |
| Action | teal `#00856F` | Primary buttons, links (4.58:1 on white — AA, not AAA; never for small body text) |
| Action-deep | `#005350` / `#035748` | Alt button fill, footer/form bands — darker teal for contrast on light |
| Highlight | mint `#58EDA2` | Eyebrow markers, button wraps — energy on pine (9.6:1 on pine, AAA) |
| Secondary text | sage `#64726F` | Meta, list descriptions (5.0:1 on white AA; fails on pine — light-only use) |
| Program coding | periwinkle `#7176FF`, yellow `#FFD622`, cyan `#26C9DF` | Colored dots distinguishing care programs (fertility, maternity, menopause…) |
| Text-dark | `#222222` / `#263633` | Tabs, deep body copy on light (12.6:1, AAA) |

- **One warm neutral does the calming:** bone replaces clinical white — softer, premium,
  still AAA with pine ink. White (`#FFFFFF`) is reserved for cards and button text.
- **Teal acts, mint energizes, dots categorize:** teal never decorates backgrounds;
  mint never carries text except on pine; program dots are the only multi-hue moment.
- **Light handling:** light-first with inverted pine sections (demo hero, footer) for
  rhythm — depth through section inversion, not dark mode.

## 3. Typography Rules

- **Pairing: serif emotion + grotesk clarity.** Display in IvarDisplay (160/91/69/56px,
  400, 1.1) and Domaine Display headings (50/40/24px, 400–600); body and UI entirely in
  Helvetica Now Display (24/22/20/18px, 300–700). Serif promises care; grotesk delivers
  information without friction.
- **Weight-as-tone:** display stays light/regular (300–400) even at 160px — never shouts;
  emphasis comes from size and serif character, not bold. Bold (600–700) is reserved for
  small labels and CTA text (16px/600).
- **Fluid display:** large sizes flagged fluid — 160px hero scales down the breakpoint
  ladder instead of jumping. Body holds 18–24px at 1.5 leading for long health copy;
  12–14px semibold for eyebrows, dots, and legal.
- **Hierarchy:** 160px statement → 62–76px section headlines → 40–50px Domaine card
  titles → 18–24px body → 12–14px meta. Tight display leading (1.0–1.1), roomy body
  leading (1.5–1.64).

## 4. Component Stylings

- **Primary button:** teal fill (`#00856F`), white text, small `4px` radius, `0 20px` /
  `14px 30px` padding — "Book a demo", "Get pricing". Rectangular confidence, not
  pill-playfulness; the anti-SaaS-pill is a genre signal.
- **Ghost button:** transparent fill, teal text, same 4px radius — "Login". Quiet
  alongside the filled primary; the dual CTA (ghost + filled) is the nav signature.
- **Deep variant:** dark-teal fill (`#005350`) with white text for "Explore our
  solutions" on light — same shape, darker job (buyer CTA vs member CTA).
- **Cards:** 8–12px radii, paper/white fills, section-tinted bands (`24px 24px 0 0`
  top-rounded sections); program cards use color dots, not colored fills — categorization
  without rainbow noise.
- **Inputs:** two modes — underline inputs (0px radius, bottom hairline) for newsletter/
  footer capture; boxed inputs (4px radius, `#DEE3E3` border) for forms. Focus state is
  blue (`#3898EC`) outline — functional, not branded.
- **Links:** teal, underline on default for body links; nav links white/pine with teal
  hover — color change only, `0.3–0.4s ease`, no layout shift.

## 5. Layout Principles

- **Spacing scale:** 8px base; workhorses are 8/16/24/32px with 1px hairlines, then
  large section jumps (96/100px observed 18+ times) — dense component interiors floating
  in generous editorial whitespace.
- **Section rhythm:** statement hero → trust/employer proof → programs (dot-coded cards)
  → services/eyebrow deep-dives → features list → stories tabs → research cards →
  pricing → demo hero → footer. Each section earns attention once; buyers and members
  each get dedicated proof bands.
- **Webflow grid:** centered, narrow-measure compositions; imagery supports rather than
  dominates — photography proves human outcomes, UI never crowds it.
- **Inversion rhythm:** light bone sections alternate with deep pine bands (demo hero,
  footer/form) — pacing through tonal inversion instead of decorative dividers.

## 6. Depth & Elevation

- **Soft functional shadows**, not hairline structure: `rgba(0,0,0,0.25) 0/4/4`,
  green-tinted `rgba(38,54,51,0.12) 0/0/4/4`, faint `rgba(0,0,0,0.1) 0/0/12/2` — cards
  lift gently off bone; restraint keeps them clinical-clean.
- **Borders minimal:** inputs and program rows use 1px lines; cards rely on shadow +
  tonal fill rather than outlines.
- **Motion over depth for feedback:** buttons/cards/links transition `0.3–0.4s ease`
  on color/opacity/transform; hero fades in `0.8s ease-out`; tab progress runs `5s
  linear` — calm, never bouncy. No glow or glass effects.

## 7. Do's and Don'ts

- **Do:** bone + pine AAA pair as the foundation; serif display + grotesk body; 4px
  rectangular CTAs; dot-coded program categories; inverted pine bands for pacing; AAA
  body contrast; dual-audience proof (member stories + employer outcomes).
- **Don't:** use teal for small body text (AA only); put sage text on pine (fails);
  pill-ify the CTAs (breaks the editorial-clinical voice); rainbow-fill program cards
  (dots categorize, fills shout); add sterile blue gradients — warmth is the brand.

## 8. Responsive Behavior

- Dense Webflow ladder (1920 → 1660 → 1440 → 1280 → 991 → 768 → 479 → 320) — continuous
  refinement; standard collapses at 991 (nav + multi-column), 768 (cards stack), 479
  (type + CTA full-width).
- Display type fluid-scales (160px → mobile) instead of reflowing; hero stacks to single
  column with CTA pair intact; program dots and eyebrows stay legible at small sizes.
- Touch targets stay comfortable (14–16px CTA text, 30–32px padding); underline inputs
  gain tap height on mobile; tables/pricing stack to single column.

## 9. Agent Prompt Guide

> Build a landing page with a **warm clinical-editorial aesthetic**: bone canvas
> (`#EDE9E3` / `#F8F5F1`), deep pine ink (`#013126`, AAA), teal action (`#00856F`,
> AA-only — buttons and links, never small body copy), mint highlight (`#58EDA2`) for
> eyebrows on pine, sage (`#64726F`) for light-only meta. Serif display (Ivar-style,
> light/regular, tight 1.0–1.1 leading, fluid 160px → mobile) + grotesk body
> (18–24px, 1.5 leading) + 12–14px semibold labels. Rectangular 4px CTAs — teal-filled
> primary plus ghost secondary, deep-teal variant for buyer actions. Program categories
> as color dots (periwinkle/yellow/cyan), never full fills. 8px spacing scale with
> 96–100px section padding; alternate light sections with inverted pine bands. Soft
> functional shadows only; `0.3–0.4s ease` feedback, `0.8s` hero fade. Tone: calm,
> trusted, inclusive — care that lowers anxiety.

## 10. Component Map

1. Navbar — bone/translucent; wordmark left, solution links center, ghost "Login" + teal "Book a demo" right.
2. Hero — oversized serif statement (160px fluid) + dual CTA + human photography proof.
3. Trust / employer band — logos + outcome stats ("predictable costs") for buyer confidence.
4. Programs cards — dot-coded care areas (fertility, maternity, menopause…); dot color is the category system.
5. Services eyebrow deep-dives — mint markers + pine bands explaining care models.
6. Features list — two-column rows (sage descriptions) pairing copy with proof.
7. Stories tabs — member narratives with tabbed visuals + `5s` progress motion.
8. Research cards — link-block cards ("research_card-link-block") for credibility.
9. Pricing — "Get pricing" CTA + predictable-costs card (10px radius band).
10. Demo hero — inverted pine band ("Explore our solutions" deep-teal CTA + white ghost "Work with us").
11. Contact / form band — boxed + underline inputs per context.
12. Footer — deep pine/green, multi-column links, newsletter capture, social quiet.

## 11. Pattern Position

Best fits a **healthcare-trust landing** (no `healthcare` pattern file exists yet — this
analysis is the seed): empathy-led hero, dot-coded program taxonomy, dual-audience proof
(member stories + employer outcomes), transparent pricing path, inverted closing band.
It borrows the SaaS-landing skeleton (hero → proof → features → pricing → CTA) but
replaces SaaS energy with editorial calm and clinical credibility — the genre markers to
codify are bone+pine AAA warmth, serif/grotesk pairing, and program-dot categorization.

## 12. Synthesis Notes

- **Unique:** warm bone + pine AAA system instead of sterile white/blue clinical; serif
  display emotion with grotesk operational clarity; rectangular 4px CTA discipline (anti-pill);
  program-dot taxonomy (color categorizes without rainbow fills); dual-audience flow in one
  visual language; inverted pine bands as pacing devices.
- **Combine with:** Ramp's single-accent discipline (swap mint intensity to change
  temperature); Ghost's type-led calm for long-form health content; Linear's weight-grade
  restraint for buyer-facing proof sections; Wispr's editorial serif moments for storytelling
  bands.
- **Weaknesses / avoid:** teal body text and sage-on-pine fail contrast — don't copy those
  pairs into new roles; the palette depends on bone warmth, so placing it on pure white/gray
  flattens it; program dots only work with ≤6 categories — more dots become noise; don't lift
  the exact pine + teal + 4px combo without changing layout/voice (that reads as a Maven
  clone, not inspiration).
