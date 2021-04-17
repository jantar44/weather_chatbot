import requests

def get_lat_lon(city, country=''):

    def get_api_key():
        return 'API_KEY'

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

    def get_api_key():
        return '13845f6d2c046e62f2d5fcb1f148a6c7'

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
