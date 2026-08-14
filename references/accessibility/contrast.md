# Contrast

Contrast is the single most common accessibility failure and the easiest to prevent if you
treat it as a token-level rule, not a final audit.

## WCAG 2.1 ratios (quick reference)

| Use | Ratio | Example |
|---|---|---|
| Body text / normal text | **4.5:1** | 16px paragraph on a surface |
| Large text (≥24px, or ≥18.66px bold) | **3:1** | Hero headline |
| UI components (borders, icons with bg) | **3:1** | Button, input border, icon |
| Graphics required to understand | **3:1** | Chart, infographic |

Ratio is calculated between **foreground and the actual background behind it** — not against
white. On gradients, images, or dark cards this is where failures hide.

## Practical rules

1. **Text neutrals are a scale.** Build a tinted gray scale (toward your brand hue) with
   *guaranteed* ratios: e.g. body text at least 4.5:1 against the lightest surface it can sit
   on.
2. **Never put body text on your primary color.** Primary is for CTAs/large text; a small
   white label on a mid-tone primary can fail 4.5:1.
3. **White on brand:** check it. Many bright/neon accents fail AA for small white text —
   use them for large type, icons, or as decorative color with proper text on neutral.
4. **Focus rings:** ≥3:1 against adjacent background — test on each surface color.
5. **Disabled states** are exempt from 4.5:1 but should still be readable (≥3:1, and never
   rely on color alone to signal disabled).
6. **Dark themes flip the problem:** light gray text on near-black is fine; mid-gray on
   near-black can fail — test.

## Useful ratio pairs (examples)

| Foreground | Background | Ratio |
|---|---|---|
| `#111827` (near-black) | `#ffffff` | ~17:1 ✅ |
| `#6b7280` (gray-500) | `#ffffff` | ~4.6:1 ✅ body |
| `#9ca3af` (gray-400) | `#ffffff` | ~3.0:1 ⚠️ large only |
| `#ffffff` | `#4f46e5` (indigo-600) | ~5.6:1 ✅ |
| `#ffffff` | `#6366f1` (indigo-500) | ~4.1:1 ⚠️ large only |
| `#f5f5f7` | `#0a0a0a` | ~18:1 ✅ |

## How to validate

- Automated: Dembrandt `--wcag` walks the real DOM and reports every text/bg pair + grades
  (use this in `add.py`/`update.py`).
- Manual: a contrast checker (WCAG AA) against the *real* rendered background.
- During generation: choose neutrals that pass by construction, verify accent-on-surface pairs
  before shipping.

## Anti-patterns (never copy)

- Gray-500 body text on white "because it looks subtle" (fails 4.5:1 if below 18.66px bold).
- White text on saturated brand colors without checking.
- Decorative text (the whole paragraph) at 3:1 — only large text is exempt.
- Hover states that *drop* contrast (text turning lighter).
