import requests


print("\n****************WEATHER APP****************\n")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "3388164df1639df43faa856864458835"
CITY = input("Enter the name of location  ")

def convert_to_celcius(kelvin):
    celcius = kelvin-273
    return celcius

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()
temp_kelvin = response["main"]["temp"]
temp_celcius = convert_to_celcius(temp_kelvin)
humidity = response["main"]["humidity"]
pressure = response["main"]["pressure"]
feels_like = response["main"]["feels_like"]
feels_like_celcius = convert_to_celcius(feels_like)
max_temp = response["main"]["temp_max"]
min_temp = response["main"]["temp_min"]
max_temp_celcius = convert_to_celcius(max_temp)
min_temp_celcius = convert_to_celcius(min_temp)

print(f"Data for {CITY} is \n")
print(f"TEMPERATURE is: {temp_celcius} Celcius  ")
print(f"MAX TEMP was: {max_temp_celcius} Celcius ")
print(f"MIN TEMP was: {min_temp_celcius} Celcius ")
print(f"FEELS LIKE: {feels_like_celcius} ")
print(f"PRESSURE: {pressure} mbar ")
print(f"HUMIDITY: {humidity}% ")
