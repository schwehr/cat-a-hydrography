import pytest
import numpy as np
from b1_1c_nl_solutions.precision import demonstrate_precision_loss, demonstrate_catastrophic_cancellation

def test_precision_loss_demonstration():
    # This should fail because the function is not yet implemented
    result = demonstrate_precision_loss()
    assert result < 1e-9

def test_catastrophic_cancellation_demonstration():
    # This should fail because the function is not yet implemented
    result_naive, result_robust = demonstrate_catastrophic_cancellation(1e-8)
    assert abs(result_naive - result_robust) > 1e-9
