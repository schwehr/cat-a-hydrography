import pytest
from pyproj import Transformer

def test_pyproj_wgs84_to_utm():
    # Setup transformer: WGS84 (EPSG:4326) to UTM Zone 32N (EPSG:32632)
    transformer = Transformer.from_crs("epsg:4326", "epsg:32632", always_xy=True)
    
    # Example coordinate: Oslo, Norway (~ 10.75 East, 59.91 North)
    lon, lat = 10.75, 59.91
    easting, northing = transformer.transform(lon, lat)
    
    # Asserting approximate coordinates in UTM Zone 32N
    assert 590000 < easting < 605000
    assert 6640000 < northing < 6650000

def test_pyproj_utm_to_wgs84():
    transformer = Transformer.from_crs("epsg:32632", "epsg:4326", always_xy=True)
    easting, northing = 597650, 6642100
    lon, lat = transformer.transform(easting, northing)
    assert 10.0 < lon < 11.0
    assert 59.0 < lat < 60.0
