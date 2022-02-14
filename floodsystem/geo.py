# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import math
from math import sqrt

from sympy import stationary_points
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from floodsystem.stationdata import build_station_list

#Task1B Henry Wall
def stations_by_distance(stations, p):  
    "this function takes list of stations and point p which we want to know the distance away from, and returns sorted list of stations with distance from p"
    station_and_distance = []
    for station in stations:          #for each individual station in list of stations
        distance = haversine(station.coord, p)        #calculate distance from p
        station_and_distance.append((station, distance))      #add tuple of station (along with all its data) and its distance from p to a collectiove list
    return sorted_by_key(station_and_distance, 1)       #return the list we just made, sorted by distance, the 2nd key in the tuple
#need to run pytests for geo now

#Task1C Henry Wall
def stations_within_radius(stations, centre, r): #want to return a list of stations within radius r of geographic coordinate x
    "This function returns a list of stations within radius r of a geographical coordinate, it takes a list of stations, centre coordiante and radius"
    close_stations=[]
    for station in stations:
        if  haversine(station.coord, centre) < r:
            close_stations.append(station)
    return close_stations
            
#Task 1D Henry Wall
def rivers_with_station(stations): #want to return a list of rivers with stations
    "This function returns a list of rivers that have stations from a list of stations inputted"
    r_w_s = []
    for i in stations: #for each monitoring station, add its river to a list, this is obviously a list of rivers with monitoring stations
        r_w_s.append(i.river)
    return set(r_w_s) #return a set so we get no repeats

def stations_by_river(stations): #want to create a function that returns a dictionary mapping river names to a list of station objects along river
    "This function creates a dictionary that maps river keys to their associated station values, it takes a list of stations"
    r_n_w_s = rivers_with_station(stations)
    stations = build_station_list()
    def stations_on_each_river(rivers, stations):     #need list of all stations on a river, listed for all rivers, create new function that returns this
        stations_on_each_river_list = [[] for i in range(len(rivers))] #create list of empty lists, each corresponds to one river
        j=0
        dict_element_list = [] #empty list that will store dictionaries that only contain one river key for now
        for river_name in rivers:   #iterate for each river
            for station in stations: #iterate for each station
                if river_name == station.river: #if the station is on the river we are currently searching for
                    (stations_on_each_river_list[j]).append(station) #add the station to the river's corresponding list
            dict_element_list.append({river_name: stations_on_each_river_list[j]}) #add the singular dictionary {river: stations on it} to a list of dictionaries
            j=j+1 #move to the next empty list for the next river

        return dict_element_list #we are returning a list of dictionaries of form {river: stations on it}

    dict_list = stations_on_each_river(r_n_w_s, stations) #call function we just made to generate list of dictionary elements
    dictionary = {}
    for k in dict_list: #add elements to one main dictionary
        dictionary.update(k)
    return dictionary 

#Task 1E Uday Singh
def rivers_by_station_number(stations,N):
    "This function returns the rivers in descending order of the number of stations by that river "       
    dictionary = stations_by_river(stations)  #This section of code appends a tuple of river, with the number of stations per river to a list
    num_of_stations_per_river=[]
    for river in dictionary:
        num_of_stations_per_river.append((river,len(dictionary[river])))
    #It sorts the list created first alphabetically and then by the number of stations per river in descending order
    num_of_stations_per_river.sort(key=lambda tup: tup[0])
    num_of_stations_per_river.sort(key=lambda tup: tup[1], reverse=True)
    #This section of code returns the first N terms in the list
    n_s_r=[]
    n=1
    x=0
    while n<=N:
        n_s_r.append(num_of_stations_per_river[x])
        x +=1
        if num_of_stations_per_river[x][1]>num_of_stations_per_river[x+1][1]:    
            n+=1
    return(n_s_r)


               


