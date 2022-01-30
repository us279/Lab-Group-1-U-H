# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from math import sqrt
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):      #takes list of stations and point p which we want to know the distance away from
    station_and_distance = []
    for MonitoringStation in stations:          #for each individual station in list of stations
        distance = haversine(MonitoringStation.coord, p)        #calculate distance from p
        station_and_distance.append((MonitoringStation, distance))      #add tuple of station (along with all its data) and its distance from p to a collectiove list
    return sorted_by_key(station_and_distance, 1)       #return the list we just made, sorted by distance, the 2nd key in the tuple


    