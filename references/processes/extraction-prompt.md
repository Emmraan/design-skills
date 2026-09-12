# Frontier Extraction Prompt (give this to BOTH models, web UI chat)

> Status: draft — awaiting user review before use. Give the same prompt to
> Claude-family (Fable) and GPT-family (Astra) so answers are comparable.
> If a model cannot fetch a link, paste that file's contents into the chat.

---

Copy everything below the line into the chat:

---

I want to learn YOUR working process for building high-quality website UI —
not code, but the method you follow. Please read these first (same repo,
a design knowledge base I maintain):

- https://github.com/Emmraan/design-skills/blob/main/SKILL.md
- https://github.com/Emmraan/design-skills/blob/main/references/prompts/generation-prompt.md
- https://github.com/Emmraan/design-skills/blob/main/references/prompts/synthesis-rules.md
- https://github.com/Emmraan/design-skills/blob/main/references/copywriting/human-copy.md

Then describe, in this exact structure:

1. **Phases.** The ordered phases you go through from receiving a brief to
   delivering finished UI (e.g. brief analysis, planning, design-language
   decisions, composing, self-critique, polish). Name each phase and what
   visibly changes in the output because of it.
2. **Per-phase rules.** For each phase: 3–6 concrete rules or checks you apply.
   Rules must be actionable ("do X / never do Y"), not vague ("make it good").
3. **Design-language decisions.** How do you choose layout composition, spacing
   rhythm, type pairing, color roles, and motion for a NEW brief — and how do
   you keep the result original rather than template-like?
4. **De-AI moves (design).** What specific moves keep your UI from looking
   AI-generated? List the tells you actively avoid and what you do instead.
5. **De-AI moves (copy).** How do you write on-page copy (headlines, CTAs,
   feature text) so it reads human, not generated? List patterns you avoid and
   your grounding/voice rules.
6. **Self-critique.** Before delivering, what do you check, and what most often
   fails your own check? Be specific.
7. **Anti-patterns.** 5+ things you see in weak AI-built UI (design + copy)
   that you never ship.

Constraints: be concrete and honest about what you ACTUALLY do, not an
idealized process. If a step varies by surface (landing vs dashboard vs
settings), say how. No code samples — process only.

---

## Standard v1 briefs (same briefs to both models, landing-first)

After the process answer, ask each model to build the SAME brief, one at a
time (outputs are checked for conformance with its stated process):

- **Brief A (saas):** Landing page for a fictional invoicing tool for
  freelancers. Light theme, minimal premium tone. Sections: hero, social proof,
  features, how-it-works, pricing, faq, final CTA.
- **Brief B (ai):** Landing page for a fictional meeting-notes AI. Dark theme,
  bold tone. Sections: hero with product visual, logos, features, testimonial,
  pricing, faq, CTA.
- **Brief C (fintech):** Landing page for a fictional expense-card startup.
  Light theme, trust-forward tone. Sections: hero, trust band, features,
  metrics, testimonials, pricing, faq, CTA.

Record for each output: which stated-process steps are visible in the output
(`confirmed`), which are missing (`gap`). Gaps demote claims to provisional.

## Standard v2 briefs (dashboard — one surface at a time, same protocol)

Run each brief on BOTH models in fresh chats. Instruction line to prepend:
"Apply the UI process you described earlier in this chat. Full dashboard
direction with copy, states, and responsive behavior — no code."

- **Brief E (ops, light):** Operations dashboard for Helpdeskly, a fictional
  SaaS support tool. Light theme, calm-dense tone. Must cover: status overview,
  exception queue (SLA breaches, unassigned), trends, ticket detail moment,
  empty/loading/error states, filter context, keyboard + reduced-motion notes.
- **Brief F (fintech, dark):** Cash-flow operations dashboard for fictional
  Ledgerline (same product world as v1 Brief C). Dark theme, precise tone.
  Must cover: current position, anomaly/exception list, approval actions,
  supporting detail, empty/loading/error/permission states, density + scan
  order rationale, reduced-motion notes.

Save outputs as `output/dashboard/claude-dashboard-E.txt`,
`output/dashboard/claude-dashboard-F.txt`,
`output/dashboard/astra-dashboard-E.txt`,
`output/dashboard/astra-dashboard-F.txt` (2 briefs × 2 models = 4 runs).
Distillation promoted Astra signal 12 dashboard rows to `both-confirm` in
playbook v1.2.0; settings rows stay `single` until app-settings briefs run.
If the original process chat was deleted, precede each brief with the
family-specific recap block (see chat history) instead of the "described
earlier" line.

## Standard v3 briefs (settings — one surface at a time, same protocol)

Run each brief on BOTH models in fresh chats. Instruction line to prepend:
"Apply the UI process you described earlier in this chat. Full settings
direction with copy, states, and responsive behavior — no code."

- **Brief G (team access, light):** Team + access settings for Helpdeskly
  (same product world as v2 Brief E). Light theme, calm-admin tone. Must
  cover: mental-model grouping (account/team/notifications/security),
  role-change + member-removal consequence disclosure, save-state clarity
  (saved/saving/unsaved/discard), non-admin permission view, destructive
  gating, empty/loading/error states, keyboard + reduced-motion notes.
- **Brief H (billing + secrets, dark):** Billing + API-security settings for
  fictional Ledgerline (same product world as v1 Brief C / v2 Brief F).
  Dark theme, precise tone. Must cover: plan + usage meters, payment
  methods, API-key lifecycle (create/reveal/revoke), danger zone
  (close workspace / delete data) with consequence disclosure, unsaved-change
  handling, empty/loading/error/permission states, reduced-motion notes.

Save outputs as `output/settings/claude-settings-G.txt`,
`output/settings/claude-settings-H.txt`,
`output/settings/astra-settings-G.txt`,
`output/settings/astra-settings-H.txt` (2 briefs × 2 models = 4 runs).
Distillation promoted settings rows to `both-confirm` in playbook v1.3.0;
sidebar/profile rows await their briefs.

## Standard v4 briefs (sidebar / nav-shell — one surface at a time, same protocol)

Run each brief on BOTH models in fresh chats. Instruction line to prepend:
"Apply the UI process you described earlier in this chat. Full nav-shell
direction with copy, states, and responsive behavior — no code."

- **Brief I (ops nav, light):** App nav-shell for Helpdeskly (same product
  world as v2 Brief E / v3 Brief G). Light theme, calm-dense tone. Must
  cover: sidebar grouping + ordering, topbar (search/scope/context),
  command palette, breadcrumbs, collapse behavior, permission-filtered
  items, keyboard + reduced-motion notes.
- **Brief J (finance nav, dark):** App nav-shell for fictional Ledgerline
  (same product world as v1 Brief C / v2 Brief F / v3 Brief H). Dark theme,
  precise tone. Must cover: dense sidebar with role-based visibility,
  topbar + global search entry, command palette, breadcrumbs, collapse +
  icon-rail states, permission-filtered items, mobile nav recomposition,
  reduced-motion notes.

Save outputs as `output/sidebar/claude-sidebar-I.txt`,
`output/sidebar/claude-sidebar-J.txt`,
`output/sidebar/astra-sidebar-I.txt`,
`output/sidebar/astra-sidebar-J.txt` (2 briefs × 2 models = 4 runs).
Distillation target: sidebar/nav-shell annex (grouping + ordering, topbar
jobs, palette discipline, collapse honesty, permission filtering) graded
`both-confirm` only on cross-family conformance — promoted in playbook
v1.4.0; profile rows await their briefs. If the original process chat was deleted, precede each brief with
the family-specific recap block (see chat history) instead of the
"described earlier" line.
