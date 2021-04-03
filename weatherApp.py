import requests
import os
from datetime import datetime 

user_api=input("Enter your api : ")
city_name = input("Enter city name : ")


api_link= "https://api.openweathermap.org/data/2.5/weather?q="+city_name+ "&appid="+user_api

api_li_nk = requests.get(api_link)
api_data= api_li_nk.json()

if api_data['cod'] == '404' :
    print('Invalid city!!')
else:
    temp_arature = ((api_data['main']['temp']) - 273.15)
    wea_ther = api_data['weather'][0]['description']
    humi_dity = api_data['main']['humidity']
    wind_speed = api_data['wind']['speed']
    date_time = datetime.now().strftime(" %d %b %Y | %I:%M:%S %p ")

    print ("Weather stats for - {} | {}".format(city_name.upper(), date_time))
    print("Current Temperature : ", temp_arature,"deg C" )
    print("Weather : ",wea_ther)
    print("Humidity : ",humi_dity,"%")
    print("Wind Speed : ",wind_speed,"km/h")


