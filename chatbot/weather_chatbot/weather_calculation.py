import pandas as pd
import json
try:
    import forecast_downloader
except ImportError:
    print('Import of forecast_downloader failed')

class Forecast:

    def __init__(self, city, country = ''):
        """[summary]

        :param city: Name of the city
        :type city: str
        :param country: Country of the city, defaults to ''
        :type country: str, optional
        :raises UserWarning: Warning is raised when 
        """        

        self.coordinates = forecast_downloader.get_lat_lon(city).json()[0]
        self.forecast = forecast_downloader.get_forecast(str(self.coordinates['lat']),str(self.coordinates['lon'])).json()
        if len(self.forecast) == 0:
            print('There is no data.')
            raise UserWarning
        #columns=['dt', 'sunrise', 'sunset', 'temp', 'feels_like', 'pressure', 'humidity', 'dew_point', 'wind_speed', 'wind_deg', 'weather', 'clouds', 'pop', 'uvi'])
    
    def search_day(self, data, day):
        for dt, value in data:
            if dt == day:
                return value
    
    def search_day_inner(self, data, day, label_key):

        if label_key is None:                                           #program is filling label key with default value if it is missing
            if data[0][1] in ('id','main','description','icon'):
                label_key = 'main'
            else:
                label_key = 'day'

        for dt, label, value in data:
            if dt == day:
                if label == label_key:
                    return value

    def daily_forecast_inner(self, label_key):

        daily_forcast = list()
        for day_forecast in self.forecast['daily']:
            for key, value in day_forecast[label_key].items():
                daily_forcast.append((day_forecast['dt'], key, value))

        return daily_forcast

    def daily_forecast(self, label_key):

        daily_forcast = list()
        for value in self.forecast['daily']:
            daily_forcast.append((value['dt'], value[label_key]))

        return daily_forcast

    def get_value(self, label_key, day, inner_label_key = None):

        if label_key in ('temp','feels_like','weather'):
            return self.search_day_inner(self.daily_forecast_inner(label_key), day, inner_label_key)
        else:
            return self.search_day(self.daily_forecast(label_key), day)
