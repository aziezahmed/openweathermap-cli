"""An Object to store and retrive user settings"""

import os, configparser

from os.path import expanduser

class UserSettings(object):
    def __init__(self):

        self.basedir = "~/.openweathermap-cli"

        if not os.path.exists(expanduser(self.basedir)):
            print("Creating base dir %s"%self.basedir)
            os.makedirs(expanduser(self.basedir))

        self.user_config_dir = os.path.expanduser(self.basedir);
        self.user_config_path = self.user_config_dir + "/openweathermap-cli.ini"

        self.config = configparser.ConfigParser()
        self.config.add_section('openweathermap-cli')
        self.config['openweathermap-cli']['api-key'] = "none"

        if not os.path.isfile(self.user_config_path):
            with open(self.user_config_path, 'w') as f:
                self.config.write(f)

        self.config = configparser.ConfigParser()
        self.config.sections()
        self.config.read(self.user_config_path)

    def get_api_key(self):
        return self.config['openweathermap-cli']['api-key']

    def set_api_key(self, api_key):
        self.config.set('openweathermap-cli','api-key',api_key)
        with open(self.user_config_path, 'w') as configfile:
            self.config.write(configfile)
