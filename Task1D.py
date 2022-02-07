from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

stations = build_station_list()
rivers = rivers_with_station(stations) #call function
print('\n Number of stations \n', len(rivers))
print('First ten rivers are: \n', sorted(list(rivers))[:10]) #gives different to what example gives, I am guessing it has updated and some have been added/removed

dictionary = stations_by_river(stations)

def s_o_r(river_name, stations): #repeating the same process for a few rivers, so efficient to define a function
    "This function returns list of station names on the river inputted"
    river = stations_by_river(stations)[river_name] #list of station objects
    station_names=[]
    for i in river:
        station_names.append(i.name) #only want the names of the station objects
    return sorted(station_names)

print('\n Stations on River Aire: \n', s_o_r('River Aire', stations)) #call the function for the rivers we want, with some formatting
print('\n Stations on River Cam: \n', s_o_r('River Cam', stations))
print('\n Stations on River Thames: \n', s_o_r('River Thames', stations))
