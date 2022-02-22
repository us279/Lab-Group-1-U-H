import numpy as np
import matplotlib
import datetime
import matplotlib.dates
from scipy.misc import derivative
from sympy import poly
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import update_water_levels, build_station_list

#Task 2F Uday Singh
def polyfit(dates, levels, p):
	d0 = matplotlib.dates.date2num(dates[1])
	x = matplotlib.dates.date2num(dates)-d0
	y = np.asarray(levels)
	#This section of code finds the coeffiecient for the different terms in the polynomial expression
	p_coeff = np.polyfit(x, y, p)
	#This section of the code converts the coefficents into the polynomial expression
	poly = np.poly1d(p_coeff)
	return poly, d0

#Task 2G Uday Singh
#This section of code tries to find the rate of increase of water, by finding the derivative of the polynomial
def rate_of_increase(dates, levels, p):
    poly, d0 = polyfit(dates, levels, p)
    derivative = np.polyder(poly)
    return derivative[0]
#Task 2G Uday Singh
#This section of code groups the stations by their water level- 'high' level, 'mid' level and 'low' level
def water_level():
    stations = build_station_list()
    update_water_levels(stations)
    high = []
    mid = []
    low = []
    for station in stations:
        if station.relative_water_level() == None:
            pass
        elif station.relative_water_level() <1:
            low.append(station)
        elif station.relative_water_level() > 2:
            high.append(station)
        else:
            mid.append(station)
    return low, mid, high


