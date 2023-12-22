import json
import os


class ConfigManager:
    @staticmethod
    def get_config_value(key):
        config_path = os.path.join('..', 'test_data', 'config.json')
        with open(config_path) as config_file:
            data = json.load(config_file)
            return data.get(key)
