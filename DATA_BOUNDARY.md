# Data Boundary

This repository is a public portfolio sandbox. It is designed to show clinical AI workflow thinking without exposing patient information, private clinical exports, or vendor-specific production workflow details.

## Allowed

- Synthetic patient IDs such as `SYN-001`
- Fictional symptoms, monitoring gaps, follow-up tasks, and risk flags
- Generalized workflow language
- Demo output generated from synthetic fixtures
- Safety checks, tests, and documentation that explain the review boundary

## Not Allowed

- Real patient names, initials, dates of birth, phone numbers, emails, addresses, lab values, appointment details, or chart text
- Screenshots or exports from production clinical tools
- Vendor-specific internal workflow details
- Credentials, tokens, private URLs, or operational identifiers
- Any data copied from a live clinical system, even if it looks harmless

## Review Gates

Before adding new examples, confirm that:

- every record is fictional and uses a synthetic ID
- no examples can be traced to a real patient or clinical encounter
- generated output is labeled as synthetic
- clinical risk language routes to human review
- no automated output is framed as diagnosis, treatment advice, or a final note

## Why This Matters

The purpose of this repo is to show useful healthcare AI product judgment. In public clinical AI demos, the data boundary is part of the product. A good demo should make safety and human review visible before any system gets close to real clinical work.
