from cProfile import label
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list
from haversine import haversine, Unit

stations=build_station_list()
p= (52.2053, 0.1218)

station_distance = stations_by_distance(stations, p)
n_t= []
d= []
for MonitoringStation in stations:
    name = MonitoringStation.name
    town = MonitoringStation.town
    n_t.append((name, town))
    for statdist in station_distance:
        distance = statdist[1]
        d.append(distance)
n_t_d= []
for i in range(len(n_t)):
    n_t_d += (tuple(n_t[i])) + tuple(d) 
print('test')





