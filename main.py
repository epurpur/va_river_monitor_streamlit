#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:06:26 2020

@author: ep9k
"""

import streamlit as st
import pandas as pd
from va_river_classes import RiverAPI    #my own module


st.title("Central Virginia River Monitor")

st.subheader('So you are never left high and dry')

# river_site_info = {
#     'South Fork Rivanna River': ['02032515', 38.10180306, -78.4605666],
#     'James River': ['02025500', 37.5012508, -79.2625287],
#     'Moormans River': ['02032250', 38.1406902, -78.5558478],
#     'Tye River': ['02027000', 37.71541868, -78.981691],
#     'Piney River': ['02027500', 37.7023625, -79.0275254]
#     }

river_site_info = {
    'South Fork Rivanna River': '02032515',
    'James River': '02025500',
    'Moormans River': '02032250',
    'Tye River': '02027000',
    'Piney River': '02027500'
    }

# current_data_list = []

# #iterate through sites and collect current water data
# for river_name, site_number in river_site_info.items():
# 	data = RiverAPI(river_name, site_number)
# 	current_water_level = data.get_current_water_level()
# 	current_data_list.append(current_water_level)

# #write data to csv file
# va_river_data = RiverAPI.read_from_and_write_to_csv(current_data_list)



import matplotlib.pyplot as plt
import numpy as np

values = [189, 186, 186, 186, 186, 595, 587, 462]
current_value = 345

plt.title('South Fork Rivanna River')
plt.axhline(y=np.mean(values), color='red', linestyle="--", label='Average Water Level')
plt.legend()

plt.ylim(min(values) * .9, max(values) * 1.1)

plt.bar('Current Water Level', current_value)

st.pyplot()

plt.grid(axis='y', linestyle='-')

plt.subplots_adjust(left=0.1, right=0.11, top=0.9, bottom=0.1)

plt.show()








