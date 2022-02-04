from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.station import MonitoringStation
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
def test_stations_by_distance():
    p=(52.2053, 0.1218)
    tol = 1e-5
    stations= build_station_list()
    stations_and_distance = stations_by_distance(stations, p)
    assert  isinstance(stations_and_distance, list) #check we output a list
    for i in stations_and_distance:
        assert isinstance(i, tuple) #check the list contains tuples
    assert stations_and_distance[0][0].name == 'Cambridge Jesus Lock' #check for some known values in list
    assert abs(stations_and_distance[0][1] - 0.8402364350834995)<tol

def test_stations_within_radius():
    p = (52.2053, 0.1218)
    r = 10
    stations= build_station_list()
    names_within_radius = []
    full_data_within_radius = stations_within_radius(stations, p, r)
    stations_within_radius_list = stations_within_radius(stations, p, r)
    assert isinstance(stations_within_radius_list, list) #check output is a list
    for i in stations_within_radius_list: #check contains MonitoringStation class types
        assert isinstance(i,MonitoringStation)
    for i in full_data_within_radius:
        names_within_radius.append(i.name)
    sorted_nwr = sorted(names_within_radius)
    assert (sorted_nwr)[0] == 'Bin Brook' #check known values
    assert (sorted_nwr)[-1] == 'Stapleford'

def test_rivers_with_station(): #should return a set of length 950, containing river name strings
    stations= build_station_list()
    river_names = rivers_with_station(stations)
    assert isinstance(river_names, set)
    for i in river_names:
        assert isinstance(i, str)
    assert len(river_names)==950

def test_stations_by_river(): #function should return a dictionary mapping river keys to the stations on that river 
    stations= build_station_list()
    dictionary = stations_by_river(stations)
    assert isinstance(dictionary, dict)
    assert len(dictionary) == len(rivers_with_station(stations)) #check that every river is in dictionary
   
