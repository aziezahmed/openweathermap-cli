"""The week command."""

import pyowm

import time

from .base import Base

import os, configparser

from tabulate import tabulate

from . import __api_key__ as API_KEY

class Week(Base):
    
    def run(self):
        user_config_dir = os.path.expanduser("~");
        user_config_path = user_config_dir + "/.openweathermap-cli-config.ini"

        config = configparser.ConfigParser()
        config.sections()
        config.read(user_config_path)

        location = config['weather']['location']

        owm = pyowm.OWM(API_KEY)
        forecast = owm.daily_forecast(location, limit=5)
        f = forecast.get_forecast()
        location = f.get_location()
        
        table = []

        for weather in f:
            table.append([time.strftime('%d %b %Y', time.localtime(weather.get_reference_time())), weather.get_detailed_status(), weather.get_temperature('celsius')['min'], weather.get_temperature('celsius')['max']])
            
        headers = ['Date','Summary','Temp Min', 'Temp Max']
        print(tabulate(table, headers, tablefmt="psql"))

        

        
