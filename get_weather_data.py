import requests

api_key = 'bb3808839c6dae4bd443865888b584a3'

user_input = input("Enter city : ")

weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}')

if weather_data.json()['cod'] == '404':
    print("No city found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    feels_Like = weather_data.json()['main']['feels_like']
    humidity = weather_data.json()['main']['humidity']
    wind = weather_data.json()['wind']['speed']
    pressure = weather_data.json()['main']['pressure']
    
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F ")
    print(f"The temperature feels like in {user_input} is: {feels_Like} ")
    print(f"Humidity in {user_input} is : {humidity}")
    print(f"wind speed in {user_input} is : {wind}")
    print(f"pressure in {user_input} is :{pressure}")
