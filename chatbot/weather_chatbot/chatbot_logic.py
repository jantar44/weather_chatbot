import rasa

import weather_calculation

# nlp = spacy.load('en_core_web_sm')

def chatbot(sentence):
    city_similarity = nlp('Weather forecast for')
    sentence = nlp(sentence)
    min_similarity = 0.7

    if city_similarity.similarity(sentence) > min_similarity:
        for ent in sentence.ents:
            if ent.label_ == 'GPE':
                city = ent.text
            # if ent.label_ == 'DATE':
            #     time = ent.text
                break
            else:
                return 'You need to tell me bigger city to check.'
        city_forecast = weather_calculation.Forecast(city)
        weather = city_forecast.get_value('wind_speed',1617962400)
        if city_forecast is not None:
            print(f'In {city} there is {weather}')


chatbot('Weather forecast for Warsaw')


# a = weather_calculation.Forecast('Warszawa')
# print(a.get_value('wind_speed',1617962400))
# import rasa