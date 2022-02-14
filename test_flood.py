from numpy import float32
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_stations_level_over_threshold():  #checking the output of the function is as intended
    stations = build_station_list()
    over_threshold_list = stations_level_over_threshold(stations, tol=0.8)
    assert isinstance(over_threshold_list, list) 
    for i in over_threshold_list:
        assert isinstance(i, tuple)
        assert isinstance(i[0], MonitoringStation)
        assert isinstance(i[1], float)