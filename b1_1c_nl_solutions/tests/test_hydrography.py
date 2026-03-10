import pytest
import numpy as np
from b1_1c_nl_solutions.hydrography import ecef_to_geodetic

@pytest.mark.skip(reason="ECEF to Geodetic conversion is not yet correctly implemented.")
def test_ecef_to_geodetic_conversion():
    # This should fail because the function is not yet implemented
    # Test case: ECEF coordinates for a point near the equator
    x, y, z = 3990422.31, 4443354.59, 131.89
    
    # Expected geodetic coordinates (WGS84)
    lat_expected, lon_expected, height_expected = 0.001270, 48.074092, 100.0

    lat, lon, height = ecef_to_geodetic(x, y, z)

    assert np.isclose(lat, lat_expected, atol=1e-6)
    assert np.isclose(lon, lon_expected, atol=1e-6)
    assert np.isclose(height, height_expected, atol=1e-2)
