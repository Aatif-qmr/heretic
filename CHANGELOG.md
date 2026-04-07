# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.2.0] - 2025-11-XX

### Added
- Support for Qwen3 MoE architecture
- Support for Phi-3.5-MoE architecture
- Support for Granite MoE architecture
- Batch size auto-tuning for optimal hardware utilization
- CoT (Chain of Thought) prefix suppression
- PaCMAP residual vector visualization and geometry analysis
- Multi-objective optimization (refusals + KL divergence)
- Checkpoint persistence and resume functionality
- Interactive post-optimization model saving and uploading
- TOML-based configuration with CLI overrides
- 4-bit quantization support via bitsandbytes
- Pydantic-based settings validation

### Changed
- Upgraded to Optuna TPE sampler for multi-objective optimization
- Improved weight kernel parameterization with SVD approximation
- Enhanced row normalization options (none, pre, full)

### Fixed
- Type safety issues around module casting in MoE models
- Memory management for large model weights
- Configuration loading from multiple sources (CLI, env, TOML)

## [1.1.0] - Previous Release

### Added
- Initial LoRA-based directional ablation implementation
- Support for dense transformer models
- KL divergence evaluation
- Refusal counting with configurable markers
- Basic CLI interface

### Changed
- Migrated from custom training loop to Optuna optimization

## [1.0.0] - Initial Release

### Added
- Core abliteration logic
- HuggingFace model integration
- Basic evaluation metrics
- Command-line interface

[Unreleased]: https://github.com/Aatif-qmr/Uncensored-AI/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/Aatif-qmr/Uncensored-AI/releases/tag/v1.2.0
[1.1.0]: https://github.com/Aatif-qmr/Uncensored-AI/releases/tag/v1.1.0
[1.0.0]: https://github.com/Aatif-qmr/Uncensored-AI/releases/tag/v1.0.0
