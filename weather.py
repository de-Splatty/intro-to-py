import json

file = open("weather.json", "r")

data = file.read()
# print(type(data))

json_data = json.loads(data)
# print(type(json_data))

print(json_data['main']['temp'])

weather = json_data['weather'][0]['main']
print(weather)

print(json_data['wind']['speed'])

from datetime import datetime

# JSON data
weather_data = {
   "sys": {
      "sunrise": 1726636384,
      "sunset": 1726680975
   }
}

# Extract sunrise and sunset timestamps
sunrise_epoch = weather_data["sys"]["sunrise"]
sunset_epoch = weather_data["sys"]["sunset"]

# Convert to human-readable format
sunrise_time = datetime.fromtimestamp(sunrise_epoch).strftime('%Y-%m-%d %H:%M:%S')
sunset_time = datetime.fromtimestamp(sunset_epoch).strftime('%Y-%m-%d %H:%M:%S')

print("Sunrise:", sunrise_time)
print("Sunset:", sunset_time)
