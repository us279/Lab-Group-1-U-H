#Task 2E Uday Singh
import datetime
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels


stations = build_station_list()
update_water_levels (stations)
six_stations_with_highest_relative_levels = stations_highest_rel_level(stations,6) #This section of code ignores the first value because it is not correct
five_stations_with_highest_relative_levels = six_stations_with_highest_relative_levels[1:]
#this section of code plots the graphs for the 5 graphs. Time period = 10 days
for i in five_stations_with_highest_relative_levels:
    dt = 10
    station, relative_level = i
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_levels(station.name, dates, levels)
