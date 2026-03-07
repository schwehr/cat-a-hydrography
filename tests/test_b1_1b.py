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

from book.b1_1b import matrix_compose, matrix_transpose, linear_operator_demo

def test_matrix_compose():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    result = matrix_compose(A, B)
    expected = np.array([[19, 22], [43, 50]])
    assert np.all(result == expected)

def test_matrix_transpose():
    A = np.array([[1, 2], [3, 4]])
    result = matrix_transpose(A)
    expected = np.array([[1, 3], [2, 4]])
    assert np.all(result == expected)

def test_linear_operator_demo():
    A, v, result = linear_operator_demo()
    assert result.shape == (2, )
    assert result[0] == 5
    assert result[1] == 11

from book.b1_1b import translate_2d, rotate_2d

def test_translate_2d():
    point = np.array([1.0, 2.0])
    translation = np.array([3.0, -1.0])
    result = translate_2d(point, translation)
    expected = np.array([4.0, 1.0])
    assert np.all(result == expected)

def test_rotate_2d():
    point = np.array([1.0, 0.0])
    angle_rad = np.pi / 2  # 90 degrees
    result = rotate_2d(point, angle_rad)
    expected = np.array([0.0, 1.0])
    assert np.allclose(result, expected)
