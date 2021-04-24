# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import weather_calculation

#   - action_get_specific_weather
#   - action_get_general_weather


class ActionCheckWeatherGeneral(Action):

    def name(self) -> Text:
        return "action_get_general_weather"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('location')
        city_forecast = weather_calculation.Forecast(city)
        city_forecast.get_value(label_key = 'weather', day = 1)

class ActionCheckWeatherSpecific(Action):

    def name(self) -> Text:
        return "action_get_specific_weather"
    
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('location')
        part = tracker.get_slot('type')
        city_forecast = weather_calculation.Forecast(city)
        city_forecast.get_value(label_key = part, day = 1)

# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
