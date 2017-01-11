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
    with open("default_config.ini", 'w') as f:
        config.write(f)

    user_config_dir = os.path.expanduser("~") + "/.config"
    user_config = user_config_dir + "/user_config.ini"

    if not os.path.isfile(user_config):
        os.makedirs(user_config_dir, exist_ok=True)
        shutil.copyfile("default_config.ini", user_config)

    config = configparser.ConfigParser()
    config.read(user_config)


    import weather.commands
    options = docopt(__doc__, version=VERSION)

    for (k, v) in options.items(): 
        if hasattr(weather.commands, k) and v:
            module = getattr(weather.commands, k)
            weather.commands = getmembers(module, isclass)
            command = [command[1] for command in weather.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
