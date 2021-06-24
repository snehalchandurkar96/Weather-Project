import requests
#import os
from datetime import datetime

api_key = 'dd4d478fb782ce71c4ea1309d0b8d107'
location = input("Enter the city name: ")

comp_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(comp_api_link)
api_data = api_link.json()
#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

file = open("result.txt","w")

file.write("\n")
file.write("Weather Stats for - {} || {}".format(location.upper(),date_time))

file.write("\n")

file.write("Current temperature is: {:.2f} deg C".format(temp_city)) 

file.write("\n")

file.write("Current weather desc  :"+str(weather_desc))

file.write("\n")

file.write("Current Humidity      :"+ str(hmdt) + "%")

file.write("\n")

file.write("Current wind speed      :"+ str(wind_spd) + "kmph")

file.close()

