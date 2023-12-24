import json
import os

import pytest
import requests
from py_selenium_auto_core.logging.logger import Logger
from apiUtils.apiutils import ApiUtils
from models.root import Root
from models.user import User
from utilities.configManager import ConfigManager
from utilities.generateRandomText import GenerateRandomText


class TestApi:

    _id_step_2 = 99
    _id_step_3 = 150
    _id_step_4 = 1
    _id_step_5 = 5
    _expected_userId = 10

    @pytest.mark.test_api
    def test_api(self):
        Logger.info("Шаг 1. Отправьте запрос GET, (/posts).")
        responce_from_url = ApiUtils.rest_get(ConfigManager.get_config_value("Posts"))
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        assert ApiUtils.content_type(responce_from_url), "Тело ответа не JSON"
        assert ApiUtils.id_sort(responce_from_url), "Сообщения не упорядочены по возрастанию"

        Logger.info("Шаг 2. Отправьте запрос GET, с id=99")
        responce_from_url = ApiUtils.rest_get(ConfigManager.get_config_value("ParamPost").format(str(self._id_step_2)))
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        assert Root.from_dict(json.loads(responce_from_url.text)).id == self._id_step_2, "id not equals"
        assert Root.from_dict(json.loads(responce_from_url.text)).userId == self._expected_userId, "userId not equals"
        assert Root.from_dict(json.loads(responce_from_url.text)).title, "Заголовок не должен быть пустым"
        assert Root.from_dict(json.loads(responce_from_url.text)).body, "Тело не должно быть пустым"

        Logger.info("Шаг 3. Отправьте запрос GET, с id=150.")
        responce_from_url = ApiUtils.rest_get(ConfigManager.get_config_value("ParamPost").format(str(self._id_step_3)))
        assert responce_from_url.status_code == requests.codes.not_found, "Статус код не равен 404"
        assert responce_from_url.text == ConfigManager.get_config_value("EmptyContent"),\
            "Тело ответа не должно содержать данных при статусе 404"

        Logger.info("Шаг 4. Отправьте POST-запрос, со случайным телом и случайным заголовком")
        post_data = {
            'title': GenerateRandomText.generate_random_text(),
            'body': GenerateRandomText.generate_random_text(),
            'userId': self._id_step_4
        }
        responce_from_url = ApiUtils.rest_post(ConfigManager.get_config_value("Posts"), post_data)
        assert responce_from_url.status_code == requests.codes.created, "Статус код не равен 201"
        created_post = json.loads(responce_from_url.text)
        assert Root.from_dict(json.loads(responce_from_url.text)).title == post_data['title'], "Заголовок не соответствует ожидаемому"
        assert Root.from_dict(json.loads(responce_from_url.text)).body, "Тело не соответствует ожидаемому"
        assert created_post['userId'] == str(post_data['userId']), "userId не соответствует ожидаемому"
        assert 'id' in created_post, "Отсутствует 'id' в ответе"

        Logger.info("Шаг 5. Отправьте запрос GET, чтобы получить пользователя.")
        responce_from_url = ApiUtils.rest_get(ConfigManager.get_config_value("Users"))
        assert ApiUtils.content_type(responce_from_url), "Тело ответа не JSON"
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        users_list = json.loads(responce_from_url.text)
        user_with_id_5 = next((user for user in users_list if user.get("id") == self._id_step_5), None)
        assert user_with_id_5, f"Пользователь с id={self._id_step_5} не найден в списке пользователей"
        json_path = os.path.join('..', 'test_data', 'user_data.json')
        with open(json_path, "r", encoding="utf-8") as file:
            expected_user_data_dict = json.load(file)
        expected_user_data = User.from_dict(expected_user_data_dict)
        actual_user_data = User.from_dict(user_with_id_5)
        assert actual_user_data == expected_user_data, "Данные пользователя не соответствуют ожидаемым"

        Logger.info("Шаг 6. Отправьте запрос GET,  с id=5 (/users/5).")
        responce_from_url = ApiUtils.rest_get(ConfigManager.get_config_value("ParamUsers").format(str(self._id_step_5)))
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        user_with_id_5 = json.loads(responce_from_url.text)
        json_path = os.path.join('..', 'test_data', 'user_data.json')
        with open(json_path, "r", encoding="utf-8") as file:
            expected_user_data_dict = json.load(file)
        expected_user_data = User.from_dict(expected_user_data_dict)
        actual_user_data = User.from_dict(user_with_id_5)
        assert actual_user_data == expected_user_data, "Данные пользователя не соответствуют ожидаемым"