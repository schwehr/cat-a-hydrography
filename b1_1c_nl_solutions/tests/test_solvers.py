import pytest
from b1_1c_nl_solutions.solvers import bisection, newton_raphson, secant

# Test function: f(x) = x^2 - 4, with root at x = 2
def func(x):
    return x**2 - 4

def func_derivative(x):
    return 2*x

def test_bisection_solver():
    # This should fail because the function is not yet implemented
    root = bisection(func, 0, 5)
    pytest.approx(root, 2, 1e-6)

def test_newton_raphson_solver():
    # This should fail because the function is not yet implemented
    root = newton_raphson(func, func_derivative, 5)
    pytest.approx(root, 2, 1e-6)

def test_secant_solver():
    # This should fail because the function is not yet implemented
    root = secant(func, 4, 5)
    pytest.approx(root, 2, 1e-6)
