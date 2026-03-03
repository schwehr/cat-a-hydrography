import pytest
import math
from pyproj import Transformer, Geod

def calculate_utm_distance(lon1, lat1, lon2, lat2, epsg_code="epsg:32633"):
    transformer = Transformer.from_crs("epsg:4326", epsg_code, always_xy=True)
    e1, n1 = transformer.transform(lon1, lat1)
    e2, n2 = transformer.transform(lon2, lat2)
    return math.sqrt((e2 - e1)**2 + (n2 - n1)**2)

def calculate_geodesic_distance(lon1, lat1, lon2, lat2):
    geod = Geod(ellps="WGS84")
    _, _, distance = geod.inv(lon1, lat1, lon2, lat2)
    return distance

def test_programming_assignment_distances():
    lon1, lat1 = 15.0, 50.0
    lon2, lat2 = 15.1, 50.1
    
    utm_dist = calculate_utm_distance(lon1, lat1, lon2, lat2)
    geod_dist = calculate_geodesic_distance(lon1, lat1, lon2, lat2)
    
    assert utm_dist > 0
    assert geod_dist > 0
    # Difference should be relatively small for this distance
    assert abs(utm_dist - geod_dist) < 50.0
