import requests
from . import config

def get_api_key():
    return config.api_key

def get_lat_lon(city, country=''):
    """Function downloads latitude & longitude from openweathermap.org

    Args:
        city (str): name of the city
        country (str, optional): name of the country. Defaults to ''.

    Raises:
        Exception: No connection available

    Returns:
        json: response from API (lat&lon)
    """
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
    """Function downloads forecast data from openweathermap.org

    Args:
        lat (str): latitude value of the city
        lon (str): longitude value of the city

    Raises:
        Exception: No connection available

    Returns:
        json: weather data from API
    """
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
