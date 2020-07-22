import requests
import json

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



james_river_current_water_level = data['value']['timeSeries'][0]['values'][0]['value'][0]['value']
tye_river_current_water_level = data['value']['timeSeries'][2]['values'][0]['value'][0]['value']
piney_river_current_water_level = data['value']['timeSeries'][4]['values'][0]['value'][0]['value']
moormans_river_current_water_level = data['value']['timeSeries'][6]['values'][0]['value'][0]['value']
rivanna_river_current_water_level = data['value']['timeSeries'][8]['values'][0]['value'][0]['value']



