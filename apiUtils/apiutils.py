import json

import requests
from utilities.configManager import ConfigManager
from utilities.jsonlogger import JsonLogger


class ApiUtils:

    @staticmethod
    def rest_post(url_parts, data):
        base_url = ConfigManager.get_config_value("Url")
        response = requests.post(base_url+url_parts, data)

        return response

    @staticmethod
    def rest_get(url_parts):
        base_url = ConfigManager.get_config_value("Url")
        response = requests.get(base_url+url_parts)

        return response

    @staticmethod
    def content_type(response):
        try:
            response.raise_for_status()
            content_type = response.headers.get('content-type')
            if 'application/json' not in content_type:
                return False
            return True
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    @staticmethod
    def id_sort(response):
        posts = json.loads(response.text)
        ids = [post["id"] for post in posts]
        return ids == sorted(ids)