#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:06:26 2020

@author: ep9k
"""

import streamlit as st
import matplotlib.pyplot as plt
import concurrent.futures

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


with concurrent.futures.ThreadPoolExecutor() as executor:
	result = executor.submit(RiverAPI.prep_current_water_data, river_site_info)
	current_data_list = result.result()


#write data to csv file
va_river_data = RiverAPI.read_from_and_write_to_csv(current_data_list)


# now make the plots in matplotlib
counter = 1

for river_name in river_site_info.keys():
	
	values = va_river_data[river_name].tolist()
	values = [float(i) for i in values]    #convert values from string to float

	current_value = current_data_list[counter]
	current_value = float(current_value)

	counter += 1

	ax = RiverAPI.make_plots(river_name, values)
	ax.bar('Current River Level', current_value)
	st.pyplot()












