from numpy import float32
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():  #checking the output of the function is as intended
    stations = build_station_list()
    update_water_levels(stations)
    over_threshold_list = stations_level_over_threshold(stations, tol=0.8)
    assert isinstance(over_threshold_list, list) 
    for i in over_threshold_list:
        assert isinstance(i, tuple)
        assert isinstance(i[0], MonitoringStation)
        assert isinstance(i[1], float)
    
def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    N=10
    first_10_stations = stations_highest_rel_level(stations, N)
    assert isinstance(first_10_stations, list)
    assert len(first_10_stations) == 10
    for i in first_10_stations:
        assert isinstance(i, tuple)
        assert isinstance(i[0], MonitoringStation)
        assert isinstance(i[1], float)
