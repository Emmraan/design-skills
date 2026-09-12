# Flowstep — Design Analysis

> Source: `https://app.flowstep.ai/welcome` (AI workflow product — auth gate) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 2 pages: `/login`, `/register` — `/welcome` redirects to login; page copy minimal at 129/278 chars, tokens read from stylesheets)

Flowstep is an honest auth-capture: the welcome page sits behind login, so this reference documents a real production auth flow — Google-OAuth-first, brand-blue (`#0247fe`, 6.3 AA) actions, ghost secondary buttons, borderless filled inputs, and an 8px-only radius system. The stylesheets leak a richer token world (full brand-blue 200–900 scale, earth-tone families, DM Sans + Caveat + Geist Mono) that the auth pages only partly use — documented as observed, not assumed.

## 1. Visual Theme & Atmosphere

- Mood: clean waiting room — white, one confident blue, Google-button familiarity, zero marketing noise.
- Philosophy: auth as hospitality — get the stranger inside fast (OAuth first, email second), save personality for the app.
- Caveat-first reference: thin page copy means layout/funnel claims stay minimal; token claims are stylesheet-grounded.

## 2. Color Palette & Roles

- Brand blue scale (observed in CSS vars): `#c0d7fa` 200 → `#91befa` 300 → `#6e9dfa` 400 → `#4d7af7` 500 → `#2e66ff` 600 → `#102f85` 900; functional primary `#0247fe` (6.3 AA on white) with `#0a3cc7` text-primary (white-on-it 8.45 AAA hover).
- Earth families (stylesheet, unused on auth pages): mist `#394447`, olive `#7c7c67`/`#5b5b4b`, mauve `#463947`/`#d7d0d7`, taupe `#473c39`/`#d8d2d0` — a warm-neutral system waiting in the app.
- Ink `#1c1c21` (16.97 AAA) + `#646573` (5.75 AA); fail `#9899a4` on white 2.83 (placeholder-grade, correctly non-essential).
- Hairlines: single `#d7d7de` left-rule token — dividers barely exist on auth.

## 3. Typography Rules

- Rendered: Inter 600, 18→12px — auth minimalism, one weight.
- Stylesheet-declared: DM Sans (variable, opsz), Caveat (handwritten accents), Geist Mono (code) — the app's voice/mono/hand split, visible here only as intent.
- Decision: document both layers, borrow only the rendered one. Borrow the declared split only after capturing an app page.

## 4. Component Stylings

- Primary: `#0247fe` 8×16px, white text — single blue door.
- Secondary: 4%-black ghost pill (0×12px, ink text) — the quiet alternative.
- OAuth: "Continue with Google" color-shift hover — third-party trust as primary path.
- Inputs: borderless 4%-black fill, 8×12px, 8px radius — filled-field pattern (no outline anxiety).
- Links: ink, blue, muted-underlined — three jobs, three treatments.
- Logo: inline SVG `#1c1c21` wordmark (112×24, links to flowstep.ai) + ico favicon.

## 5. Layout Principles

- Auth minimal: centered card, logo → OAuth → divider → email → submit; spacing tokens sparse (8/4/2px observed — card padding comes from unparsed utilities).
- Single 600px breakpoint — auth is mobile-first by nature.
- Motion: 0.218s button ease + 0.3s input ease-in-out — fast, barely-there.

## 6. Depth & Elevation

- Zero shadows detected — flat card on white, separation by fill (4% black) rather than lift.
- Decision: filled-flat auth — no elevation performance cost, no visual noise before the product.

## 7. Do's and Don'ts

- Do: AAA ink pairs; AA blue primary; OAuth-first ordering; filled borderless inputs; 8px radius consistency; 600px auth breakpoint.
- Do: keep muted placeholder text non-essential (it fails); keep auth fast (<0.3s motion).
- Don't: market on the login page (Flowstep doesn't); don't outline inputs that fill could soften; don't invent radius variety.

## 8. Responsive Behavior

- 600px single stop — stacks and stretches; full-width blue primary is thumb-first.
- Touch: OAuth + primary both full-width on mobile; verify 44px targets before borrowing.

## 9. Agent Prompt Guide

- Quick reference: `ai / auth-blue / auth-gate / light / low complexity / single CTA (continue with Google)`.
- Ready-to-use prompt: "Design an auth gate in the Flowstep logic: white grounds with AAA ink text, one AA brand-blue primary button, ghost secondary, Google-OAuth-first ordering, borderless 4%-fill inputs with 8px radii, single 600px breakpoint, sub-0.3s motion, zero shadows. Get the stranger inside fast; save personality for the app."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. SVG wordmark (112×24) — brand anchor.
2. Google OAuth button — primary door.
3. Email input (filled, borderless) — secondary path.
4. Blue submit (8×16) — commitment.
5. Muted help links — escape hatches.

### 11. Pattern Position

- Fits the auth-gate pattern: trust (OAuth brand) → path (email) → commit (blue) → escape (help links). The repo's first pure-auth reference — pairs with any product page as its front door.
- Page-flow logic: assume the visitor already decided (they hit /welcome); the only job is removing keystrokes.

### 12. Synthesis Notes

- Unique (borrow as logic): OAuth-first ordering; filled-borderless inputs; 8px-only radius; stylesheet-declared vs rendered token honesty; warm-earth families reserved for app depth; zero-shadow auth.
- Combine with: any product landing as its gate (this reference is a door, not a house) and SaaS onboarding patterns for what comes after register.
- Avoid: copying blue + Inter auth verbatim (reads "generic SaaS login" — the value here is restraint, which must be re-earned per brand); marketing copy on login; outlined inputs by default; slow auth motion.
- Revisit: capture an authenticated app page later — the declared DM Sans/Caveat/earth system deserves a rendered reference.
