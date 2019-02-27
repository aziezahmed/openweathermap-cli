"""
weather

Usage:
  weather
  weather week
  weather api <api-key>
  weather -h | --help
  weather --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  weather
  weather week
  
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/aziezahmed/openweathermap-cli/
"""

import requests

import json

from docopt import docopt

from . import __version__ as VERSION

from weather.user_settings import UserSettings

def main():

    geo_location_url = 'https://freegeoip.live/json/'
    request = requests.get(geo_location_url)
    location = json.loads(request.text)
    lat = location['latitude']
    lon = location['longitude']

    from weather.commands import Today
    from weather.commands import Week
   
    options = docopt(__doc__, version=VERSION)

    user_settings = UserSettings()
    api_key = user_settings.get_api_key()

    if api_key == "none" and not options["api"]:
        print("you need to set your api key first")
        print("if you don't have one you can get your's free from openweathermap.org")
        print("example:");
        print("")
        print("weather api 99213MY89API3842KEY0943320900")

    elif options["api"]:
        user_settings.set_api_key(options["<api-key>"])
        
    elif options["week"]:
        forecast = Week(lat,lon,options)
        forecast.run()
    else:
        today = Today(lat,lon,options)
        today.run()
