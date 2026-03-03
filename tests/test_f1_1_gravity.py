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


def calculate_dynamic_height(geopotential_number: float) -> float:
    gamma_45 = 9.806199 
    return geopotential_number / gamma_45

def calculate_orthometric_height(geopotential_number: float, mean_actual_gravity: float) -> float:
    return geopotential_number / mean_actual_gravity

def calculate_normal_height(geopotential_number: float, mean_normal_gravity: float) -> float:
    return geopotential_number / mean_normal_gravity

def test_height_systems():
    C = 98.06199 # Example geopotential number
    
    # Dynamic height should be exactly 10.0 if C = 10 * gamma_45
    assert math.isclose(calculate_dynamic_height(C), 10.0, rel_tol=1e-5)
    
    # Orthometric height using a slightly different actual gravity
    g_bar = 9.81
    assert math.isclose(calculate_orthometric_height(C, g_bar), C / g_bar, rel_tol=1e-5)
    
    # Normal height using a slightly different normal gravity
    gamma_bar = 9.80
    assert math.isclose(calculate_normal_height(C, gamma_bar), C / gamma_bar, rel_tol=1e-5)
