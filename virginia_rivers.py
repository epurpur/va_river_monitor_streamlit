import requests
import json
import csv 
from datetime import datetime




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


# 3. Create new csv data to it
    
# csvfile = open('/Users/ep9k/Desktop/va_river_monitor/river_levels.csv', 'a')

# fieldnames = ['Time Stamp', 'South Fork Rivanna River', 'James River', 'Moormans River', 'Tye River', 'Piney River']
    
# writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
# writer.writeheader()
    
# writer.writerow({
#         'Time Stamp': current_datetime_formatted,
#         'South Fork Rivanna River': rivanna_river_current_water_level,
#         'James River': james_river_current_water_level,
#         'Moormans River': moormans_river_current_water_level,
#         'Tye River': tye_river_current_water_level,
#         'Piney River': piney_river_current_water_level
#         })
    
    
# csvfile.close()


# 4. Append data to existing file

with open (r'/Users/ep9k/Desktop/va_river_monitor/river_levels.csv', 'a') as csvfile:
    
    writer = csv.writer(csvfile)
    
    writer.writerow([current_datetime_formatted,
                      rivanna_river_current_water_level, 
                      james_river_current_water_level, 
                      moormans_river_current_water_level,
                      tye_river_current_water_level, 
                      piney_river_current_water_level])
    
    csvfile.close()






