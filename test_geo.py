from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
def test_stations_by_distance():
    p=(52.2053, 0.1218)
    tol = 1e-5
    stations= build_station_list()
    stations_and_distance = stations_by_distance(stations, p)
    assert  isinstance(stations_and_distance, list)
    for i in stations_and_distance:
        assert isinstance(i, tuple)
    assert stations_and_distance[0][0].name == 'Cambridge Jesus Lock'
    assert abs(stations_and_distance[0][1] - 0.8402364350834995)<tol


