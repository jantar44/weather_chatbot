import requests
import config

def get_api_key():
    return config.api_key

def get_lat_lon(city, country=''):
    try:
        response = requests.get('http://api.openweathermap.org/geo/1.0/direct?q='+city+
                                '&limit=1&appid='+get_api_key())

    except requests.exceptions.HTTPError as e:
        print('HTTP Error')
        print(e)

    except requests.exceptions.ConnectionError as e:
        print('Connection error')
        print(e)

    except requests.exceptions.RequestException as e:
        print('Other error')
        print(e)

    if not response:
        raise Exception('No connection available')
    
    return response

def get_forecast(lat, lon):

    try:
        response = requests.get('http://api.openweathermap.org/data/2.5/onecall?lat='+lat+
                            '&lon='+lon+'&units=metric&appid='+get_api_key())

    except requests.exceptions.HTTPError as e:
        print('HTTP Error')
        print(e)

    except requests.exceptions.ConnectionError as e:
        print('Connection error')
        print(e)

    except requests.exceptions.RequestException as e:
        print('Other error')
        print(e)

    if not response:
        raise Exception('No connection available')
    else:
        return response


print(get_lat_lon('Warsaw'))