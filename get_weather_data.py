import requests

city_name = 'New Delhi'
API_key = 'bb3808839c6dae4bd443865888b584a3'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric"


response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print('city name is :',city_name)
    print('weather is :',data['weather'][0]['description'])
    print('current temperature is :',data['main']['temp'])
    print('current temperature feels like is :',data['main']['feels_like'])
    print('Humidity is :',data['main']['humidity'])
    print('Pressure is :',data['main']['pressure'])
    print('wind speed is :',data ['wind']['speed'] )