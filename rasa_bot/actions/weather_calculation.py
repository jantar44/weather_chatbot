import pandas as pd
import json
try:
    import forecast_downloader
except ImportError:
    print('Import of forecast_downloader failed')

class Forecast:

    def __init__(self, city, country = ''):
        """Downloades forecast using forecast_downloader

        Args:
            city (str): name of the city.
            country (str, optional): name of the country. Defaults to ''.

        Raises:
            UserWarning: No data downloaded
        """
        self.coordinates = forecast_downloader.get_lat_lon(city).json()[0]
        self.forecast = forecast_downloader.get_forecast(str(self.coordinates['lat']),str(self.coordinates['lon'])).json()
        if len(self.forecast) == 0:
            print('There is no data.')
            raise UserWarning

        # print(self.forecast)
        #columns=['dt', 'sunrise', 'sunset', 'temp', 'feels_like', 'pressure', 'humidity', 'dew_point', 'wind_speed', 'wind_deg', 'weather', 'clouds', 'pop', 'uvi']
    
    def daily_forecast(self, label_key):
        """Function returns list of all avaialble data of single cathegory of forecast.
        (f.e. pressure values in next 5 days)

        Args:
            label_key (str): cathegory of forecast (i.e. pressure, hummidity)

        Returns:
            list: list of all data of single type
        """
        daily_forcast = list()
        for value in self.forecast['daily']:
            daily_forcast.append(value[label_key])

        return daily_forcast

    def search_day(self, data, day):
        """Functions returns value of forecast of needed day (from list returned from daily_forecast).

        Args:
            data (list): forecast data 
            day (str): needed day

        Returns:
            [str]: forecast value
        """
        return data[day]

    def daily_forecast_inner(self, label_key):
        """Function returns list of all avaialble data of single cathegory of forecast.
        Function applies to temperature, feel temperature and general weather

        Args:
            label_key (str): cathegory of forecast (i.e. feels like, temperature and general weather)

        Returns:
            list: list of all data of single type in format [key, value]
        """
        daily_forcast = list()
        for day_forecast in self.forecast['daily']:
            for key, value in day_forecast[label_key].items():
                daily_forcast.append((key, value))
        return daily_forcast

    def search_day_inner(self, data, day, label_key):
        """Functions returns value of forecast of needed day (from list returned from daily_forecast_inner).

        Args:
            data (list): forecast data 
            day (str): needed day
            label_key (str): inner cathegory
            result (list): list of values

        Returns:
            [str]: forecast value
        """
        if label_key is None:       #program is filling label key with default value if it is missing
            if data[0][1] in ('id','main','description','icon'):
                label_key = 'main'
            else:
                label_key = 'day'
                
        result = list()
        for label, value in data:
            if label == label_key:
                result.append(value)
        return result[day]

    def get_value(self, label_key, day, inner_label_key = None):
        """Function automatise getting the needed value

        Args:
            label_key (str): cathegory of forecast (i.e. pressure, hummidity)
            day (int): epoch value of time
            inner_label_key (str, optional): inner cathegory. Defaults to None.

        Returns:
            [str]: forecast value
        """
        if label_key in ('temp','feels_like','weather'):
            return self.search_day_inner(self.daily_forecast_inner(label_key), day, inner_label_key)
        else:
            return self.search_day(self.daily_forecast(label_key), day)
