# Dokploy — Design Analysis

> Source: `https://dokploy.com/` (self-hostable application deployment platform) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/`, `/pricing`, `/contact`, `/enterprise`, `/features/application-deployment-platform`)

Dokploy is shadcn-zinc discipline: pure black (`#000000`), zinc text (`#fafafa` at 20.12 AAA), Lexend display + Inter body, inverted 6px buttons, and a 21-menu mega-nav. Against Coolify's amber populism and Openship's aurora drama, this is the systems pole of self-hosting — the page looks like the dashboard it sells.

## 1. Visual Theme & Atmosphere

- Mood: server room at midnight — black, zinc hairlines, one blurple (`#5965f2`) signal, GitHub stars (37.2k) as headline proof.
- Philosophy: the interface is the marketing — shadcn/Radix/Headless primitives on the landing match the product UI, so trial feels like home.
- 21 homepage menus opened by the crawler: mega-nav depth is a feature (every capability one hover away).

## 2. Color Palette & Roles

- System: black `#000000` + `#fafafa` (20.12 AAA) + `#27272a` panels + `#a1a1aa` secondary (8.19 AAA on black, fails on white — dark-only discipline).
- Signal: blurple `#5965f2` (cloud/supporting actions) + TW ring blue `#3b82f6` (focus states) + green `#4ade80` links (success/terminal connotation).
- Fails: zinc-on-white 2.46, white-on-red `#f87171` 2.65 — decorative/error washes only.
- Borders: zinc hairlines at 30–50% alphas + slate 10% dividers — hairline hierarchy, never boxes.

## 3. Typography Rules

- Display: Lexend 500 only, 72→18px — rounded geometric warmth against cold zinc; single weight = single voice.
- Body: Inter 500–800, 40→12px — workhorse for features, pricing, enterprise.
- Decision: friendly display + neutral body splits emotion from information. Borrow for devtools that need approachability without playfulness.

## 4. Component Stylings

- Buttons: inverted 6px squares — white/zinc-950 primary, black/zinc-bordered secondary (8×16px). No pills except cloud auth ("Sign In/Up Dokploy Cloud" 9999px) — pills mean account, squares mean action.
- Inputs (`/contact`): zinc-900 `#18181b` fill, 6px radius — form as terminal.
- Code blocks: 12px radius, zinc-bordered — docs credibility inline on marketing pages.
- Links: 5 styles resolving to `hsl(var(--primary))` hover — token-driven, theme-aware.
- Logo: inline SVG `#fafafa` wordmark (50×40) + svg icon + og-image; no raster logo anywhere.

## 5. Layout Principles

- 8px scale (1/2/4/6/8/12/16/20/24/32/40/48/64/80/128px) with 128px hero air — vast dark space, dense 12–16px feature core.
- Funnel: black hero with stars pill → mega-nav feature depth → pricing → enterprise → feature page (`/features/...`, 75k chars) → contact.
- 10 homepage gradients stage hero and bands; 5 breakpoints (1400/1280/1024/768/640) collapse grids cleanly.

## 6. Depth & Elevation

- Inset rings + one xl drop for the hero card — elevation is inset-first (pressed-in dashboard feel), the opposite of marketing lift.
- Decision: dashboard-real depth — the landing previews the product's surface physics.

## 7. Do's and Don'ts

- Do: AAA zinc-on-black pairs; pill/account vs square/action button semantics; mega-nav for capability depth; stars pill as headline proof; token-driven link hovers.
- Do: keep `#a1a1aa` on dark only (fails on white); keep ambient motion to pulse/marquee/gradient-8s.
- Don't: add accent colors (blurple + green + ring-blue is the full budget); don't round product buttons into pills; don't slow 0.15s micro-motion.

## 8. Responsive Behavior

- 5-step ladder (1400→640) — mega-nav collapses to drawer; hero air compresses 128→48px; feature grids stack single-column.
- Touch: 8×16px buttons need 44px targets on mobile — verify before borrowing densities.

## 9. Agent Prompt Guide

- Quick reference: `developer-tools / midnight-zinc / product-funnel / dark / medium complexity / dual CTA (cloud signup + self-host)`.
- Ready-to-use prompt: "Design a self-hosting platform page in the Dokploy logic: pure black grounds with AAA zinc text, Lexend display at a single weight plus Inter body, inverted 6px square buttons where pills mean account and squares mean action, zinc hairline hierarchy, mega-nav capability depth, GitHub-stars headline proof, token-driven link hovers, inset dashboard-style depth, and a 5-step responsive ladder. Sell the dashboard by being the dashboard."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Black hero + stars pill — ownership + proof in one viewport.
2. Mega-nav (21 menus) — capability depth without scrolling.
3. Feature bands + code blocks — show, don't tell.
4. Pricing (`/pricing`, 9/9 WCAG) — packaging transparency.
5. Enterprise (`/enterprise`) — procurement trust.
6. Feature deep-page (75k chars) — SEO + evaluation depth.
7. Contact (`/contact`, zinc inputs) — capture close.

### 11. Pattern Position

- Fits the self-host funnel: own → explore (mega-nav) → evaluate (features, pricing) → procure (enterprise) → contact. Against Coolify (populist amber, community-first), Dokploy is systems-first — the pair covers the two self-hosting buyer psychologies.
- Page-flow logic: assume the buyer will self-host and needs procurement cover; enterprise page exists so champions can forward one link.

### 12. Synthesis Notes

- Unique (borrow as logic): landing-as-dashboard surface physics; pill/account vs square/action semantics; mega-nav as capability proof; stars-as-headline; Lexend-single-weight display; enterprise page as champion-enablement.
- Combine with: Coolify's philosophy/contributors trust layer (Dokploy is faceless — community would warm it) and Openship's ambient motion (Dokploy is statically confident).
- Avoid: copying black-zinc + Lexend verbatim (reads "Dokploy clone"); zinc secondary text on light; pill product buttons; hiding pricing or enterprise — transparency is the category contract.
