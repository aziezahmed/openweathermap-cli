"""The today command."""

import pyowm

from .base import Base

import os, configparser

from tabulate import tabulate

from . import __api_key__ as API_KEY

class Today(Base):
    
    def run(self):
        user_config_dir = os.path.expanduser("~");
        user_config_path = user_config_dir + "/.openweathermap-cli-config.ini"

        config = configparser.ConfigParser()
        config.sections()
        config.read(user_config_path)

        location = config['weather']['location']

        owm = pyowm.OWM(API_KEY)

        observation = owm.weather_at_place(location)
        w = observation.get_weather()

        location = observation.get_location()

        table = []
        table.append(["Temperature",str(w.get_temperature('celsius')['temp'])])
        table.append(["Summary",w.get_status()])
        table.append(["Detail", w.get_detailed_status()])

        headers = [location.get_name(),'']
        print(tabulate(table, headers, tablefmt="psql"))



        
 
