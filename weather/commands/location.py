"""The location command."""

from .base import Base

import os, configparser

class Location(Base):
    
    def run(self):

        user_config_dir = os.path.expanduser("~") + "/.config"
        user_config = user_config_dir + "/user_config.ini"

        if self.options['--set']:
            config = configparser.ConfigParser()
            config.sections()
            config.read(user_config)
            config.set('weather','location',self.options['--set'])
            
            with open(user_config, 'w') as configfile:
                config.write(configfile)
            print('location set to ' + self.options['--set'])

        else:
            config = configparser.ConfigParser()
            config.sections()
            config.read(user_config)
            print('Current location set as ' + config['weather']['location'])
 
