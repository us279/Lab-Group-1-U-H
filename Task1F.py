# This section calls the different functions and classes
from floodsystem.station import MonitoringStation
from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
stations = build_station_list()

list_of_incorrect_data = inconsistent_typical_range_stations(stations)

print(list_of_incorrect_data)