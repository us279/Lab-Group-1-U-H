
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


stations=build_station_list()
p= (52.2053, 0.1218)

station_distance = stations_by_distance(stations, p)
n_t= []
d= []
n_t_d=[]
for MonitoringStation, statdist in station_distance: 
    #need to only extract the name and town from all the station information, and pair up with the corresponding distance from p
    name = MonitoringStation.name
    town = MonitoringStation.town
    n_t.append((name, town))
    for statdist in station_distance:
        distance = statdist[1]
        d.append(distance)
n_t_d=list(zip(n_t, d))
#pair up the corresponding tuple elements from list of station info and distances from p
closest_stations = n_t_d[:10] #first 10 elements of list of stations sorted by distance
furthest_stations = n_t_d[-10:] #last 10 elements of list of stations sorted by distance
print('Closest 10 stations are:', closest_stations)
print('Furthest 10 stations are:', furthest_stations)
