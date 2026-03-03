import pytest
import math

def calculate_tissot_indicatrix(lat_rad, lon_rad, R=6371000.0):
    """Calculates Tissot indicatrix semi-axes a and b, and maximum angular distortion omega.
    For a simplified spherical case on a regular cylindrical projection (e.g. Equidistant Cylindrical / Plate Carrée).
    Returns (a, b, omega_deg).
    """
    # Plate Carree: x = R*lon, y = R*lat
    # scale factor along parallel: h = 1.0 (meridian scale)
    # scale factor along meridian: k = sec(lat)
    h = 1.0
    k = 1.0 / math.cos(lat_rad)
    a = max(h, k)
    b = min(h, k)
    
    # max angular distortion: 2 * arcsin((a-b)/(a+b))
    omega_rad = 2 * math.asin((a - b) / (a + b))
    omega_deg = math.degrees(omega_rad)
    
    return a, b, omega_deg

def test_calculate_tissot_indicatrix():
    # Equator: should be a circle, a=1, b=1, omega=0
    a, b, omega = calculate_tissot_indicatrix(0.0, 0.0)
    assert math.isclose(a, 1.0, rel_tol=1e-5)
    assert math.isclose(b, 1.0, rel_tol=1e-5)
    assert math.isclose(omega, 0.0, rel_tol=1e-5)
    
    # 60 degrees North: cos(60) = 0.5. For Plate Carree, parallel scale k = 1/cos(lat) = 2.0
    a, b, omega = calculate_tissot_indicatrix(math.radians(60), 0.0)
    assert math.isclose(a, 2.0, rel_tol=1e-5)
    assert math.isclose(b, 1.0, rel_tol=1e-5)
    assert omega > 0.0
