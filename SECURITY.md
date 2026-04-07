# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.2.x   | :white_check_mark: |
| < 1.2   | :x:                |

## Reporting a Vulnerability

If you discover a security vulnerability in Heretic, please report it privately to the maintainers.

**Do NOT open a public issue.**

### How to Report

1. Go to the [GitHub Security Advisories](https://github.com/Aatif-qmr/Uncensored-AI/security/advisories) page
2. Click "Report a vulnerability"
3. Provide a detailed description of the vulnerability and steps to reproduce

Alternatively, contact the maintainer directly via GitHub.

### What to Expect

- We will acknowledge receipt of your report within 48 hours
- We will provide a preliminary assessment within 7 days
- We will work with you to understand and fix the issue
- We will coordinate public disclosure timing with you

### Scope

Security vulnerabilities may include:
- Remote code execution through malicious model files
- Credential leakage (HuggingFace tokens, API keys)
- Arbitrary file access through configuration
- Denial of service via crafted inputs

### Out of Scope

- Refusal behavior in generated text
- Model output quality
- Performance issues (unless they constitute DoS)

## Security Best Practices for Users

1. **Never share your HuggingFace token** - Heretic stores it in your local environment only
2. **Verify model sources** - Only load models from trusted HuggingFace repositories
3. **Use virtual environments** - Always run Heretic in an isolated Python environment
4. **Review configurations** - Check TOML config files before running optimization
