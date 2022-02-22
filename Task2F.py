import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels

stations = build_station_list()
update_water_levels (stations)
six_stations_with_highest_relative_levels = stations_highest_rel_level(stations,6)
five_stations_with_highest_relative_levels = six_stations_with_highest_relative_levels[1:]
#This section of code plots the graphs with the polynomials for the five graphs. Time period = 3 days
for i in five_stations_with_highest_relative_levels:
    dt = 3
    station, relative_level = i
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    plot_water_level_with_fit(station.name, dates, levels, 4)
