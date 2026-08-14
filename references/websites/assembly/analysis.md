# Assembly — Design Analysis

> Source: `https://assembly.com/` · Baseline: `baseline.json` · Collected: 2026-08-14 (Dembrandt)
> Assembly is a creator-commerce / membership payments platform. The marketing page is a
> lesson in **understated premium minimalism**: near-white canvas, a single vivid blue
> accent, and confident typography that lets a young brand feel established.

## 1. Visual Theme & Atmosphere

- **Clean, confident, minimal.** A near-white canvas (`#FEFEFD`) with off-black type and a
  single saturated blue (`#0000EE`) used as the accent.
- **Editorial restraint:** generous whitespace, small type on quiet surfaces, and a flat
  black button. Feels premium and careful.
- **The blue is the spark:** the primary `#0000EE` is used for links/highlights/accents —
  one vivid moment against calm neutrals.
- Mood: minimal, premium, trustworthy, quietly energetic.

## 2. Color Palette & Roles

| Role | Value (observed) | Job |
|---|---|---|
| Primary / accent | vivid blue `#0000EE` | Links, highlights, key interactive elements |
| Surface | off-white `#FEFEFD` | Page canvas (warm-tinted, not pure white) |
| Surface alt | gray `#CFCFCF` | Secondary surfaces, dividers |
| Text | warm gray `#404040` | Body/meta |
| Button | near-black `#101010` | Primary buttons (contrast anchor) |

- **Restraint:** off-white + gray + warm-black text + one blue. The blue is the only
  saturated color, making it instantly memorable.
- **Neutral strategy:** warm/cool gray mixtures — clean but not cold.
- **Dark handling:** primarily light-first; minimal dark usage.

## 3. Typography Rules

- **Families:** PPMori (display, 400-600) + Bagoss (secondary) + ABCDiatypeMono (mono
  accents for data/labels). A refined premium grotesque pairing.
- **Display scale:** 64px / 48px / 32px with `line-height ~1.0-1.13`, tight and semi-bold.
  Headlines rely on **weight (600) + size**.
- **Body:** 14-16px, `1.4-1.5` leading.
- **Mono accent:** ABCDiatypeMono for technical eyebrows, numbers, meta — an editorial-tech
  signature.

## 4. Component Stylings

- **Primary button:** near-black fill (`#101010`) with off-white text, fully rounded (pill,
  ~30px radius observed), generous padding. Confident and flat.
- **Secondary:** ghost/outline, blue or black text.
- **Links:** ink → blue on hover (the vivid accent moment).
- **Cards:** off-white/gray surfaces, small radius (8-20px), hairline edges.
- **Inputs:** white fill, bordered, small radius.

## 5. Layout Principles

- **Spacing scale:** 8px base, tight micro steps (2-13px observed) with large section
  padding — precise, editorial rhythm.
- **Grid:** centered, strongly max-width'd columns; lots of whitespace; asymmetric moments
  keep it from feeling stiff.
- **Breakpoints:** 1400 / 1110 / 1080 / 999 / 992 / 991 — desktop→tablet→mobile.

## 6. Depth & Elevation

- **Almost flat:** hairline borders and very subtle shadows. Premium comes from space and
  type, not depth.

## 7. Do's and Don'ts

- **Do:** commit to minimalism; use ONE vivid accent for links/CTAs; warm-tinted near-white
  canvas; black pill buttons; editorial whitespace.
- **Don't:** add multiple saturated colors; clutter the canvas; use heavy shadows; let the
  minimalism become cold.

## 8. Responsive Behavior

- Display type fluid-scales; hero collapses cleanly to single column; nav collapses to
  hamburger with CTA; grids stack on mobile.

## 9. Agent Prompt Guide

> Build a landing page with an **understated premium minimal aesthetic**: warm-tinted
> near-white canvas, warm-gray body text, near-black type and buttons, and a SINGLE vivid
> blue-style accent used only for links/highlights/CTAs. Use a refined grotesque sans for
> display (32-64px, tight leading) and body (14-16px, 1.5), with a mono accent for technical
> labels. Pill-shaped black buttons. Generous whitespace, flat surfaces with hairlines,
> centered columns. Content tone: minimal, premium, quietly confident.

## 10. Component Map

1. Nav — minimal, logo left, CTA right.
2. Hero — centered statement type + product/visual + black pill CTA.
3. Logo cloud / trust — quiet band.
4. How it works — numbered/editorial steps.
5. Features — minimal rows, blue highlights.
6. Testimonials / creators — quotes.
7. Pricing — clean cards, highlighted plan.
8. CTA band — black or blue moment.
9. Footer — muted, legal links.

## 11. Pattern Position

Best fits the **fintech** pattern (`patterns/fintech.md`) (payments/memberships) with a
minimal-credit philosophy, or a SaaS landing with premium restraint. It proves that young
brands can feel established through minimalism + one accent.

## 12. Synthesis Notes

- **Unique:** the "near-white + one vivid blue" economy; warm-tinted surfaces; black pill
  buttons; mono accent for editorial-tech detail; premium minimalism that feels older than
  the company.
- **Combine with:** Ramp's acid-accent discipline (swap blue for a different accent);
  Ghost's type-led calm; a warm editorial serif from Wispr for contrast.
- **Weaknesses / avoid:** extreme minimalism needs strong copy + photography; can feel too
  plain for consumer/playful brands; avoid copying its exact blue + off-white without
  changing the roles.