import math

def calculate_normal_gravity(latitude_degrees: float) -> float:
    gamma_e = 9.7803253359
    gamma_p = 9.8321849378
    a = 6378137.0
    b = 6356752.3142
    
    lat_rad = math.radians(latitude_degrees)
    sin_lat = math.sin(lat_rad)
    cos_lat = math.cos(lat_rad)
    
    num = (a * gamma_e * (cos_lat**2)) + (b * gamma_p * (sin_lat**2))
    den = math.sqrt((a**2 * (cos_lat**2)) + (b**2 * (sin_lat**2)))
    
    return num / den

def test_calculate_normal_gravity():
    # Equator
    assert math.isclose(calculate_normal_gravity(0.0), 9.7803253359, rel_tol=1e-9)
    # Pole
    assert math.isclose(calculate_normal_gravity(90.0), 9.8321849378, rel_tol=1e-9)
    # 45 Degrees
    assert math.isclose(calculate_normal_gravity(45.0), 9.8061977693, rel_tol=1e-7)

