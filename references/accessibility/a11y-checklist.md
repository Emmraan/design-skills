# Accessibility Checklist

Run this on **every** generated website. A design that isn't accessible isn't done.

## 1. Contrast
- [ ] Body text: **4.5:1** against its background (WCAG AA).
- [ ] Large text (≥24px or ≥19px bold): **3:1**.
- [ ] UI components / icons with a border or background: **3:1**.
- [ ] Test on the actual background (not just white). See `contrast.md`.

## 2. Focus
- [ ] Every interactive element has a **visible focus indicator** (never `outline: none` alone).
- [ ] Focus ring contrast ≥3:1 against adjacent background.
- [ ] Logical focus order follows visual order (DOM order).

## 3. Keyboard navigation
- [ ] All functionality reachable by keyboard (Tab, Enter, arrows, Esc).
- [ ] No keyboard traps (including modals — trap within, Esc closes).
- [ ] Skip-link to main content at top of page.
- [ ] Dropdowns, menus, accordions open/close with keyboard.

## 4. Semantic HTML & ARIA
- [ ] Landmarks: `<header>`, `<nav>`, `<main>`, `<footer>`, sections with headings.
- [ ] One `<h1>` per page; heading levels don't skip (`h1 → h2 → h3`).
- [ ] Buttons are `<button>`, links are `<a href>`. Don't use `<div onclick>`.
- [ ] Forms: `<label>` for every field, associated correctly; error text linked via
      `aria-describedby`.
- [ ] Use native HTML before ARIA (checkboxes, tabs with `role=tablist` only when needed).
- [ ] Images: meaningful `alt`, empty `alt` for decorative, `aria-hidden` for icons.
- [ ] Color alone never conveys meaning (add icon/text). See `semantics-aria.md`.

## 5. Forms
- [ ] Labels visible (placeholder is not a label).
- [ ] Inline validation on blur, clear error messages with instructions to fix.
- [ ] Mark **optional** fields, not required ones (unless most are optional).
- [ ] Error summary links to the failing field.
- [ ] Inputs have `name`, correct `type` (email, tel, password) for mobile keyboards.

## 6. Motion & media
- [ ] `prefers-reduced-motion` respected — reduce/disable animation.
- [ ] No flashing content >3 times/sec (can trigger seizures).
- [ ] Carousels/sliders: pause, stop, hide controls; manual control required.
- [ ] Video: captions; audio: transcript.

## 7. Touch & targeting
- [ ] Touch targets ≥ **44×44px** (or 24px minimum with 8px spacing).
- [ ] Sufficient space between tappable elements.

## 8. Content & language
- [ ] `<html lang>` set correctly.
- [ ] Descriptive link text ("Read pricing" not "click here").
- [ ] Page `<title>` + meta description on every page.

## 9. Responsive + zoom
- [ ] Works at 200% browser zoom and 320px width without horizontal scroll.
- [ ] Text resizable (no fixed body font-size in px blocking zoom).

---

## Minimal pass (if time is short)
Contrast ≥AA · visible focus · keyboard operable · labeled forms · `prefers-reduced-motion`.
Skip none of these five — they cover the vast majority of real accessibility failures.
