import numpy as np
import sympy as sp

def vector_add(v1: np.ndarray, v2: np.ndarray) -> np.ndarray:
    """Adds two vectors in a vector space."""
    return v1 + v2

def calculate_inner_product(v1: np.ndarray, v2: np.ndarray) -> float:
    """Calculates the Euclidean inner product (dot product) of two vectors."""
    return float(np.dot(v1, v2))

def calculate_norm(v: np.ndarray) -> float:
    """Calculates the Euclidean norm (magnitude) of a vector."""
    return float(np.linalg.norm(v))

def sympy_vector_space_demo():
    """Demonstrates theoretical vector space properties using SymPy."""
    u1, u2, u3 = sp.symbols('u1 u2 u3')
    v1, v2, v3 = sp.symbols('v1 v2 v3')
    c = sp.symbols('c')
    
    u = sp.Matrix([u1, u2, u3])
    v = sp.Matrix([v1, v2, v3])
    
    addition = u + v
    scalar_mult = c * u
    
    return u, v, addition, scalar_mult
def matrix_compose(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Composes two matrices (matrix multiplication)."""
    return A @ B

def matrix_transpose(A: np.ndarray) -> np.ndarray:
    """Returns the transpose of a matrix."""
    return A.T

def linear_operator_demo():
    """Demonstrates a simple linear operator applying to a vector."""
    A = np.array([[1, 2], [3, 4]])
    v = np.array([1, 2])
    return A, v, A @ v

def translate_2d(point: np.ndarray, translation: np.ndarray) -> np.ndarray:
    """Translates a 2D point by a given vector."""
    return point + translation

def rotate_2d(point: np.ndarray, angle_rad: float) -> np.ndarray:
    """Rotates a 2D point around the origin by a given angle in radians."""
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)
    rotation_matrix = np.array([
        [cos_a, -sin_a],
        [sin_a, cos_a]
    ])
    return rotation_matrix @ point
