# Semantics & ARIA

Semantic HTML is the accessibility foundation; ARIA is a supplement when native semantics
can't express something. Use **native elements first**, ARIA only as a patch.

## Page structure (landmarks)

```
<header>   ← site header (nav, logo)
<nav>      ← primary navigation (label if multiple navs: aria-label="Main")
<main>     ← one per page, skip target
  <h1>     ← one per page
  <section aria-labelledby="…">  ← each meaningful block has a heading
<footer>
```

- Heading levels must not skip (`h1` → `h2` → `h3`, no `h3` right after `h1`).
- Sections that are independently meaningful get an accessible name (heading or
  `aria-label`).

## Element choices (use native controls)

| Task | Use | Avoid |
|---|---|---|
| Action | `<button>` | `<div onclick>` |
| Navigation | `<a href>` | `<div role=button>` for links |
| List | `<ul>/<ol>/<li>` | `<div>` chains |
| Form input | `<input>`, `<select>`, `<textarea>` | custom divs |
| Accordion | `<details>/<summary>` or buttons + `aria-expanded` | divs with click |
| Modal | `<dialog>` or role=dialog + focus trap | invisible overlay div |
| Tabs | buttons + `role=tablist/tab/tabpanel` | clickable headings |

## Form labeling

```html
<label for="email">Work email</label>
<input id="email" name="email" type="email" required>
<!-- error -->
<p id="email-error" role="alert">Enter a valid email.</p>
<input id="email" aria-describedby="email-error" aria-invalid="true">
```

- Every field has a visible `<label>`; placeholder is never a substitute.
- Errors: `role="alert"` (or `aria-live="assertive"`) + `aria-describedby` linking to the field.
- Group related fields with `<fieldset>`/`<legend>`.

## ARIA usage rules

1. **Don't add ARIA to native elements** (`<button role="button">` is noise).
2. **`aria-hidden="true"`** on purely decorative content/icons.
3. **`aria-expanded`** on disclosure toggles (accordions, menus, mobile nav).
4. **`aria-current="page"`** on the active nav item.
5. **`aria-label`** on icon-only buttons (share, close, menu).
6. **Live regions sparingly** — `aria-live="polite"` for toasts/notifications;
   `role="alert"` for errors. Don't announce everything.
7. Icon buttons: include accessible name (`aria-label` or visually-hidden text).

## Color is never the only signal

- Errors: icon + text + color (not just red border).
- Links vs body: underline or other non-color cue.
- Active states: not just a color change.
- Charts/status: label + pattern + color.

## How to read (for analysis)

- Does the site use landmarks + a single h1 with clean heading order?
- Are interactive elements native or div-based?
- Are forms labeled + errors announced?
- Is ARIA minimal and correct (not bolted onto natives)?

## Anti-patterns (never copy)

- `div`-on-click buttons everywhere.
- Multiple `h1`s or skipped heading levels.
- Unlabeled icon-only buttons.
- `aria-live` on everything (screen-reader spam).
- Toggle switches with no visible state label.
