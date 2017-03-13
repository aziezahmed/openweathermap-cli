"""
weather

Usage:
  weather
  weather week
  weather location [--set=<location>]
  weather -h | --help
  weather --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  weather
  weather week
  weather location
  weather location --set=London,uk
  
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/aziezahmed/openweathermap-cli/
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

import os, shutil, configparser


def main():

    config = configparser.ConfigParser()
    config.add_section('weather')
    config['weather']['location'] = "London,uk"
    
    user_config_dir = os.path.expanduser("~");
    user_config_path = user_config_dir + "/.openweathermap-cli-config.ini"

    if not os.path.isfile(user_config_path):
        with open(user_config_path, 'w') as f:
            config.write(f)


    from weather.commands import Today
    from weather.commands import Week
   
    options = docopt(__doc__, version=VERSION)

    if (options["week"]):
        forecast = Week(options)
        forecast.run()
    else:
        today = Today(options)
        today.run()
