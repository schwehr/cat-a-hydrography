import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pytest
import sympy as sp
from book.b1_1b import calculate_inner_product, calculate_norm, vector_add, sympy_vector_space_demo

def test_calculate_inner_product():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    result = calculate_inner_product(v1, v2)
    assert result == 32

def test_calculate_norm():
    v = np.array([3, 4])
    result = calculate_norm(v)
    assert np.isclose(result, 5.0)

def test_vector_addition():
    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    result = vector_add(v1, v2)
    assert np.all(result == np.array([5, 7, 9]))

def test_sympy_demo():
    u, v, addition, scalar_mult = sympy_vector_space_demo()
    assert addition[0] == u[0] + v[0]
