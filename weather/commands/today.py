"""The today command."""

import pyowm

import time

import requests

import json

from .base import Base

import os, configparser

from tabulate import tabulate

from . import __api_key__ as API_KEY

class Today(Base):

    def __init__(self, lat, lon, *args, **kwargs):
        self.lat = lat
        self.lon = lon

        super(Today,self).__init__(*args, **kwargs)
    
    def run(self):

        owm = pyowm.OWM(API_KEY)

        observation = owm.weather_at_coords(self.lat,self.lon)
        w = observation.get_weather()

        location = observation.get_location()

        table = []
        table.append(["Temperature",str(w.get_temperature('celsius')['temp'])])
        table.append(["Temp Max",str(w.get_temperature('celsius')['temp_max'])])
        table.append(["Temp Min",str(w.get_temperature('celsius')['temp_min'])])
        table.append(["Summary",w.get_status()])
        table.append(["Detail", w.get_detailed_status()])
        table.append(["Sunrise", time.strftime('%H:%M:%S', time.localtime(w.get_sunrise_time()))])
        table.append(["Sunset", time.strftime('%H:%M:%S', time.localtime(w.get_sunset_time()))])
        
        headers = [location.get_name(),'']
        print(tabulate(table, headers, tablefmt="psql"))



        
 
