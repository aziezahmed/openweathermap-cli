"""The location command."""

from json import dumps

from .base import Base

import configparser

class Location(Base):
    """Say hi, world!"""
    
    def run(self):
        if self.options['--set']:
            config = configparser.ConfigParser()
            config.sections()
            config.read('config.ini')
            config.set('weather','location',self.options['--set'])
            
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            print('location set to ' + self.options['--set'])

        else:
            config = configparser.ConfigParser()
            config.sections()
            config.read('config.ini')
            print('Current location set as ' + config['weather']['location'])


        #print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
 
