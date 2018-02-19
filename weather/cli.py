"""
weather

Usage:
  weather
  weather week
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

def main():

    geo_location_url = 'http://freegeoip.net/json'
    request = requests.get(geo_location_url)
    location = json.loads(request.text)
    lat = location['latitude']
    lon = location['longitude']

    from weather.commands import Today
    from weather.commands import Week
   
    options = docopt(__doc__, version=VERSION)

    if (options["week"]):
        forecast = Week(lat,lon,options)
        forecast.run()
    else:
        today = Today(lat,lon,options)
        today.run()
