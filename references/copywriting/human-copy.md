# Human Copy — Write Website Copy That Never Reads AI-Generated

> Distilled (original prose, not copied) from three copy sources + one design
> source. Rules below govern **generated website copy only** — never repo prose.
> Version: 1.0.0 · Updated: 2026-09-12
>
> Sources:
> - https://github.com/blader/humanizer/blob/main/SKILL.md (MIT)
> - https://github.com/harshaneel/humanize (MIT)
> - https://github.com/softaworks/agent-toolkit/blob/main/skills/writing-clearly-and-concisely/signs-of-ai-writing.md (Wikipedia-derived; distill only, never verbatim)
> - https://github.com/Emmraan/agent-skills/tree/main/skills/frontend-ui (MIT; `frontend-craft` copy rules)

## 1. Core principle

Every sentence must add something the reader did not already have. Staging,
decoration, and borrowed weight are the enemy: state the point directly, ground
it in specifics, and stop.

## 2. Banned copy patterns (hard gates — audit every output)

1. **Negation pivots.** "Not just X, it's Y", "not X but Y", "it's not about X,
   it's about Y". Name what the thing IS. Keep a contrast only when the reader
   actually holds the wrong belief and both halves carry information.
2. **Staged openers and closers.** "Let's dive in", "here's what you need to
   know", "honestly?", one-sentence closers that restate the paragraph ("That is
   the real win."). Remove the run-up; end on the last concrete fact, never a
   summary the page is too short to need.
3. **Forced triads.** Ideas arriving in threes to sound complete ("innovation,
   inspiration, and insights"), three parallel examples, triple fragments. Keep
   three only when the meaning genuinely has three parts.
4. **Inflated significance.** "Pivotal moment", "stands as a testament",
   "plays a key role", "evolving landscape", "setting the stage". Keep the fact,
   drop the legacy-claim.
5. **Sales brochure register.** "Nestled", "breathtaking", "vibrant", "renowned",
   "boasts", "in the heart of", "must-visit". State what the thing is.
6. **Borrowed authority.** "Experts argue", "observers note", "featured in [outlet
   list]", follower counts as proof. Name the real source and what it said, or
   cut the claim.
7. **Shallow -ing riders.** "..., highlighting / underscoring / showcasing /
   reflecting ...". Keep the fact; keep the rider only with real supporting
   evidence.
8. **Hedge stacks.** "It is important to note", "generally speaking", "may vary"
   chains. Assert directly; hedge only with genuine uncertainty, in human words.
9. **Chat residue.** Greetings, praise, offers to continue, knowledge-cutoff
   disclaimers. Published copy never carries them.
10. **AI vocabulary clusters.** `delve`, `leverage` (verb), `robust`,
    `streamline`, `tapestry` (figurative), `landscape` (abstract), `furthermore`,
    `moreover`, `crucial`/`pivotal` inflation. One occurrence is a smell; a
    cluster is a verdict. Prefer the plain verb: use, build, cut, speed up.
11. **Placeholder product copy.** "Build something amazing", "unlock your
    potential", "welcome to X". Write concrete, product-specific claims a
    competitor could not paste onto their own page.

## 3. Specificity rule

Every abstract claim needs a grounding anchor: a number, a named example, a
time reference, a named tool. "Performance improved significantly" becomes
"p95 latency dropped from 340ms to 80ms under the same load". If specifics are
unavailable, frame plausibly ("when you're running at X scale...") — never
invent facts. A page with zero anchors reads generated no matter how clean the
prose.

## 4. Voice and rhythm

- Vary sentence length deliberately: short punchy sentences against longer ones
  that earn their clauses. Metronomic 15–20-word sentences are a tell.
- Match register to surface: landing copy may carry opinion and direct address
  ("you"); docs and settings copy stays neutral and plain.
- Transitions are invisible: cut "furthermore", "moreover", "in addition". The
  next sentence should simply follow.
- Punctuation carries no drama: em dashes rare (never as a universal
  connector), semicolons almost never outside formal prose, colons only after a
  complete sentence. Prefer periods.

## 5. RLHF voice strip

Cut the helpful-assistant register: framing openers ("here's how I'd think
about it"), unprompted balanced tradeoffs ("on one hand... on the other..."),
enumerated options nobody asked for, appended caveats on every claim,
acknowledgment prefixes, recaps of what was just said, hedged closers. Pick a
side, make the claim, end on substance.

## 6. Audit gate (run before shipping any copy)

- [ ] Count negation pivots: must be 0 (unless correcting a real reader belief).
- [ ] Count staged openers, one-line closers, triads: each must earn its place.
- [ ] Scan the banned-vocabulary clusters: no cluster survives.
- [ ] Every section has at least one specificity anchor.
- [ ] Read aloud once: anything that sounds like a brochure, a keynote, or a
      chatbot gets rewritten from the facts, not patched word by word.
- [ ] No invented numbers, names, quotes, or claims. A thin honest page beats a
      rich fabricated one.
