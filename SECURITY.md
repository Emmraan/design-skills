# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.1.x (latest) | ✅ |

Only the latest release receives security fixes.

## Reporting a vulnerability

Please do **not** open a public GitHub issue for security problems. Instead, report
privately:

- **Preferred:** open a GitHub issue with a `[security]` prefix and a description of the
  impact (public disclosure is acceptable once the issue is understood, but keep initial
  reports out of comments), or
- **Email:** reach out to the maintainer via the contact listed on your profile /
  the GitHub repository page.

Please include:
- A description of the issue and its potential impact.
- Steps to reproduce, if applicable.
- Affected file paths and versions.

You should receive an acknowledgment within a few days. We will not take legal action
against good-faith security research reported per this policy.

## Security considerations specific to this project

This repository is **design knowledge consumed by AI agents** (it is loaded as an Agent
Skill and the `analysis.md` files are read by LLMs). This creates two unique risks:

1. **Prompt injection via website content.** `references/websites/*/analysis.md` files are
   written from extraction of third-party websites (Dembrandt) or manually downloaded
   source (Woblo). Malicious or manipulated site content could sneak instructions into an
   analysis that an agent later follows. Treat every analysis as untrusted input.
2. **Untrusted scripts/commands.** Site URLs pass into Dembrandt CLI commands printed by
   the scripts. Do not paste commands for URLs you do not trust, and never run extractions
   on unknown/untrusted content in an environment with secrets.

### Good practice for contributors

- Review generated `analysis.md` files for injected instructions before committing.
- Quote site URLs when passing them to scripts (they are treated as CLI arguments).
- Do not commit secrets, tokens, or personal data into metadata or analyses.

If you find suspicious content already in the repository, report it as above — it will be
treated as a security issue.
