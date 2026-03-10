import numpy as np

def demonstrate_precision_loss():
    """
    Demonstrates loss of precision when adding a small number to a large number.
    """
    large_number = 1.0
    small_number = 1e-16
    result = large_number + small_number
    return abs(result - large_number)

def demonstrate_catastrophic_cancellation(x):
    """
    Demonstrates catastrophic cancellation when subtracting nearly equal numbers.
    The naive approach calculates sqrt(1+x) - 1 directly.
    The robust approach uses the identity (sqrt(a)-sqrt(b)) = (a-b)/(sqrt(a)+sqrt(b))
    to avoid the subtraction of nearly equal numbers.
    """
    # Naive calculation
    result_naive = np.sqrt(1 + x) - 1

    # Robust calculation
    result_robust = x / (np.sqrt(1 + x) + 1)

    return result_naive, result_robust
