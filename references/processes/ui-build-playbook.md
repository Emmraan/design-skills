# UI Build Playbook — Frontier Process for Original, Human UI

> version: 0.1.0 · updated: 2026-09-12
> evidence-from: none yet (skeleton — frontier-derived rules land in v1.0 after
> observations; every rule will carry an evidence grade:
> `both-confirm` / `single` / `contested`)
>
> Status: **skeleton**. Core phases and the De-AI pass are defined from repo
> principles. Frontier-derived rules (how Claude-family and GPT-family actually
> build) arrive via `claude-v1.md` + `astra-v1.md` and distill into v1.0.

## How to use this playbook

Read this file before generating any UI, alongside the retrieved site analyses.
Follow the phases in order. Weaker models: treat checklists as mandatory — they
encode the judgment frontier models apply implicitly.

## Phase 1 — Brief lock

- Restate in one line: this surface exists to help [audience] [outcome] by
  [mechanism], and should feel [3 quality words].
- Fix scope: surface type (landing / dashboard / settings / profile / nav-shell),
  sections needed, theme, tone, constraints (framework, a11y, speed).
- Do not proceed with an ambiguous brief — ask 2–4 targeted questions first.

## Phase 2 — Design-language lock

- Retrieve 3+ references (websites + pattern + components) and extract LOGIC,
  not values: layout flow, spacing rhythm, type pairing, color roles, motion.
- Commit before composing: hero/surface composition, section rhythm, color
  voice, type voice, motion language — each with a one-line why.
- Deliberately differ from every single source in at least 2 of layout, color,
  typography. Cross-pollinate categories.

## Phase 3 — Compose

- Assemble with the closest `references/patterns/` pattern, tokens from
  `references/design-tokens/`, components from `references/components/`, a11y
  from `references/accessibility/`.
- One coherent language: one spacing scale, one type system, one color-role
  grammar. Ship real, responsive code.

## Phase 4 — De-AI pass (hard gates)

- **Copy pass:** run `references/copywriting/human-copy.md` audit gate on every
  string. Zero negation pivots, zero placeholder copy, anchors everywhere.
- **Design pass:** run the review-checklist De-AI section. No centered-default
  layouts, no generic gradients, no template card grids, no stateless buttons,
  no missing focus/hover/loading/empty/error states.
- **Uniqueness check:** record the varied layout levers and why they fit THIS
  surface. If the result could be described as "like X but reskinned", redo it.

## Phase 5 — Critique passes

- Self-review against `references/prompts/review-checklist.md`: originality,
  a11y AA, responsiveness, content structure, code hygiene.
- Frontier-derived critique moves land here in v1.0 (pending observations).

## Phase 6 — Polish

- Final sweep: tokens reused (no inline value sprawl), performance sane,
  reduced-motion respected, synthesis note recorded (which reference gave which
  logic).

## Surface annexes

- Landing (v1): full annex arrives with v1.0 distillation.
- Dashboard, sidebar/nav-shell, profile, settings (v2): annexes arrive with
  app-surface observations. Process core above already applies to them.
