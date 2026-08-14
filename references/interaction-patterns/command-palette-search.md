# Command Palette & Search

A command palette (Cmd/Ctrl+K) is the fastest way to navigate power-user products; search
must be forgiving and fast. Both are strong differentiators when done well.

## Command palette

```
⌘K opens → overlay with:
┌─────────────────────────────────────────────┐
│ 🔍  Search actions and pages…        [esc]  │
│ ─────────────────────────────────────────── │
│  Navigate                                  │
│    › Dashboard                             │
│    › Settings                              │
│  Actions                                   │
│    › New project          ⌘N               │
│    › Invite teammate      ⌘I               │
└─────────────────────────────────────────────┘
```

**Rules:**
1. Global shortcut (**Cmd/Ctrl+K**) + keyboard-only usable; mouse optional.
2. **Fuzzy match** — typing "set" matches Settings. Highlight matched characters.
3. **Keyboard navigation**: arrows move, Enter executes, Esc closes, focus returns to trigger.
4. **Grouped results** (Actions / Navigate / Recently used) with hints on the right.
5. Fast: filter instantly as you type; debounce server queries.
6. Recent/frequent items first for the empty state.
7. Accessible: `role="dialog"`, focus trap, `aria-activedescendant` for list selection.

## Search

- **Search box with clear button** (×), keyboard shortcut `/` or Cmd+K to focus.
- **Type-ahead suggestions** (debounced) — show results, not just a spinner.
- **Forgiving matching**: synonyms, partial words, typos ("prcing" → pricing).
- **Result page**: highlight matched terms, show context snippet, sort by relevance.
- **Empty state**: "No results for 'xyz' — try 'abc' or clear filters" (never a blank page).
- **Loading**: skeleton rows, not a full-page spinner.

## Best practices

1. **Always offer search** on content-heavy sites (docs, products, large nav).
2. **Keyboard-first** in both — power users will notice.
3. Show **empty-state hints** (common searches, featured items).
4. Preserve query in URL for shareable results.

## Anti-patterns (never copy)

- No keyboard shortcut, no Esc to close.
- Search that only matches exact phrases.
- Results loading that shifts layout.
- Palette that doesn't support arrow-key navigation.
- No "no results" state.
