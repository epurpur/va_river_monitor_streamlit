#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 21:06:26 2020

@author: ep9k
"""

import streamlit as st
import pandas as pd
import va_river_classes as vrc


st.title("Central Virginia River Monitor")

st.subheader('So you are never left high and dry')

va_river_data = pd.read_csv('river_levels.csv')

columns_to_drop = ['Unnamed: 0']
va_river_data.drop(columns_to_drop, inplace=True, axis=1)



