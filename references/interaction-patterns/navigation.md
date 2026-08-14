# Navigation

Navigation is the site's map. It should be invisible when working well: the user finds
everything without thinking.

## Desktop nav anatomy

```
[Logo]  [Link  Link  Link  Dropdown▾]        [Log in] [Primary CTA]
  left: brand            center: links       right: actions
```

- **Left = brand, center/left = links, right = actions** (login + primary CTA) is the default
  that users already understand.
- Max ~5-6 top-level links; more needs grouping/dropdowns.
- The **primary CTA** is visually dominant (primary button). One CTA per nav, always.
- Sticky nav with a subtle background (blur/backdrop) after scroll keeps actions reachable.

## Mobile nav

- **Hamburger** → slide-down panel or full-screen overlay.
- Include the same links + actions; keep the primary CTA visible (sticky bar or in menu).
- Accessible: button with `aria-expanded`, menu closes on Esc / outside tap / link click.

## Dropdowns / mega menus

- Trigger on hover **and** click (hover-only breaks touch + keyboard).
- Open/close with keyboard (Enter opens, Esc closes, arrows navigate).
- `aria-expanded` on the trigger; menu as a list with proper semantics.
- Keep menus shallow (1 level) and fast (150-250ms).

## Sticky / scroll behavior

- Header hides on scroll-down, reveals on scroll-up (only on content-heavy pages).
- Or header always sticky with reduced padding on scroll (common, safe).
- Ensure anchor links account for sticky header height (scroll-margin-top).

## Best practices

1. **Visible current location** — `aria-current="page"` + a visual state.
2. **Descriptive labels** ("Pricing", not "More").
3. **Consistent order** on every page.
4. **Skip link** to main content.
5. Include a **CTA that matches the page goal** (Sign up on marketing pages).

## Patterns to reuse

| Pattern | Use |
|---|---|
| Simple top nav | SaaS, portfolio, agency |
| Centered nav + logo | Editorial, premium brands |
| Left sidebar | Docs, apps, dashboards |
| Top nav + utility row | Marketplaces, complex products |

## Anti-patterns (never copy)

- More than ~7 top-level links without grouping.
- Two competing CTAs in the nav (Sign up + Get started + Book a demo).
- Hover-only dropdowns (unusable on touch/keyboard).
- Nav that disappears and can't return to top.
