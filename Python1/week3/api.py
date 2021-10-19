#https://home.openweathermap.org/api_keys
#http://open-notify.org/
#http://api.open-notify.org/astros.json
from distutils import text_file

# import requests
# from datetime import datetime
# # from pprint import pprint as pp
#
#
# endpoint = 'http://api.open-notify.org/iss-now.json'
#
#
# response = requests.get(endpoint)
#
#
# data = response.json()
# print(data)
#
# timestamp = data['timestamp']
# dt_object = datetime.fromtimestamp(timestamp)
#
# print('dt_object = ', dt_object)
#
# msg = "At {dt} the ISS was the following location, latitude: {lat} and longitude: {lon}".format(
#     dt = dt_object,
#     lat = data['iss_position']['latitude'],
#     lon=data['iss_position']['latitude']
# )
#
# with open('space_station_location.txt', 'a+') as text_file:
#     text_file.write(msg + '\n')




# endpoint = 'http://api.open-notify.org/iss-pass.json'
# payload  = {
#     'lat': 51.507,
#     'lon': 0.1278
#  }
#
# response = requests.get(endpoint, params=payload)
#
# data = response.json()
# pp(data)


# endpoint = 'http://api.open-notify.org/astros.json'
#
# response = requests.get(endpoint)
#
# data = response.json()
# pp(data)
#
#
#
# with open('astronauts.txt', 'w') as text_file:
#     for item in data['people']:
#         text_file.write(item['name'] + '\n')