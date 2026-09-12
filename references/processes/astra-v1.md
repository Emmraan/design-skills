# GPT-family observations v1 (Astra)

> status: complete · model: gpt (OpenAI, web UI) · updated: 2026-09-12
> Method: extraction-prompt process answer (7 phases) + same 3 standard briefs
> (saas/ai/fintech landing). Repo links were NOT fetchable by the model, so the
> self-report is ungrounded in repo files — finalized here against repo
> conventions (English, decisions-not-pixels, text-only, describe-only).
> Self-reported claims were conformance-checked against all 3 brief outputs.

## Method

- Briefs used: A saas (invoicing, warm stationery premise), B ai (meeting-recap
  command surface), C fintech (Clearcard expense-cards) — each output restates
  the process phases applied to the brief, then gives the direction.
- Self-report: 7 phases (normalize brief → plan structure → design-language
  hypothesis → compose → behavior/states/responsive → critique/simplify →
  polish + honest delivery). Extra 7th phase vs Claude is complementary
  structure, not a conflict.
- Outputs examined: all 3 brief outputs. Conformance: STRONG — every output
  sets a thesis, assigns color jobs, varies section shapes, refuses invented
  proof, and names its likely first-pass failure + correction. Notable: outputs
  explicitly narrate the process AGAIN per brief (self-documenting behavior).

## Observed process signals

| # | Signal | Evidence | Grade |
|---|---|---|---|
| 1 | Brief normalized to one user + one task + one success condition; assumptions labeled, never presented as truth | Premise + audience + doubt stated per brief; fictional inputs fenced as placeholders | both-confirm |
| 2 | Design thesis written down to arbitrate later choices | "Quietly precise stationery", "high-signal command surface", "control without anxiety" | both-confirm |
| 3 | Role-based color system first; strongest accent reserved for action/status | Canvas/surface/text/border/focus/action/status roles per brief; accent scarcity rules | both-confirm |
| 4 | Every region gets one job; regions without a job removed | Section→job mapping (orient/explain/prove/compare/act/recover) in all outputs | both-confirm |
| 5 | Real or realistically constrained content composed early; no lorem-block layouts | Named clients, dated invoices, timestamped transcripts, policy values in every output | both-confirm |
| 6 | Mobile composed as reprioritization, never stacked desktop | Per-output mobile rules (message→CTA→cropped artifact; separate plan blocks) | both-confirm |
| 7 | Motion only explains state change; reduced motion is first-class | Motion rules per brief; perpetual/floating animation refused | both-confirm |
| 8 | Honest delivery: never claim testing/audit/user-research that didn't happen; record unresolved decisions | Phase 7 rules; outputs fence every fictional element with replacement conditions | single |
| 9 | Grayscale check: hierarchy must survive without accent color | Critique rules; outputs keep hierarchy in position/scale/contrast, not hue | single |
| 10 | Squint test + scan test (headings/labels/CTAs/data only) as separate passes | Critique protocol; never one vague "looks good" pass | single |
| 11 | One dominant visual anchor per major viewport | Hero composition rules; single product moment per brief | single |
| 12 | Surface-specific emphasis table (landing/dashboard/settings/editorial/commerce) | Stated in process; landing rows confirmed by outputs, app rows unconfirmed (landing-first scope) | single |
| 13 | Failure-mode honesty: names its own drift (default SaaS composition) + correction | Each brief output names its likely weak first pass and the fix | single |

Grades: `both-confirm` (Claude outputs show the same behavior) / `single`
(GPT only) / `contested` (families differ — none found in v1).

## De-AI moves observed

- Design: avoid-list maps 1:1 onto repo synthesis-rules AI-tells (centered hero
  + pills + floating card; gradient/glow/glass as brand; pill-everything;
  decorative icons; fake screenshots; neon-dark shorthand; stacked-mobile).
  Adds: nav-weight discipline, uniform-spacing refusal.
- Copy: truth-set writing (product/audience/action/evidence/next-step);
  headline-as-concrete-change; weak→better rewrite pairs. Confirms
  human-copy.md gates 2, 3, 6, 9, 11.
- Gap noted: model could not ground in repo files; repo-fit mapping done here,
  not by the model. Honest limitation stated by the model itself: no visual
  verification without rendered output — adopted as playbook caveat.
