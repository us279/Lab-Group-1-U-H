#Task 2G Uday singh
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import rate_of_increase, water_level
import datetime


severe_risk = []
high_risk = []
moderate_risk = []
low_risk = []
#This section of code collects information from the function water_level in analysis and allocates it to the respective list
low, mid, high = water_level()

#In this section of code for every station in list 'high' it computes rate of increase of water level and assesses the risk of flodding in that station depending on rate of increase.
#The expressions except ignores any value that has an error due to being out of range or is missing a value for water level
for station in high:
    try:
        dt = 1
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        rate_of_increase_1 = rate_of_increase(dates, levels, 1)
        if rate_of_increase_1 > 2:
            severe_risk.append(station.name)
        elif rate_of_increase_1 >1:
            high_risk.append(station.name)
        else:
            moderate_risk.append(station.name)
    except IndexError:
        pass
    except KeyError:
        pass
#In this section of code for every station in list 'mid' it computes rate of increase of water level and assesses the risk of flodding in that station depending on rate of increase.
#The expressions except ignores any value that has an error due to being out of range or is missing a value for water level
for station in mid:
    try:
        dt = 1
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        rate_of_increase_2 = rate_of_increase(dates, levels, 1)
        if rate_of_increase_1 > 2:
            high_risk.append(station.name)
        elif rate_of_increase_1 >1:
            moderate_risk.append(station.name)
        else:
            low_risk.append(station.name)
    except IndexError:
        pass
    except KeyError:
        pass
#In this section of code for every station in list 'low' it computes rate of increase of water level and assesses the risk of flodding in that station depending on rate of increase.
#The expressions except ignores any value that has an error due to being out of range or is missing a value for water level
for station in low:
    try:
        dt = 1
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        rate_of_increase_3 = rate_of_increase(dates, levels, 1)
        if rate_of_increase_1 > 2:
            moderate_risk.append(station.name)
        else:
            low_risk.append(station.name)
    except IndexError:
        pass
    except KeyError:
        pass

print("There are ")
print(len(severe_risk))
print('\n')
print(" stations at severe risk")
print("There are ")
print(len(high_risk))
print('\n')
print(" stations at high risk")
print("There are ")
print(len(moderate_risk))
print('\n')
print(" stations at moderate risk")
print("There are ")
print(len(low_risk))
print('\n')
print(" stations at low risk")
