import pytest
import math

# --- Actual implementation to be included in the book ---
def calculate_first_eccentricity_squared(a: float, b: float) -> float:
    return (a**2 - b**2) / a**2

def calculate_flattening(a: float, b: float) -> float:
    return (a - b) / a

def parametric_ellipse(a: float, b: float, t_degrees: float) -> tuple[float, float]:
    t_radians = math.radians(t_degrees)
    x = a * math.cos(t_radians)
    y = b * math.sin(t_radians)
    return x, y

# --- Unit tests ---

def test_calculate_first_eccentricity_squared():
    a = 6378137.0
    b = 6356752.314245
    e2 = calculate_first_eccentricity_squared(a, b)
    assert math.isclose(e2, 0.00669437999, rel_tol=1e-5)

def test_calculate_flattening():
    a = 6378137.0
    b = 6356752.314245
    f = calculate_flattening(a, b)
    assert math.isclose(1.0 / f, 298.257223563, rel_tol=1e-9)

def test_parametric_ellipse():
    a = 10.0
    b = 5.0
    x, y = parametric_ellipse(a, b, 0.0)
    assert math.isclose(x, 10.0)
    assert math.isclose(y, 0.0, abs_tol=1e-9)
    
    x, y = parametric_ellipse(a, b, 90.0)
    assert math.isclose(x, 0.0, abs_tol=1e-9)
    assert math.isclose(y, 5.0)

