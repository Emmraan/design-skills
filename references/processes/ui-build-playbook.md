# UI Build Playbook — Frontier Process for Original, Human UI

> version: 1.3.0 · updated: 2026-09-13
> evidence-from: claude-v1.md, astra-v1.md (3 landing briefs × 2 families) +
> GLM-5.3 A/B gate (brief D) + dashboard briefs E/F × both families +
> settings briefs G/H × both families
> (output-conformance checked; models worked from distilled recaps after
> original chats were deleted — recap-transfer validated by strong conformance)
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

## Surface annexes — Dashboard (v1.2.0)

Applies to monitoring/operations dashboards (support ops, cash ops, any
exception-driven work surface). Core phases hold; these rules specialize them.

### Ordering: exceptions before explanation

- Scan path: freshness/scope → current position → exceptions → approvals/
  decisions → supporting detail → trends/source-health [`both-confirm`].
- Trends and diagnosis support prioritization; they never compete with the
  exception queue for primacy [`both-confirm`].
- Landing-page storytelling structure must not leak into work surfaces
  [`both-confirm`].

### Regions with jobs

- Map regions to jobs: orient (global header), explain scope (dashboard
  header + filter context), prove condition (status overview), act (exception
  queue + approval queue), compare (trends), validate/decide (detail panel),
  recover trust (system feedback) [`both-confirm`].
- Status overview items are interactive filters that update queue + context —
  never decorative KPI tiles. Drop any metric that doesn't change staffing or
  decision action [`both-confirm`].
- Approval queue is its own decision region beside/below exceptions — never
  buried in a tab when a pending approval is itself a risk [`single-Claude`].

### Filter context honesty

- A plain-language scope sentence always accompanies filter controls; chips
  alone are insufficient and unclear in combination [`both-confirm`].
- When a filter makes a metric irrelevant, explain it inline (e.g. no SLA
  policy for this team) rather than showing dead numbers [`single-Claude`].
- Sort labels disclose the algorithm ("sorted by SLA risk, then priority");
  never imply a universal priority score [`single-Claude`].

### Queue discipline

- One dominant region; items appear once, ranked by most urgent condition,
  with reason tags for additional concerns [`both-confirm`].
- One dominant action per decision context; row action matches the most
  likely resolution (Review funding plan, Hold payment — not View)
  [`single-Astra`].
- Urgency/status always pairs color with icon + explicit text; never color
  alone, never red-green alone without target line + written value
  [`both-confirm`].
- Bulk actions appear only after selection; destructive actions live under
  overflow with consequence-confirmation, never beside routine actions
  [`single-Claude`].

### Detail preserves context

- Detail opens as a persistent side panel with the list visible behind it;
  focus moves to the detail heading and returns to the originating row on
  close [`both-confirm`].
- Detail action area maps record-state → primary CTA (unassigned → Assign
  owner; shortfall → Review forecast; failed payment → Open payment);
  vague labels (View details) fail [`both-confirm`].
- Audit history is a chronological text list; decorative timelines add
  nothing [`single-Claude`].

### Trust: freshness, fencing, uncertainty

- Freshness is decision-grade language (current / updating / last synced /
  source delayed), never a decorative dot; stale data keeps its timestamp so
  it can't be mistaken for current [`both-confirm`].
- Fence per value (`[live amount]`), not per document — blanket "all data
  fictional" headers let realistic fakes read as real inside the spec
  [`single-Claude`].
- Communicate uncertainty, never smooth it: forecast confidence breakdowns,
  "comparison unavailable" states, similarity framed as similarity (never
  fraud/duplication without evidence) [`both-confirm`].
- AI assistance is explicitly assistive and reviewable (verify-before-approve
  framing); never an accounting conclusion or verified instruction
  [`single-Astra`].

### Density and dark

- Dense by structure, not decoration: compact rows, stable alignment,
  right-aligned tabular numerals, progressive disclosure; routine detail
  quieter, high-risk items given line height + contrast [`both-confirm`].
- Dark must serve concentration (near-black blue-gray/charcoal, soft
  off-white text) — never pure black, never neon-danger shorthand; darkness
  is justified by environment and content, not sophistication signaling
  [`both-confirm`].

### Permissions and states

- Permission limits get precise language + scope notices (partial-view
  warning); never show company-wide totals for partial access; never expose
  enabled decision buttons without authority, and never disabled ones without
  explaining why [`both-confirm`].
- Fail by region with per-region retry; retain labeled stale data; empty
  states stay calm (small check icon, next action) — no celebration
  artwork [`both-confirm`].

### Mobile recomposition

- Recompose around next-exception/next-decision: header scope → position →
  exceptions → approvals → supporting detail; tables become labeled rows,
  never horizontal scrolls [`both-confirm`].
- Never hide scope, material impact, effective date, or approval authority on
  mobile; charts move below operational content with written summaries first
  [`single-Astra`].

## Settings annex

