"""The today command."""

import pyowm

from json import dumps

from .base import Base

import configparser

from . import __api_key__ as API_KEY

class Today(Base):
    """Say hi, world!"""
    
    def run(self):

        config = configparser.ConfigParser()
        config.sections()
        config.read('config.ini')

        owm = pyowm.OWM(API_KEY)

        observation = owm.weather_at_place('London,uk')
        w = observation.get_weather()

        print(observation.get_location())
        print(w.get_status())
        print(w.get_temperature('celsius'))
        print(w.get_detailed_status())
        print("today's weather")
 
