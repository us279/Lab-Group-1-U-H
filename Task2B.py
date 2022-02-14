#1B Henry Wall
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
stations = build_station_list()
tol=0.8
update_water_levels(stations) #Update all new water levels
stations_over_threshold = stations_level_over_threshold(stations, tol)

for tuple in stations_over_threshold:
    print(tuple[0].name, tuple[1])