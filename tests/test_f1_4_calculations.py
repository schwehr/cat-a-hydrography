import pytest
import math

def calculate_curvature(distance_km: float) -> float:
    """Calculates earth curvature error in meters.
    Formula: c = 0.0785 * D^2, where D is in km.
    """
    return 0.0785 * (distance_km ** 2)

def calculate_refraction(distance_km: float) -> float:
    """Calculates atmospheric refraction correction in meters.
    Formula: r = 0.011 * D^2, where D is in km.
    """
    return 0.011 * (distance_km ** 2)

def calculate_combined_correction(distance_km: float) -> float:
    """Calculates combined curvature and refraction correction in meters.
    Formula: c&r = 0.0675 * D^2, where D is in km.
    """
    return 0.0675 * (distance_km ** 2)

def reduce_level(backsight: float, foresight: float, known_elevation: float) -> float:
    """Calculates the new elevation based on a backsight and foresight."""
    height_of_instrument = known_elevation + backsight
    new_elevation = height_of_instrument - foresight
    return new_elevation

def test_calculate_curvature():
    # Example: 1 km distance -> 0.0785 m
    assert math.isclose(calculate_curvature(1.0), 0.0785, rel_tol=1e-4)
    # Example: 2 km distance -> 0.314 m
    assert math.isclose(calculate_curvature(2.0), 0.314, rel_tol=1e-4)

def test_calculate_refraction():
    assert math.isclose(calculate_refraction(1.0), 0.011, rel_tol=1e-4)
    assert math.isclose(calculate_refraction(2.0), 0.044, rel_tol=1e-4)

def test_calculate_combined_correction():
    assert math.isclose(calculate_combined_correction(1.0), 0.0675, rel_tol=1e-4)
    assert math.isclose(calculate_combined_correction(2.0), 0.270, rel_tol=1e-4)

def test_reduce_level():
    # Benchmark = 10.0m, Backsight = 1.5m, Foresight = 1.2m
    # HI = 11.5m, New elevation = 10.3m
    assert math.isclose(reduce_level(1.5, 1.2, 10.0), 10.3, rel_tol=1e-4)

