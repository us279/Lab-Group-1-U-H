#2B Henry Wall

def stations_level_over_threshold(stations, tol):
    "This function returns a list of tuples: (Station object with latest relative level > tol, Relative water level at that station)"
    s_l_o_t = []
    for i in stations:
        if i.relative_water_level() == None: #skip stations with no or inconsistent data
            continue
        elif i.relative_water_level() > tol: #add stations with a relative water level above our tolerance as part of a tuple to a list
            s_l_o_t.append((i, i.relative_water_level()))
    sorted_s_l_o_t = sorted(s_l_o_t, key=lambda x: x[1], reverse = True) #sort in descending order by second value in tuple
    return sorted_s_l_o_t
