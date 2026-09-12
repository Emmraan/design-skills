# Context.dev — Design Analysis

> Source: `https://www.context.dev/` ("Every piece of web context your agent needs" — web-context API for AI agents) · Baseline: `baseline.json` · Collected: 2026-09-12 (Dembrandt 0.32.2, 5 pages: `/` at 335k chars, `/pricing`, `/contact`, `/startup-discount`, `/blog` at 470k chars)

Context.dev is agent-native marketing: a "Copy agent setup prompt" button (89.1px radius) as a first-class CTA, dynamic OG images per headline (`/api/og?title=`), customer stories from agent-era companies (Mintlify, Daily.dev, Propane), and a rainbow gradient token system (red→violet→blue→cyan→lime) over IBM Plex Sans/Mono. Against Context7's stone calm (same problem space, opposite temperament), this is the expressive pole of AI context infrastructure.

## 1. Visual Theme & Atmosphere

- Mood: bright laboratory whiteboard — white grounds, rainbow gradient energy, dashed hairlines, spinning badges.
- Philosophy: sell to the builder AND their agent — human copy, machine-copyable prompts, dynamic social cards for every headline.
- Dashed-border signature (10% black dashes on paragraphs, 25% on spans) — technical-drawing energy no other reference has.

## 2. Color Palette & Roles

- Brand: blue `#2563eb` (logo 31px SVG) + accent `#268bff` (AA-large on tint) + deep `#1546af` + text `#030712` (20.13 AAA on white).
- Rainbow gradient tokens: `--color-1` red `#ff4242` → `--color-2` violet `#a142fe` → `--color-3` `#40a1ff` → `--color-4` cyan `#43d0ff` → `--color-5` lime `#a0ff42` (20 homepage gradients) — the spectrum IS the brand.
- Supporting: emerald `#00bc7d`, sky `#60a5fa`, hairline `#e5e7eb`, muted `#4b5563` (AA) / `#99a1af` / `#9ca3af`.
- Known fails: `#444444` on brand-blue 1.88, `#8c8c8c` AA-large-only — decorative gradient-zone text.

## 3. Typography Rules

- Voice: IBM Plex Sans 500–800, 54→5px (21 steps) — technical humanism, engineered warmth.
- Code: IBM Plex Mono 500/600 at display sizes too (43/32/25px mono headlines!) — mono as display voice, not just code.
- ui-monospace micro-captions (11→8px). Borrow Plex pairing for infra; borrow mono-display for agent-native attitude.

## 4. Component Stylings

- Agent CTA: "Copy agent setup prompt" (89.1px dark pill) — the machine is a user with a button.
- Buttons: 7+ variants — white 45px pills with layered micro-shadows, dark 45/89.1px closers, 9px mini-cards. Radius encodes voice (89.1 = agent, 45 = human, 9 = UI).
- Story cards: 21.6px radii with customer names (Mintlify, Daily.dev, Propane) — proof as gallery.
- Inputs: tight 3.6×10.8px, 5.4/7.2px radii — compact, frequent, unbothered.
- Links: 8 styles with oklab-underline treatments — underlines as tint, not lines.
- Favicon/PWA kit complete + dynamic per-title OG API.

## 5. Layout Principles

- 0.9x fractional spacing (10.8/14.4/7.2/5.4/3.6/2.7/1.8px + 72/36/43.2px) — zoom-compensated system, the most distinctive spacing in the repo.
- Funnel: gradient hero → agent-prompt CTA → stories → pricing → startup-discount → blog depth → contact.
- Startup-discount as a page (not a banner) — segment capture with dignity.

## 6. Depth & Elevation

- 51 homepage shadows: layered 2–4% micro-shadows + display-p3 ink shadows + inset rings — the deepest flat-white elevation in the repo, built from dust, not drops.
- Decision: white can have depth without grey — stack translucent micro-layers.

## 7. Do's and Don'ts

- Do: AAA ink-on-white anchors; rainbow reserved for gradients (never body text); dashed hairlines as brand; agent-prompt CTA; dynamic OG per headline; startup page; fractional spacing rhythm.
- Do: keep muted greys large-or-decorative; keep mono-display intentional (43px mono shouts — use once).
- Don't: add a second brand blue (spectrum covers it); don't solid-ify the dashes (they're the signature); don't market to humans only — the agent reads too.

## 8. Responsive Behavior

- Single 600px breakpoint detected — verify tablet/mobile manually before borrowing layout; fractional spacing scales cleanly by ratio.
- Touch: 45/89.1px pills are thumb-first; compact inputs need 44px targets on mobile.

## 9. Agent Prompt Guide

- Quick reference: `ai / gradient-plex / product-funnel / light / high complexity / dual CTA (copy agent prompt + pricing)`.
- Ready-to-use prompt: "Design an AI-agent-infrastructure page in the Context.dev logic: white grounds with AAA ink text, one brand blue plus a red-to-lime rainbow reserved for gradients, IBM Plex Sans voice with Plex Mono used at display sizes, dashed hairline borders as brand signature, a copy-agent-prompt pill CTA treating the machine as a user, radius-coded button voices, story-card proof gallery, layered micro-shadow depth on white, fractional 0.9x spacing rhythm, dynamic per-headline social cards, and a startup-discount page. Sell to the builder and their agent."

---

## Extended (synthesis-focused, keep these — they drive originality)

### 10. Component Map

1. Gradient hero + agent-prompt pill — dual-audience statement.
2. Story gallery (21.6px cards) — agent-era proof.
3. Pricing (`/pricing`, 39/50 WCAG) — packaging transparency.
4. Startup-discount — segment capture.
5. Blog (`/blog`, 470k chars) — depth moat.
6. Contact (`/contact`, compact inputs) — capture close.

### 11. Pattern Position

- Fits the AI-infra pattern: electrify (rainbow) → equip (agent prompt) → prove (stories) → package (pricing) → deepen (blog). Against Context7 (same category, stone ledger calm), this is maximalist light — the pair is a complete study in infra temperament.
- Page-flow logic: assume the buyer evaluates during a hackathon; everything must copy, paste, and run in minutes.

### 12. Synthesis Notes

- Unique (borrow as logic): agent-as-user CTA; dynamic OG API; dashed-border brand; mono-at-display-sizes; radius-coded voices; fractional spacing; micro-layer white depth; startup-discount page; rainbow-as-brand (not accent).
- Combine with: Context7's ledger restraint for pricing/packaging clarity (expression for hero, calm for contracts) and devtool changelog patterns for freshness proof.
- Avoid: copying Plex + rainbow + dashes verbatim (reads "Context clone"); rainbow body text; solid borders by default; human-only copy — the agent is in the room.
