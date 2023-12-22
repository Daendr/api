import json

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
