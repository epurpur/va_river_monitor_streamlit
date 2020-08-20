import requests
import json
import csv 
from datetime import datetime
import pandas as pd




# 1. Get API data for current water levels in each river. Data source seen in URL object

site_numbers = {
    'South Fork Rivanna River': '02032515',
    'James River': '02025500',
    'Moormans River': '02032250',
    'Tye River': '02027000',
    'Piney River': '02027500'
    }

url = 'http://waterservices.usgs.gov/nwis/iv/?format=json&sites=02032515, 02025500, 02032250, 02027000, 02027500&parameterCd=00060,00065&siteStatus=all'

response = requests.request("GET", url)
data = json.loads(response.text)


rivanna_river_current_water_level = data['value']['timeSeries'][8]['values'][0]['value'][0]['value']
james_river_current_water_level = data['value']['timeSeries'][0]['values'][0]['value'][0]['value']
moormans_river_current_water_level = data['value']['timeSeries'][6]['values'][0]['value'][0]['value']
tye_river_current_water_level = data['value']['timeSeries'][2]['values'][0]['value'][0]['value']
piney_river_current_water_level = data['value']['timeSeries'][4]['values'][0]['value'][0]['value']


# 2. Get current datetime stamp

current_datetime = datetime.now()

current_datetime_formatted = current_datetime.strftime("%d-%b-%Y (%H:%M:%S.%f)")



    
# 3. Read CSV file
va_river_data = pd.read_csv('river_levels.csv')


#remove extraneous column which is added as row index by pandas
columns_to_drop = ['Unnamed: 0']
va_river_data.drop(columns_to_drop, inplace=True, axis=1)


# 4. Evaluate current data
if va_river_data['Time Stamp'].count() > 100:
    va_river_data = va_river_data.drop(va_river_data.index[0])


#write to dataframe
va_river_data = va_river_data.append({'Time Stamp': current_datetime_formatted, 
                                      'South Fork Rivanna River': rivanna_river_current_water_level,
                                      'James River': james_river_current_water_level,
                                      'Moormans River': moormans_river_current_water_level,
                                      'Tye River': tye_river_current_water_level,
                                      'Piney River': piney_river_current_water_level},
                                     ignore_index=True)


#convert columns to float from strings, then get mean value of column (average water level)
#these averages are of the last 100 river level readings at each site
va_river_data['South Fork Rivanna River'] = va_river_data['South Fork Rivanna River'].apply(float)
rivanna_average_water_level = va_river_data['South Fork Rivanna River'].mean()
rivanna_max_water_level = va_river_data['South Fork Rivanna River'].max()
rivanna_min_water_level = va_river_data['South Fork Rivanna River'].min()


va_river_data['James River'] = va_river_data['James River'].apply(float)
james_average_water_level = va_river_data['James River'].mean()
james_max_water_level = va_river_data['James River'].max()
james_min_water_level = va_river_data['James River'].min()

va_river_data['Moormans River'] = va_river_data['Moormans River'].apply(float)
moormans_average_water_level = va_river_data['Moormans River'].mean()
moormans_max_water_level = va_river_data['Moormans River'].max()
moormans_min_water_level = va_river_data['Moormans River'].min()


va_river_data['Tye River'] = va_river_data['Tye River'].apply(float)
tye_average_water_level = va_river_data['Tye River'].mean()
tye_max_water_level = va_river_data['Tye River'].max()
tye_min_water_level = va_river_data['Tye River'].min()


va_river_data['Piney River'] = va_river_data['Piney River'].apply(float)
piney_average_water_level = va_river_data['Piney River'].mean()
piney_max_water_level = va_river_data['Piney River'].max()
piney_min_water_level = va_river_data['Piney River'].min()




# 5. Write data back to csv file (overwrites existing file)
va_river_data.to_csv('river_levels.csv')
    







