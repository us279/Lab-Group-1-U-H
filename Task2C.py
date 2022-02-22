#2C Henry Wall
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
stations=build_station_list()
update_water_levels(stations)
highest_10_levels = stations_highest_rel_level(stations, 10) #Call function we have made

for tuple in highest_10_levels:
    print(tuple[0].name, tuple[1]) #Only print station name and its relative water level
