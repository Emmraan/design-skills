# Synthesis Rules — Turning References Into Original Designs

The repo's purpose is **originality through synthesis**. These rules govern how to combine
references so the output never looks like a copy of any single source.

## Core rules

1. **Retrieve at least 3 references first.** Mix categories deliberately: e.g. a layout
   from one site, color logic from another, type pairing from a third.
2. **Steal logic, not pixels.** Extract *why* a design works (roles, rhythm, hierarchy
   mechanics), not exact values. Hex codes and px are evidence, never the design language.
3. **Change at least 2 of {layout, color, typography}** from every single source. If the
   result could be described as "like X but reskinned", redo it.
4. **Cross-pollinate categories.** The best AI page often borrows fintech restraint; the
   best fintech page borrows editorial calm; the best SaaS borrows commerce urgency. The
   collection files (`references/collections/`) and `retrieval/knowledge-map.json` point at
   deliberate pairings.
5. **One coherent language.** Borrowed pieces must resolve into a single design language —
   one spacing scale, one type system, one color-role grammar. No Frankenstein assemblies.

## A proven synthesis formula

| Source type | What to borrow | Example |
|---|---|---|
| Site A | **Layout / section flow** | Editorial alternating rows |
| Site B | **Color logic** | One saturated accent + tinted neutrals |
| Site C | **Typography pairing** | Serif display + mono meta labels |
| Design-token files | **Scale systems** | 8px spacing base, fluid clamp type |
| A11y / interaction files | **Behavior rules** | Focus states, motion constraints |

Then deliberately **flip one expectation**: if your competitors are dark, go light; if
everyone uses a split hero, use a text-forward statement; if the default accent is purple,
pick a different hue.

## Anti-patterns

- **Single-source lift:** page structure + colors + type all from one site.
- **Clichés:** purple-blue gradients, floating orbs, "the future is here" copy, 3-card
  pricing with the middle one highlighted — unless consciously inverted.
- **Value dumping:** listing hex/px as the "design" instead of roles and systems.
- **Inconsistent scale:** mixing an 8px system with a 5px system, or two display fonts
  fighting for attention.

## Before you ship

Write one line for each reference: "X gave me the hero layout; Y gave me the accent role;
Z gave me the type pairing." If any reference contributed nothing, drop it. If one
contributed too much (single source), diversify. Then run the review checklist.
