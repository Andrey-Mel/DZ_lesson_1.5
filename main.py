import requests
import datetime as dt

city = {'Дебальцево':3}
url = f'http://wttr.in/{city}'
weather_parameters = {
    'format': 2,
    'M': ''
}
response = requests.get(url, params=weather_parameters)
print(f'Погода в Дебальцево: {response.text}')
city_offset = city.values()
city_time = dt.datetime.utcnow() + dt.timedelta(hours=3)
f_time = city_time.strftime("%H:%M")
print(f'Время в Дебальцево {f_time}')
