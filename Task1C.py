from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
stations = build_station_list()
p=(52.2053, 0.1218)
r=10
full_data_within_radius = stations_within_radius(stations, p, r)
names_within_radius = []
for i in full_data_within_radius:
    names_within_radius.append(i.name)
sorted_nwr = sorted(names_within_radius)
print(sorted_nwr)