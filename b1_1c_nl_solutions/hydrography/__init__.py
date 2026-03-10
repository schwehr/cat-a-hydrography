import numpy as np

# TODO: This implementation is not correct and needs to be fixed.
def ecef_to_geodetic(x, y, z, tol=1e-12, max_iter=10):
    """
    Convert ECEF coordinates to geodetic coordinates (latitude, longitude, height)
    using an iterative method.
    """
    # WGS84 Ellipsoid parameters
    a = 6378137.0
    f = 1 / 298.257223563
    e2 = 2*f - f**2

    # Longitude
    lon = np.arctan2(y, x)

    p = np.sqrt(x**2 + y**2)

    # Iterative solution for latitude
    lat = np.arctan2(z, p * (1 - e2))
    for _ in range(max_iter):
        n = a / np.sqrt(1 - e2 * np.sin(lat)**2)
        height = p / np.cos(lat) - n
        lat_new = np.arctan2(z + e2 * n * np.sin(lat), p)
        if abs(lat_new - lat) < tol:
            break
        lat = lat_new

    # Recalculate N and height with the final latitude
    n = a / np.sqrt(1 - e2 * np.sin(lat)**2)
    height = p / np.cos(lat) - n
    
    return np.rad2deg(lat), np.rad2deg(lon), height
