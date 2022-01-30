from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

stations=build_station_list()
stations_and_centre = stations_by_distance(stations, (52.2053, 0.1218))

