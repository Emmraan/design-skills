# Modals & Dialogs

Modals focus attention on one task and block everything else — use them **sparingly** and
follow strict interaction rules.

## When to use a modal (and when not)

| Use a modal | Instead use inline / navigation |
|---|---|
| Critical confirmation (delete, destructive) | Long forms (modals hate long forms) |
| Quick focused task (rename, share, add item) | Read-heavy content |
| Login / signup (compact) | Documentation, comparisons |
| Interruption (must-decide) | Settings with many fields |

Rule of thumb: if the task needs scrolling > 1 viewport, it doesn't belong in a modal.

## Anatomy

```
┌──────────────────────────────────────┐
│  Title                      [× close] │
│  ─────────────────────────────────── │
│  Content (focused, compact)           │
│  ─────────────────────────────────── │
│            [Cancel]  [Primary action] │
└──────────────────────────────────────┘
dimmed backdrop covers the rest of page
```

- **Title** states the task. **Cancel + primary** buttons at the bottom (primary right).
- **Close ×** top-right, plus Esc and backdrop click (backdrop click can be disabled for
  critical confirmations).
- Destructive actions: the primary button is styled as danger, with a clear sentence
  ("Delete 3 members — this can't be undone").

## Accessibility (non-negotiable)

1. Use native `<dialog>` or a `role="dialog"` + `aria-modal="true"`.
2. **Focus moves into** the dialog on open (first focusable or the dialog itself).
3. **Focus is trapped** inside while open (Tab cycles within).
4. **Esc closes**; focus returns to the trigger element on close.
5. `aria-labelledby` → title, `aria-describedby` → content (optional but good).
6. Backdrop is inert to pointer AND keyboard (`inert` or `aria-hidden` siblings).

## Motion

- Backdrop: fade (200ms). Panel: scale/slide in (300-400ms), ease-out.
- On close: quick fade-out (150-200ms). Respect reduced-motion.

## Anti-patterns (never copy)

- Modals stacked on modals.
- Modal that can't close (no ×, no Esc, backdrop click ignored on a non-critical modal).
- Focus not trapped (tab escapes behind the modal).
- Long forms in a modal (scroll inside modal is a smell).
- Auto-opening modals on page load (except genuine gating, and even then offer dismiss).
