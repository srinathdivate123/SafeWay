from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import requests

@api_view(['GET', 'POST'])
def RepeatGetInfoView(request):
    if request.method == 'GET':
        return Response({"Status": "This is test data sent by GET request"})
    if request.method == 'POST':
        content = json.loads(request.body)
        latitude = content['latitude']
        longitude = content['longitude']
        speed = content['speed']
        date = content['date']
        time = content['time']
        gender = content['gender']
        driver_age = content['driver_age']
        vehicle_age = content['vehicle_age']
        #weatherReturnData = LiveWeatherConditions(latitude, longitude, time)
        #weatherConditions = weatherReturnData[0]
        #elevation = weatherReturnData[1]
        return Response({"value":2, "text":"Text message shown on the screen to driver"})
    

def timeClassFunc(time):
    if float(time) >= 0 and float(time) <= 100:
        return 1
    if float(time) >= 100 and float(time) <= 200:
        return 2
    if float(time) >= 200 and float(time) <= 300:
        return 3
    if float(time) >= 300 and float(time) <= 400:
        return 4
    if float(time) >= 400 and float(time) <= 500:
        return 5
    if float(time) >= 500 and float(time) <= 600:
        return 6
    if float(time) >= 600 and float(time) <= 700:
        return 7
    if float(time) >= 700 and float(time) <= 800:
        return 8
    if float(time) >= 800 and float(time) <= 900:
        return 9
    if float(time) >= 900 and float(time) <= 1000:
        return 10
    if float(time) >= 1000 and float(time) <= 1100:
        return 11
    if float(time) >= 1100 and float(time) <= 1200:
        return 12
    if float(time) >= 1200 and float(time) <= 1300:
        return 13
    if float(time) >= 1300 and float(time) <= 1400:
        return 14
    if float(time) >= 1400 and float(time) <= 1500:
        return 15
    if float(time) >= 1500 and float(time) <= 1600:
        return 16
    if float(time) >= 1600 and float(time) <= 1700:
        return 17
    if float(time) >= 1700 and float(time) <= 1800:
        return 18
    if float(time) >= 1800 and float(time) <= 1900:
        return 19
    if float(time) >= 1900 and float(time) <= 2000:
        return 20
    if float(time) >= 2000 and float(time) <= 2100:
        return 21
    if float(time) >= 2100 and float(time) <= 2200:
        return 22
    if float(time) >= 2200 and float(time) <= 2300:
        return 23
    if float(time) >= 2300 and float(time) <= 2359:
        return 24


def LiveWeatherConditions(latitude, longitude, time):
    time_class = timeClassFunc(time)
    base_link = 'https://api.weather.gov/points/'+str(latitude)+','+str(longitude)
    
    while(True):
        base_link_response = requests.get(base_link)
        print('ran 1st')
        if base_link_response.status_code != 500:
            break
        
    json_base_link_response = json.loads(base_link_response.text)
    while(True):
        main_link_response = requests.get((json_base_link_response['properties'])['forecastHourly'])
        print('ran 2nd')
        if main_link_response.status_code != 500:
            break

    json_main_link_response = json.loads(main_link_response.text)
    parent_data = ((json_main_link_response['properties'])['periods'])[time_class-1]
    elevation = ((json_main_link_response['properties'])['elevation'])['value']
    temperature = parent_data['temperature']
    probabilityOfPrecipitation = (parent_data['probabilityOfPrecipitation'])['value']
    windSpeed = (parent_data['windSpeed'])[:2]
    shortForecast = parent_data['shortForecast']
    
    if int(windSpeed)>30 or int(temperature)<=40:
        return [2, elevation]
    elif 'Clear' in shortForecast or 'CLEAR' in shortForecast or 'clear' in shortForecast:
        return [3, elevation]
    elif 'Cloudy' in shortForecast or 'CLOUDY' in shortForecast or 'cloudy' in shortForecast:
        return [4, elevation]
    elif int(probabilityOfPrecipitation)>=40 or 'Rain' in shortForecast or 'RAIN' in shortForecast or 'rain' in shortForecast:
        return [5, elevation]
    elif 'Snow'in shortForecast or 'SNOW' in shortForecast or 'snow' in shortForecast or int(temperature)<=35:
        return [6, elevation]
    else:
        return [7, elevation]