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
