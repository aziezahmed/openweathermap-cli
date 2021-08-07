"""The today command."""

import pyowm

import time

import requests

import json

from .base import Base

import os, configparser

from tabulate import tabulate

from weather.user_settings import UserSettings

class Today(Base):

    def __init__(self, lat, lon, *args, **kwargs):
        self.lat = lat
        self.lon = lon

        super(Today,self).__init__(*args, **kwargs)
    
    def run(self):

        user_settings = UserSettings()
        api_key = user_settings.get_api_key()

        owm = pyowm.OWM(api_key)

        mgr = owm.weather_manager()
        one_call = mgr.one_call(lat=self.lat, lon=self.lon)

        weather = one_call.current
        temperature = weather.temperature("celsius").get("temp")
        feels_like = weather.temperature("celsius").get("feels_like")

        if(not temperature):
            temperature = weather.temperature("celsius").get("day")
            feels_like = weather.temperature("celsius").get("feels_like_day")
        status = weather.status
        detailed_status = weather.detailed_status

        table = []
        table.append(["Temperature",temperature])
        table.append(["Feels Like",feels_like])
        table.append(["Status",status])
        table.append(["Detail",detailed_status])
        
        headers = ["Weather",'']
        print(tabulate(table, headers, tablefmt="psql"))



        
 
