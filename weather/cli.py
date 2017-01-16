"""
weather

Usage:
  weather today
  weather location [--set=<location>]
  weather -h | --help
  weather --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  weather today
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


    import weather.commands
    options = docopt(__doc__, version=VERSION)

    for (k, v) in options.items(): 
        if hasattr(weather.commands, k) and v:
            module = getattr(weather.commands, k)
            weather.commands = getmembers(module, isclass)
            command = [command[1] for command in weather.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
