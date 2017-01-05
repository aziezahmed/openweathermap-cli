"""The today command."""

import pyowm

from json import dumps

from .base import Base


class Today(Base):
    """Say hi, world!"""
    
    def run(self):

        owm = pyowm.OWM('1eec8d995c77560d0b45f4a01ec7813d')

        observation = owm.weather_at_place('London,uk')
        w = observation.get_weather()
        print(w.get_status())
        
 
