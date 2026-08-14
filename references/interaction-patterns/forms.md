# Forms

Forms are where users abandon sites. Every field asks a question — keep the questions few,
clear, and painless.

## Structure

- **One column** for most forms (faster to complete than multi-column).
- **First name / last name → single "Full name"** where acceptable (one less field).
- **Group** related fields (`<fieldset>` + `<legend>` for radios/checkboxes).
- **Order flows** top-to-bottom like a conversation (email before password, address before city).

## Labels & fields

1. **Visible labels always** (placeholder is not a label). Top-aligned labels scan fastest.
2. **Only ask what you need.** Every extra field cuts conversion.
3. **Mark optional, not required** — when most fields are required, invert the convention.
4. **Correct input types** (`type=email`, `tel`, `number`) → right mobile keyboard + validation.
5. **`autocomplete`** for name/email/address/country — browsers prefill, users love it.
6. **Format expectations**: show format hints inline for phone/date/card numbers.

## Validation & errors

| State | Pattern |
|---|---|
| Valid | Subtle green check (optional, don't over-celebrate) |
| Invalid on blur | Inline error below the field + red border + error text |
| On submit | Focus the first failing field, scroll to it |
| Character limits | Live counter or format as-you-type (card numbers) |

- Error messages must say **what's wrong and how to fix it** ("Enter at least 8 characters").
- Never clear the user's input on error.
- `aria-invalid="true"` + `aria-describedby` linking error text (see `semantics-aria.md`).

## Buttons

- **Primary submit** is visually dominant and near the fields.
- Disable submit while validating/loading; prevent double-submit.
- Destructive forms (delete account): require confirmation, style danger, add a type-in
  confirm if irreversible ("type DELETE").

## Special cases

- **Password:** show/hide toggle (purely visual, keep accessible name), don't over-restrict
  rules ("at least 8 chars" is enough).
- **Checkbox consent:** label links to terms; keep it adjacent to submit.
- **Multi-step forms:** progress indicator, save state, allow back navigation without data loss.
- **Signup/CTA forms:** single field + button ("Enter your email → Get started") converts
  better than a full form.

## Anti-patterns (never copy)

- 12 fields for a "quick" signup.
- Errors only shown on submit and hidden after (no inline feedback).
- Label as placeholder only (disappears, no persistent label).
- Disabled submit button with no explanation of what's missing.
- No autocomplete support.
