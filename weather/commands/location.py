"""The location command."""

from .base import Base

import os, configparser

class Location(Base):
    
    def run(self):

        user_config_dir = os.path.expanduser("~");
        user_config_path = user_config_dir + "/.openweathermap-cli-config.ini"

        if self.options['--set']:
            config = configparser.ConfigParser()
            config.sections()
            config.read(user_config_path)
            config.set('weather','location',self.options['--set'])
            
            with open(user_config_path, 'w') as configfile:
                config.write(configfile)
            print('location set to ' + self.options['--set'])

        else:
            config = configparser.ConfigParser()
            config.sections()
            config.read(user_config_path)
            print('Current location set as ' + config['weather']['location'])
 
