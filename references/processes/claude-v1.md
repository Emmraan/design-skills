# Claude-family observations v1 (Fable)

> status: complete · model: claude (Anthropic, web UI) · updated: 2026-09-12
> Method: extraction-prompt process answer (6 phases) + same 3 standard briefs
> (saas/ai/fintech landing). Repo links were NOT fetchable by the model, so the
> self-report is ungrounded in repo files — finalized here against repo
> conventions (English, decisions-not-pixels, text-only, describe-only).
> Self-reported claims were conformance-checked against all 3 brief outputs.

## Method

- Briefs used: A saas (Kitebill invoicing), B ai (Aster meeting-notes), C
  fintech (Ledgerline expense-cards) — full landing directions with copy.
- Self-report: 6 phases (decode brief → information architecture → design
  language → compose main screen → functional realism → critique/subtract/polish).
- Outputs examined: all 3 brief outputs. Conformance: STRONG — every output
  opens with a visual thesis, uses role-based color, varies section shapes,
  labels fictional proof as placeholder, and ends with mobile priorities +
  details-to-avoid. No claim without a visible output behavior.

## Observed process signals

| # | Signal | Evidence | Grade |
|---|---|---|---|
| 1 | Brief decoded to one user + one action + decision anxiety; facts separated from assumptions | All 3 outputs state concept, job, primary CTA, and mark fictional claims as placeholders | both-confirm |
| 2 | Visual thesis phrase set before composing, arbitrating later choices | "Quiet financial confidence", "control room for conversation", "control without theater" — each output commits upfront | both-confirm |
| 3 | Semantic color roles before attractive colors; status hues reserved for real status | Role palettes in every output; explicit "green/amber/red carry status only" | both-confirm |
| 4 | One primary action per decision point; secondary actions quiet | Primary/secondary CTA split + hierarchy in all 3 outputs | both-confirm |
| 5 | Proof placed near the claim it supports; fictional proof labeled, never shipped as real | Placeholder testimonials/metrics explicitly tagged fictional with replacement rules | both-confirm |
| 6 | Information shape varies per section; cards only where repetition means system | Editorial splits, timelines, decision flows, exception queues — no card-grid monoculture | both-confirm |
| 7 | Hero visual must do a product job, never decorate | Invoice workspace, transcript→decision panel, card+policy+ledger composites specified per brief | both-confirm |
| 8 | Edge states designed as part of composition (empty/loading/error/long-content/mobile) | Mobile-priority sections + state coverage in every output | both-confirm |
| 9 | Subtractive critique: delete ≥1 nonessential treatment; first drafts lose 20–35% | Stated + "details to avoid" lists closing every output | single |
| 10 | Transplant test: "could this belong to any company?" → rewrite or remove | Self-critique specificity check; headlines rewritten until untransplantable | single |
| 11 | Icons must have a job; decorative icons rare | Critique checklist item, applied in outputs (icons absent unless functional) | single |
| 12 | Copy honesty without fake personality: no quirky fragments/slang/em dashes to seem human | Voice rules; outputs use plain direct sentences, placeholders instead of invented quotes | single |
| 13 | UX copy states what happened + what user can do + whether work is safe | Error/empty language rules; settings consequence-near-control | single |

Grades: `both-confirm` (Astra outputs show the same behavior) / `single`
(Claude only) / `contested` (families differ — none found in v1).

## De-AI moves observed

- Design: centered-hero + gradient-blob + floating-card default refused in all
  3 outputs; one-or-two signature decisions with the rest quiet; texture from
  real content (invoice rows, transcript lines, ledger states); density as a
  style choice. Confirms repo synthesis-rules AI-tells.
- Copy: banned-phrase list overlaps human-copy.md (unlock/seamless/elevate/
  revolutionize); CTA-as-action; claims proportional to evidence. Confirms
  human-copy.md gates 1, 4, 5, 10, 11.
- Gap noted: model could not ground in repo files; repo-fit mapping done here,
  not by the model.
