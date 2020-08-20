#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 07:56:11 2020

@author: ep9k
"""

import requests
import json
from datetime import datetime
import pandas as pd


class RiverAPI():
    
    site_info = {
        'South Fork Rivanna River': ['02032515', 38.10180306, -78.4605666],
        'James River': ['02025500', 37.5012508, -79.2625287],
        'Moormans River': ['02032250', 38.1406902, -78.5558478],
        'Tye River': ['02027000', 37.71541868, -78.981691],
        'Piney River': ['02027500', 37.7023625, -79.0275254]
        }
    
    
    def __init__(self, site_number, lat, lon):
        self.site_number = site_number
        self.lat = lat
        self.lon = lon
    
    def get_current_water_level(self):
        """Takes river site id number and makes API request to waterservices.usgs.gov
        Then parses response to get current water level for river and returns it."""
        
        url = f'http://waterservices.usgs.gov/nwis/iv/?format=json&sites={self.site_number}&parameterCd=00060,00065&siteStatus=all'

        response = requests.request("GET", url)
        data = json.loads(response.text)
        
        #parses json response to get only value of current water level for given river
        current_water_level = data['value']['timeSeries'][0]['values'][0]['value'][0]['value']
        
        return current_water_level
    
    def get_historical_river_data(self, current_water_level):
        # """How can I use the output from current water level as input for this function? """
        

    
    
    def write_to_csv(self):
        """Takes water level data from get_river_data method and writes it to river_levels.csv """
        pass
    
        



test1 = RiverAPI('02027500', 37.7023625, -79.0275254)




        
        
