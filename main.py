#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:06:26 2020

@author: ep9k
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from va_river_classes import RiverAPI    #my own module


st.title("Central Virginia River Monitor")

st.subheader('So you are never left high and dry')


river_site_info = {
    'South Fork Rivanna River': '02032515',
    'James River': '02025500',
    'Moormans River': '02032250',
    'Tye River': '02027000',
    'Piney River': '02027500'
    }


current_data_list = []

#iterate through sites and collect current water data
for river_name, site_number in river_site_info.items():
	data = RiverAPI(river_name, site_number)
	current_water_level = data.get_current_water_level()
	current_data_list.append(current_water_level)

#write data to csv file
va_river_data = RiverAPI.read_from_and_write_to_csv(current_data_list)


#now make the plots in matplotlib
counter = 1

for river_name in river_site_info.keys():
	
	values = va_river_data[river_name].tolist()
	values = [float(i) for i in values]    #convert values from string to float

	current_value = current_data_list[counter]
	current_value = float(current_value)

	counter += 1

	plt.title(river_name)
	plt.axhline(y=sum(values)/len(values), color='red', linestyle="--", label='Average Water Level')
	plt.legend()

	plt.ylim(min(values) * .95, max(values) * 1.05)

	plt.bar('Current Water Level', current_value)

	plt.grid(axis='y', linestyle='-')

	plt.subplots_adjust(left=0.1, right=0.6, top=0.9, bottom=0.1)
	st.pyplot()    #makes the plot happen


	









