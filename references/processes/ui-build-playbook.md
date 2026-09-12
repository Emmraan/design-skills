# UI Build Playbook — Frontier Process for Original, Human UI

> version: 1.1.0 · updated: 2026-09-12
> evidence-from: claude-v1.md, astra-v1.md (3 landing briefs × 2 families,
> output-conformance checked) + GLM-5.3 A/B gate (brief D baseline vs
> playbook-run; gate rules tagged `gate-evidence`)
>
> Every rule carries an evidence grade: `both-confirm` (both families converge —
> strong), `single` (one family — provisional, marked), `contested` (families
> differ — both options + condition; none in v1).
>
> Caveat (adopted from Astra): visual polish cannot be honestly verified without
> seeing the rendered result. Reason about quality, then inspect at real
> viewport sizes.

## How to use this playbook

Read this file before generating any UI, alongside the retrieved site analyses.
Follow the phases in order. Weaker models: treat checklists as mandatory — they
encode the judgment frontier models apply implicitly.

## Phase 1 — Brief lock

- Reduce the brief to one user + one task + one success condition. If the
  primary action can't be stated in one sentence, the brief isn't ready
  [`both-confirm`].
- Separate supplied facts from assumptions. Never present an assumption
  (pricing, integrations, metrics, workflows) as product truth; label it or
  fence it as placeholder [`both-confirm`].
- When proof is missing (customers, metrics, price), ship an evidence-ready
  template + pre-launch replacement panel — never realistic-looking fiction.
  Named fake people, quotes, and logos read as real; that is fabrication, not
  placeholder [`gate-evidence`].
- Name the user's decision anxiety ("will this work with my stack?", "can I
  trust this with my data?") — it decides what proof the page needs
  [`both-confirm`].
- Translate vague adjectives (premium, modern, clean) into observable choices:
  density, contrast, materiality, type scale, image treatment [`single-Astra`].
- Ask only questions that change structure or visual direction; otherwise pick
  a conservative default and label the uncertainty [`both-confirm`].

## Phase 2 — Design-language lock

- Write a visual thesis phrase first ("quiet operational confidence") and let
  it arbitrate every later choice [`both-confirm`].
- Retrieve 3+ references and extract LOGIC, not values. Then commit: hero
  composition, section rhythm, color voice, type voice, motion language — each
  with a one-line why [`both-confirm`].
- Define semantic color roles before choosing attractive colors: canvas,
  surface, primary/muted text, border, action, focus, success, warning, danger.
  Strong accent reserved for action and real status [`both-confirm`]. A second
  accent needs a second job — decorative second hues get cut [`gate-evidence`].
- Limit visual voices: one display treatment, one body treatment, one accent
  behavior, one surface model [`single-Claude`].
- Choose one or two signature compositional devices that fit the product —
  never a pile of decorative effects [`single-Astra`].
- Differ from every single source in at least 2 of layout, color, typography.
  Originality comes from product-specific specificity (hierarchy, hero visual,
  data representation, density), not novel chrome [`both-confirm`].

## Phase 3 — Compose

- Give every region one job (orient, explain, prove, compare, act, recover).
  Remove regions with no distinct job; never add a section because pages
  "usually have one" [`both-confirm`]. Numbered grids (01–04) with identical
  internal structure are cards in disguise — vary module shape AND internal
  structure [`gate-evidence`].
- Compose the highest-value moment first (hero + conversion path), with real or
  realistically constrained content — never lorem-block layouts [`both-confirm`].
- Hero visual must do a product job: show a meaningful state, workflow, or
  artifact — not a decorative dashboard [`both-confirm`].
- Hierarchy via position, scale, contrast, whitespace, grouping — before
  borders, shadows, badges, color [`both-confirm`].
- One dominant visual anchor per major viewport; one primary action per
  decision point, secondary actions quiet [`single-Astra` + `both-confirm`].
- Assemble with the closest `references/patterns/` pattern, tokens from
  `references/design-tokens/`, components from `references/components/`, a11y
  from `references/accessibility/`. One coherent language throughout
  [`both-confirm`].

## Phase 4 — De-AI pass (hard gates)

- **Copy pass:** run `references/copywriting/human-copy.md` audit gate on every
  string. Zero negation pivots, zero placeholder copy, anchors everywhere.
  CTA names the outcome; claims stay proportional to evidence [`both-confirm`].
- **Design pass:** run the review-checklist De-AI section. No centered-default
  layouts, no generic gradients, no template card grids, no stateless buttons,
  no missing focus/hover/loading/empty/error states [`both-confirm`].
- **Uniqueness check:** transplant test — "could this belong to any company?"
  If yes, rewrite or remove [`single-Claude`]. Record varied levers + why they
  fit THIS surface.

## Phase 5 — Critique, subtract, polish

- Run separate passes, never one vague review: task clarity, hierarchy, visual
  coherence, content truthfulness, accessibility, responsive behavior
  [`single-Astra`].
- Squint test (message, action, groupings survive at a glance) + scan test
  (labels/headings/CTAs/data alone tell the story) + grayscale check
  (hierarchy survives without hue) [`single-Astra`]. Extend the scan test to
  self-consistency: artifact details must agree with surrounding copy — names,
  dates, days, numbers, states (a Saturday alert next to a Mon–Fri grid fails)
  [`gate-evidence`].
- Subtract before adding: delete at least one nonessential treatment; first
  drafts typically lose 20–35% [`single-Claude`].
- Check the result at full page, first viewport, narrow mobile, and zoomed-in
  component state — at real viewport sizes, not a zoomed-out canvas
  [`single-Claude` + `single-Astra`].
- Align repeated elements (type, radii, borders, shadows, spacing, icon and
  interaction vocabulary) into one system [`both-confirm`].
- Tighten copy against the final layout; a headline that wraps badly or
  overclaims is not final [`single-Astra`].
- Record the synthesis note (which reference gave which logic) and any
  unresolved product decisions — honestly labeled, never concealed
  [`single-Astra`].

## Phase 6 — Edge states + honest delivery

- Cover empty, loading, error, success, permission-limited, and long-content
  states for primary flows before calling the result complete [`both-confirm`].
- Destructive actions visibly distinct; system status in actionable language
  ("sync failed 12 minutes ago", not a vague red dot); status never color-alone
  [`single-Claude`].
- Mobile is recomposition: message → action → cropped artifact; tables become
  labeled rows; plans become separate blocks [`both-confirm`].
- Never claim visual testing, accessibility audit, or user testing that didn't
  happen [`single-Astra`].

## Surface annex — Landing (v1)

Narrative sequence: claim → proof → mechanism/product evidence → objections →
conversion [`both-confirm`]. Thought path: "for someone like me" → "looks
easy" → "handles what I dislike" → "I can start" → "cost is reasonable" →
"concerns answered" [`single-Astra`]. Trust-forward surfaces earn trust through
clarity and labeled placeholders, never fabricated logos, metrics, or quotes
[`both-confirm`].

## Surface annexes — Dashboard, sidebar/nav-shell, profile, settings (v2)

Astra's surface-emphasis rows (scan order + exception handling for dashboards;
mental-model grouping + consequence disclosure + save-state clarity for
settings) are recorded in `astra-v1.md` signal 12 — unconfirmed by outputs
(landing-first scope). They distill into annexes once app-surface briefs run.