Distilled from settings briefs G (Helpdeskly team + access, light) + H
(Ledgerline billing + API security, dark) × Claude + Astra (4 outputs,
output-conformance checked — STRONG both families, zero contested, De-AI
clean). Promotes Astra `astra-v1.md` signal 12 settings rows from `single`
to `both-confirm`.

### Ordering and grouping

- Group by mental model, not by control type: account identity → team &
  access (primary surface, densest) → notifications → security; billing:
  plan health first → payment → API keys → danger zone last, isolated and
  separated [`both-confirm`].
- Ordinary sections stay deliberately quiet; remove promotional panels,
  health widgets, and decorative cards — density follows consequence, not
  decoration [`both-confirm`].
- Danger zone never shares a section with routine controls: red boundary,
  own heading, closing position [`both-confirm`].

### Consequence disclosure

- Every consequential control states its consequence inline, before
  confirmation: role change names before/after authority ("will no longer be
  able to manage…"); member removal states access timing + ticket
  disposition ("lose access immediately… past notes remain… not reassigned
  automatically") [`both-confirm`].
- Never merge distinct destructions: close workspace (stops operations,
  keeps data) vs delete data (scope + legal exclusions stated) are separate
  actions with separate gates [`both-confirm`].
- Billing timing is explicit: upgrade takes effect immediately and prorated;
  downgrade holds until the renewal date with new limits stated
  [`both-confirm`].

### Save-state clarity

- Quiet `Saved` at rest; persistent bottom bar for drafts —
  `Unsaved changes — [what changed]` + `Discard / Save changes`
  [`both-confirm`].
- `Saving…` disables only the affected section and keeps the bar; failure
  keeps edits in place with retry (`Changes weren't saved. Edits still
  here…`) [`both-confirm`].
- Leave-guard offers `Keep editing / Discard` — never a bare "Leave"
  [`both-confirm`].
- Transactional actions (create/revoke key, plan change, close/delete) are
  excluded from page-save; each confirms on its own [`both-confirm`].
- Never show green unless the server confirmed [`single-Claude`].

### Destructive gating

- Ordinary removal = confirmation dialog; blue for consequential change,
  red only for true loss [`both-confirm`].
- Impossible destructions are blocked with explanation, never faked:
  last-admin ("at least one admin required"), SSO-managed ("remove in
  identity provider — no local action") [`both-confirm`].
- Irreversible actions need typed gates (`Type DELETE [name]`) and
  multi-step flows; never a lone disabled red button
  [`both-confirm`].

### Permission views

- Never show enabled decision buttons without authority, and never
  disabled ones without explaining why: non-admins see a `My access`
  summary (role, scope, allows/does-not-allow, who to contact) instead of
  admin controls [`both-confirm`].
- Restriction notices on deep links (`Team management is restricted… View
  my access`) — no silent redirects [`both-confirm`].
- Viewers never see secret fragments; key management hides entirely
  without permission [`both-confirm`].

### Secrets and billing meters

- API keys reveal once: masked by default, `Create and reveal`, `Copy key /
  Copied`, "stored securely" acknowledgement, leave-without-copying guard;
  `Rotate` is never `Edit`; revoked keys stay listed; a failed revocation
  never claims revoked [`both-confirm`].
- Usage meters are label + exact used/included counts + reset date with a
  secondary bar — horizontal rows, never radial gauges; threshold copy
  states what remains; unavailable meters show a timestamped notice, never
  zeros; forecasts appear only if calculable [`both-confirm`].

### Settings mobile

- Navigation collapses to a `Settings sections` index list; member/key
  edits and all confirmations become full-screen task views; tables become
  labeled rows [`both-confirm`].
- The save bar pins above the safe area only while a draft exists;
  destructive actions stay separated with identical gates
  [`both-confirm`].

## Surface annexes — Sidebar/nav-shell, profile (later)

Sidebar/nav-shell and profile await their briefs.

## Composing a surface with no annex (mandatory protocol)

If the surface you must build has no annex above, do NOT improvise outside
this playbook. Compose it:

1. **Pick the nearest annexes.** Map the surface to composed patterns, e.g.
   date-picker → dashboard ordering + table discipline + detail actions;
   in-app comments → detail panel + feedback states; pricing-as-app → billing
   logic + list discipline; search results → table discipline + empty states.
2. **Run all 6 core phases** with the composed rules treated as provisional
   (`single`-grade at best — say so in your synthesis note).
3. **De-AI pass and review-checklist gates are non-negotiable** — composition
   never exempts copy, design-tell, or state-coverage gates.
4. **Record the mapping and its gaps** in your synthesis note: which annex
   gave which logic, what the composition couldn't cover.
5. **Promotion trigger:** when the same unlisted pattern is needed by a second
   surface, stop composing and propose a dedicated annex (new briefs → both
   families → distill + changelog, same as A16–A21 were born). Log the
   proposal in `process-changelog.md` even before the annex exists.
