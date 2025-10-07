#values required: description, temp, feels like, min-max temp, humidity, windspeed, wind gust
import requests
city = "London"
country = "GB"
API_KEY = '29d7b2f6bca9e3d53eccb79eab7252e5'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={},{}&mode=json&units=metric&appid={}')
data = requests.get(API_URL.format(city,country, API_KEY)).json()
print(data)
if data['cod'] == "404":
    print('Error')
else:
    temp = round(data['main']['temp'],1)
    description = data['weather'][0]['description'].title()
    feels = round(data['main']['feels_like'],1)
    min_temp = round(data['main']['temp_min'],1)
    min_temp = str(min_temp)
    max_temp = round(data['main']['temp_max'],1)
    max_temp = str(max_temp)
    min_max_temp = min_temp + "/" + max_temp
    humidity = str(data['main']['humidity']) + "%"
    windspeed = str(data['wind']['speed']) + "km"
    wind_degrees = data['wind']['deg']
    if wind_degrees in range(337,361) or range(0,24):
        wind_degrees = "N"
    if wind_degrees in range(24,69):
        wind_degrees = "NE"
    if wind_degrees in range(69,114):
        wind_degrees = "E"
    if wind_degrees in range(114,159):
        wind_degrees = "SE"
    if wind_degrees in range(159,204):
        wind_degrees = "S"
    if wind_degrees in range(204,248):
        wind_degrees = "SW"
    if wind_degrees in range(248,294):
        wind_degrees = "W"
    if wind_degrees in range(294,337):
        wind_degrees = "NE"

    print(description, temp, feels, min_max_temp, humidity, windspeed, wind_degrees)