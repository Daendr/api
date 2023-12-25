import json
import os
import requests
from models.user import User
from utilities.configManager import ConfigManager


class ApiUtils:

    @staticmethod
    def r_post(url_parts, data):
        base_url = ConfigManager.get_config_value("Url")
        response = requests.post(base_url+url_parts, data)

        return response

    @staticmethod
    def r_get(url_parts):
        base_url = ConfigManager.get_config_value("Url")
        response = requests.get(base_url+url_parts)
        return response

    @staticmethod
    def get_content_type(response):
            response.raise_for_status()
            content_type = response.headers.get('content-type')
            return 'application/json' in content_type

    @staticmethod
    def is_sort_by_value(response, value):
        posts = json.loads(response.text)
        posts_list = [post[value] for post in posts]
        return posts_list == sorted(posts_list)

    @staticmethod
    def give_expected_data():
        json_path = os.path.join('..', 'test_data', 'user_data.json')
        with open(json_path, "r", encoding="utf-8") as file:
            expected_user_data_dict = json.load(file)
        expected_user_data = User.from_dict(expected_user_data_dict)
        return expected_user_data

    @staticmethod
    def get_value(responce, value, content_type):
        users_list = json.loads(responce.text)
        user = next((user for user in users_list if user.get(content_type) == value), None)
        return User.from_dict(user)
