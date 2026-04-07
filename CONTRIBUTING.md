# Contributing to Heretic

Thank you for your interest in contributing to Heretic! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

This project follows a code of conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- Git

### Development Setup

1. **Fork and clone the repository:**
   ```bash
   git clone https://github.com/YOUR-USERNAME/Uncensored-AI.git
   cd Uncensored-AI
   ```

2. **Install dependencies:**
   ```bash
   uv sync --all-extras
   ```

3. **Verify the setup:**
   ```bash
   uv run heretic --help
   ```

## Development Workflow

### Code Style

This project uses:
- **Ruff** for linting and formatting
- **ty** for type checking

Before submitting a PR, run:
```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check --fix

# Type check
uv run ty check
```

All code must pass these checks. The CI will reject PRs that do not comply.

### Running Tests

```bash
# Run all tests
uv run pytest

# Run specific test file
uv run pytest tests/test_evaluator.py

# Run with coverage
uv run pytest --cov=heretic --cov-report=html
```

### Adding Tests

- Place tests in the `tests/` directory
- Name test files `test_*.py`
- Use descriptive test function names: `test_should_compute_kl_divergence_correctly`
- Use pytest fixtures for common setup

## Submitting Changes

1. Create a new branch for your feature or fix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-description
   ```

2. Make your changes and commit with clear messages:
   ```bash
   git commit -m "feat: add support for XYZ architecture"
   git commit -m "fix: resolve KL divergence calculation edge case"
   ```

3. Push to your fork and open a Pull Request.

### Pull Request Guidelines

- **Title:** Use semantic prefixes (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`)
- **Description:** Explain what the change does and why it is needed
- **Tests:** Include tests for new functionality
- **Documentation:** Update relevant documentation (README, docstrings, CHANGELOG)
- **Scope:** Keep PRs focused and small. Multiple small PRs are preferred over one large PR.

## Architecture Overview

```
src/heretic/
├── __init__.py       # Public API exports
├── main.py           # CLI entry point and Optuna optimization loop
├── model.py          # Model loading, LoRA management, abliteration logic
├── evaluator.py      # KL divergence and refusal counting
├── config.py         # Pydantic settings and configuration parsing
├── analyzer.py       # PaCMAP visualization and residual geometry
└── utils.py          # Utilities: memory management, prompts, helpers
```

### Key Components

- **Model**: Handles model loading, LoRA adapter management, and the core abliteration logic (directional ablation on attention `o_proj` and MLP `down_proj` components)
- **Evaluator**: Computes KL divergence between original and modified model outputs, counts refusals based on configurable markers
- **Config**: Pydantic-based settings loaded from CLI arguments, environment variables, or TOML files
- **Analyzer**: Research tools for PaCMAP projection visualization and residual vector geometry analysis

## Reporting Issues

When reporting bugs, please include:
- Heretic version (`heretic --version`)
- Python version (`python --version`)
- Model ID you are using
- Full error traceback
- Configuration file (if applicable)

## License

By contributing to Heretic, you agree that your contributions will be licensed under the AGPL-3.0-or-later license.
