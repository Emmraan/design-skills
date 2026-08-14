# Feedback & Loading

Users need to know the system is alive. **Visible system status** is a core usability law:
every action needs a response, and every wait needs an indication of progress.

## Feedback types

| Moment | Feedback |
|---|---|
| Button pressed | Immediate visual state change (depressed, loading spinner inside) |
| Form submit | Progress → success or inline error; never silent |
| Save/autosave | "Saving…" → "Saved" (with timestamp) |
| Long operation | Progress bar / percentage, not infinite spinner |
| Delete/destructive | Confirmation dialog (undo where possible) |
| Action complete | Success toast/checkmark (auto-dismiss, polite) |
| Async/background | Toast/banner with a "view" or "dismiss" action |

## Loading states (choose the right one)

| State | Duration | Pattern |
|---|---|---|
| Instant actions | < 300ms | No loader; just the state change (spinner flashing is worse) |
| Short wait | 300ms-1s | Inline spinner in the button, disable input to prevent double-submit |
| Medium | 1-3s | Skeleton screens (matching real layout) beat spinners |
| Long | > 3s | Progress bar + percentage + cancel option |

**Skeletons > spinners:** a skeleton that mirrors the final layout (text bars, image blocks)
reduces perceived wait and prevents layout shift. Dembrandt/design analyses note the loading
approach of reference sites for a reason.

## Rules

1. **Every button press changes something** within ~100ms (even just an active state).
2. **Never leave an action unacknowledged** — silent failures are the worst UX.
3. **Prevent double-submit** on forms/checkout (disable while pending).
4. **Errors are helpful:** say what happened and how to fix it ("Enter a valid email").
5. **Toast placement** bottom-right (or top-center on mobile); don't cover primary CTAs.
6. **`aria-live="polite"`** for toasts; `role="alert"` for errors (see `semantics-aria.md`).
7. Respect **`prefers-reduced-motion`** (no busy shimmer; static skeleton).

## Anti-patterns (never copy)

- Endless spinners with no progress indication.
- Loading that causes layout jump (content shifts when data arrives).
- "Success" with no confirmation or way to verify.
- Errors with no guidance ("Something went wrong" alone).
- Buttons that let users submit 3 times while "loading".
