# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

#1F Uday Singh
    def typical_range_consistent(self):
        if self.typical_range == None: #This returns false if there is no value stored in typical range
            return False
        elif self.typical_range[0]>self.typical_range[1]: #This returns false if the minimum value is greater than maximumu value in typical range
            return False
        else: #If the values are what expected it returns true
            return True
    

    #2B Henry Wall
    def relative_water_level(self):
        "This function returns latest water level as a fraction of the typical range"
        if self.latest_level == None:   #if no data
            return None
        elif self.typical_range_consistent() == False:  #if data is inconsistent
            return None
        elif self.typical_range_consistent() == True:
            fraction = (self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
            
            return fraction

#1F Uday Singh
def inconsistent_typical_range_stations(stations):
    list_of_inconsistent_data=[]
    for station in stations: 
        if station.typical_range_consistent() == False: #If typical range value in station is false it is appendeds it to a list
            list_of_inconsistent_data.append(station.name)
    list_of_inconsistent_data.sort() #Sorts the list alphabetically
    return list_of_inconsistent_data
 