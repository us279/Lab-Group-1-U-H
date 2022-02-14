#2B Henry Wall

def stations_level_over_threshold(stations, tol):
    "This function returns a list of tuples: (Station object with latest relative level > tol, Relative water level at that station)"
    s_l_o_t = []
    for i in stations:
        if i.relative_water_level() == None: #skip stations with no or inconsistent data
            continue
        elif i.relative_water_level() > tol: #add stations with a relative water level above our tolerance as part of a tuple to a list
            s_l_o_t.append((i, i.relative_water_level()))
    s_l_o_t.sort( key=lambda x: x[1], reverse = True) #sort in descending order by second value in tuple
    return s_l_o_t

#2C Henry Wall
def stations_highest_rel_level(stations, N):
    "This function returns the first N rivers with the highest relative water levels"
    stations_and_level = []
    for station in stations:
        if station.relative_water_level() == None: #skip stations with no or inconsistent data
            continue
        else:
            stations_and_level.append((station, station.relative_water_level()))
    stations_and_level.sort(key=lambda x: x[1], reverse=True) #Sort by relative water level in descending order
    n=0
    first_N_station_levels = []
    while n<N:
        first_N_station_levels.append(stations_and_level[n]) #add (station, relative water level) to list
        n+=1
    return first_N_station_levels