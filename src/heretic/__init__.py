# SPDX-License-Identifier: AGPL-3.0-or-later

"""
Heretic - Automated censorship removal for transformer language models.

Heretic implements directional ablation to suppress refusal behavior in LLMs
using Optuna-based multi-objective optimization. It supports dense models,
MoE architectures, and multimodal models with 4-bit quantization.

Usage:
    from heretic import Heretic
    from heretic.config import Settings

    settings = Settings(model_id="meta-llama/Llama-3.1-8B")
    heretic = Heretic(settings)
    heretic.optimize()
    heretic.save_lora("my-uncensored-model")
"""

from heretic.main import Heretic
from heretic.config import Settings
from heretic.model import Model
from heretic.evaluator import Evaluator
from heretic.analyzer import Analyzer

__version__ = "1.2.0"
__author__ = "Aatif Qmr"
__email__ = ""
__license__ = "AGPL-3.0-or-later"

__all__ = [
    "Heretic",
    "Settings",
    "Model",
    "Evaluator",
    "Analyzer",
    "__version__",
]
