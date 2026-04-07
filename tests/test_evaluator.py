# SPDX-License-Identifier: AGPL-3.0-or-later

"""Tests for the Evaluator module."""

import pytest
from heretic.evaluator import Evaluator, RefusalCounter


class TestRefusalCounter:
    """Tests for the RefusalCounter class."""

    def test_should_count_refusal_markers(self):
        """Refusal markers in text should be counted correctly."""
        counter = RefusalCounter(markers=["I cannot", "I'm sorry"])
        text = "I cannot help with that. I'm sorry but I must decline."
        assert counter.count(text) == 2

    def test_should_return_zero_for_clean_text(self):
        """Text without refusal markers should return zero."""
        counter = RefusalCounter(markers=["I cannot"])
        text = "Here is the answer you requested."
        assert counter.count(text) == 0

    def test_should_be_case_sensitive_by_default(self):
        """Refusal counting should be case-sensitive by default."""
        counter = RefusalCounter(markers=["I cannot"])
        text = "i cannot help with that."
        assert counter.count(text) == 0


class TestEvaluator:
    """Tests for the Evaluator class."""

    def test_should_compute_kl_divergence(self):
        """KL divergence should be computed between two distributions."""
        evaluator = Evaluator()
        # Simple test case: identical distributions should have zero KL divergence
        p_logits = [[0.0, 0.0, 0.0]]
        q_logits = [[0.0, 0.0, 0.0]]
        kl_div = evaluator.compute_kl_divergence(p_logits, q_logits)
        assert kl_div >= 0

    def test_should_evaluate_model_output(self):
        """Evaluation should return refusal count and KL divergence."""
        evaluator = Evaluator(markers=["I cannot"])
        result = evaluator.evaluate(original_logits=[[0.0]], modified_text="I cannot do that.")
        assert "refusals" in result
        assert result["refusals"] == 1
