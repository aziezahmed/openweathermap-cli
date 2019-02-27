"""The week command."""

import pyowm

import time

from .base import Base

import os, configparser

from tabulate import tabulate

from weather.user_settings import UserSettings

class Week(Base):

    def __init__(self, lat, lon, *args, **kwargs):
        self.lat = lat
        self.lon = lon
        
        super(Week,self).__init__(*args, **kwargs)
    
    def run(self):

        user_settings = UserSettings()
        api_key = user_settings.get_api_key()

        owm = pyowm.OWM(api_key)
        forecast = owm.daily_forecast_at_coords(self.lat,self.lon, limit=5)
        f = forecast.get_forecast()
        location = f.get_location()
        
        table = []

        for weather in f:
            table.append([time.strftime('%d %b %Y', time.localtime(weather.get_reference_time())), weather.get_detailed_status(), weather.get_temperature('celsius')['min'], weather.get_temperature('celsius')['max']])
            
        headers = ['Date','Summary','Temp Min', 'Temp Max']
        print(tabulate(table, headers, tablefmt="psql"))

        

        
