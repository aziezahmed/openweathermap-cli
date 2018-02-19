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
    
    def run(self):
        user_config_dir = os.path.expanduser("~");
        user_config_path = user_config_dir + "/.openweathermap-cli-config.ini"

        config = configparser.ConfigParser()
        config.sections()
        config.read(user_config_path)

        ##location = config['weather']['location']

        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']

        owm = pyowm.OWM(API_KEY)

        observation = owm.weather_at_coords(lat,lon)
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



        
 
