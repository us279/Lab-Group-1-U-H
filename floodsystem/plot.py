import matplotlib.pyplot as plt
import matplotlib
import datetime
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit
import numpy as np
from floodsystem.stationdata import build_station_list

#Task 2E Uday Singh
def plot_water_levels(stations, dates, levels):
    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title("Water level for station :"+ stations + "in the last 10 days")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

#Task 2F Uday Singh
def plot_water_level_with_fit(station, dates, levels, p):
    if dates == []:
        pass
    else:
        polynomial, d0 = polyfit(dates, levels, p)
        stations = build_station_list()
        #This section of code returns evenly spaced points of typical range over the time period dates
        for station in stations:
            if station.name == station:
                typical_low=np.linspace(station.typical_range[0],station.typical_range[0],len(dates))
                typical_high=np.linspace(station.typical_range[1],station.typical_range[1],len(dates))
        
        #Plots
        plt.plot(dates, levels)
        plt.plot(dates, typical_low)
        plt.plot(dates, typical_high)

        # Add axis labels, rotate date labels and add plot title
        plt.xlabel('date')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45);
        plt.title("Water level for station :"+ stations + "in the last 10 days")

        #Display plot
        plt.tight_layout()  # This makes sure plot does not cut off date labels
        plt.show()   