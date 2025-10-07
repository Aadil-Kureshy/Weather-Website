from flask import Flask, render_template, request
import time
import requests
app = Flask(__name__)
DB = 'FLK_weatherData'
WDB = open(DB,'r+')

@app.route('/', methods=['POST', 'GET'])


def OpenHTML():
    WDB.seek(0)
    lst = []
    for n in WDB:
        p = n.split(',')
        lst.append(p[0]+","+p[1])
    return render_template('FLK_weatherIN.html', list1=lst)


@app.route('/newcity', methods=['POST','GET'])


def NewCity():
    if request.method == "POST":
        city = request.form['newcity_in']
        city1 = city.split(",")
        city2 = city1[0].capitalize()
        country = city1[1].strip().upper()
        print(city2, country)
        API_KEY = 'PUT KEY FROM OPENWEATHER HERE'
        API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={},{}&mode=json&units=metric&appid={}')
        data = requests.get(API_URL.format(city, country, API_KEY)).json()
        info = city2 + ", " + country
        if data['cod'] == "404":
            return "Error: City Not Found"
        CheckDB = open(DB,'r+')
        CheckDB.seek(0)
        for l in CheckDB:
            print(l)
            if info in l:
                return "Error: City In Database"
        else:
            Add_CityDB = open(DB, "a")
            Add_CityDB.seek(0)
            Add_CityDB.write("\n" + info)
            Add_CityDB.close()
            temp = round(data['main']['temp'], 1)
            temp = str(temp) + " C°"
            description = data['weather'][0]['description'].title()
            feels = round(data['main']['feels_like'], 1)
            feels = str(feels) + " C°"
            min_temp = round(data['main']['temp_min'], 1)
            min_temp = str(min_temp) + " C°"
            max_temp = round(data['main']['temp_max'], 1)
            max_temp = str(max_temp) + " C°"
            min_max_temp = min_temp + "- " + max_temp
            humidity = str(data['main']['humidity']) + "%"
            windspeed = round(data['wind']['speed'], 1)
            windspeed = str(windspeed) + " km"
            wind_degrees = data['wind']['deg']
            day = time.strftime("%A")
            num_date = time.strftime('%d')
            month = time.strftime('%m')
            date = month + " - " + num_date
            if wind_degrees in range(337, 361) or range(0, 24):
                wind_degrees = "North"
            if wind_degrees in range(24, 69):
                wind_degrees = "North-East"
            if wind_degrees in range(69, 114):
                wind_degrees = "East"
            if wind_degrees in range(114, 159):
                wind_degrees = "South-East"
            if wind_degrees in range(159, 204):
                wind_degrees = "South"
            if wind_degrees in range(204, 248):
                wind_degrees = "South-West"
            if wind_degrees in range(248, 294):
                wind_degrees = "West"
            if wind_degrees in range(294, 337):
                wind_degrees = "North-East"
            # print(description, temp, feels, min_max_temp, humidity, windspeed, wind_degrees)
            return render_template('FLK_weatherWP.html', day=day, date=date, city=city2, country=country, description=description, temp=temp, feels=feels, min_max_temp=min_max_temp, humidity=humidity, windspeed=windspeed, wind_degrees=wind_degrees)


@app.route('/city', methods=['POST','GET'])


def Weather():
    if request.method == "POST":
        city = request.form['City']
        city1 = city.split(",")
        city2 = city1[0]
        country = city1[1]
        print(city2, country)
        API_KEY = 'PUT KEY FROM OPEN WEATHER HERE'
        API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={},{}&mode=json&units=metric&appid={}')
        data = requests.get(API_URL.format(city, country, API_KEY)).json()
        temp = round(data['main']['temp'], 1)
        temp = str(temp) + " C°"
        description = data['weather'][0]['description'].title()
        feels = round(data['main']['feels_like'], 1)
        feels = str(feels) + " C°"
        min_temp = round(data['main']['temp_min'], 1)
        min_temp = str(min_temp) + " C°"
        max_temp = round(data['main']['temp_max'], 1)
        max_temp = str(max_temp) + " C°"
        min_max_temp = min_temp + "- " + max_temp
        humidity = str(data['main']['humidity']) + "%"
        windspeed = round(data['wind']['speed'], 1)
        windspeed = str(windspeed) + " km"
        wind_degrees = data['wind']['deg']
        day = time.strftime("%A")
        num_date = time.strftime('%d')
        month = time.strftime('%m')
        date = month + " - " + num_date
        if wind_degrees in range(337, 361) or range(0, 24):
            wind_degrees = "North"
        if wind_degrees in range(24, 69):
            wind_degrees = "North-East"
        if wind_degrees in range(69, 114):
            wind_degrees = "East"
        if wind_degrees in range(114, 159):
            wind_degrees = "South-East"
        if wind_degrees in range(159, 204):
            wind_degrees = "South"
        if wind_degrees in range(204, 248):
            wind_degrees = "South-West"
        if wind_degrees in range(248, 294):
            wind_degrees = "West"
        if wind_degrees in range(294, 337):
            wind_degrees = "North-East"
        #print(description, temp, feels, min_max_temp, humidity, windspeed, wind_degrees)
        return render_template('FLK_weatherWP.html', day = day, date = date, city=city2, country=country, description= description, temp= temp, feels= feels, min_max_temp= min_max_temp, humidity= humidity, windspeed= windspeed, wind_degrees= wind_degrees)



if __name__ == "__main__":

        app.run()

