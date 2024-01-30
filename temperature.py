import requests
from selectorlib import Extractor


class Temperature:
    """
    Represent a temperature value extracted from the timeanddate.com/weather webpage.
    """

    def __init__(self, country: str, city: str):
        self.country = country
        self.city = city

    def get_value(self):
        try:
            extractor = Extractor.from_yaml_file('temperature.yaml')
            r = requests.get(f'https://www.timeanddate.com/worldclock/{self.country}/{self.city}')
            raw_temperature = extractor.extract(r.text)
            temperature = int(raw_temperature['temp'].split()[0])
            return temperature
        except:
            print('Country and/or city not found. Please check input and try again.')
            return None


if __name__ == "__main__":
    temp_obj = Temperature('canada', '')
    print(temp_obj.get_value())
