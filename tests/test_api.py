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
    _id_step_4 = 1
    _id_step_5 = 5
    _expected_userId = 10

    @pytest.mark.test_api
    def test_api(self):
        Logger.info("Шаг 1. Отправьте запрос GET, (/posts).")
        responce_from_url = ApiUtils.r_get(ConfigManager.get_config_value("Posts"))
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        assert ApiUtils.get_content_type(responce_from_url), "Тело ответа не JSON"
        assert ApiUtils.is_sort_by_value(responce_from_url, ConfigManager.get_config_value("Value")),\
            "Сообщения не упорядочены по возрастанию"

        Logger.info("Шаг 2. Отправьте запрос GET, с id=99")
        responce_from_url = ApiUtils.r_get(ConfigManager.get_config_value("ParamPost").format(str(self._id_step_2)))
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        assert Root.from_dict(json.loads(responce_from_url.text)).id == self._id_step_2, "id not equals"
        assert Root.from_dict(json.loads(responce_from_url.text)).userId == self._expected_userId, "userId not equals"
        assert Root.from_dict(json.loads(responce_from_url.text)).title, "Заголовок не должен быть пустым"
        assert Root.from_dict(json.loads(responce_from_url.text)).body, "Тело не должно быть пустым"

        Logger.info("Шаг 3. Отправьте запрос GET, с id=150.")
        responce_from_url = ApiUtils.r_get(ConfigManager.get_config_value("ParamPost").format(str(self._id_step_3)))
        assert responce_from_url.status_code == requests.codes.not_found, "Статус код не равен 404"
        assert responce_from_url.text == ConfigManager.get_config_value("EmptyContent"),\
            "Тело ответа не должно содержать данных при статусе 404"

        Logger.info("Шаг 4. Отправьте POST-запрос, со случайным телом и случайным заголовком")
        post_data = {
            'title': GenerateRandomText.generate_random_text(),
            'body': GenerateRandomText.generate_random_text(),
            'userId': self._id_step_4}
        responce_from_url = ApiUtils.r_post(ConfigManager.get_config_value("Posts"), post_data)
        assert responce_from_url.status_code == requests.codes.created, "Статус код не равен 201"
        assert Root.from_dict(json.loads(responce_from_url.text)).title == post_data['title'],\
            "Заголовок не соответствует ожидаемому"
        assert Root.from_dict(json.loads(responce_from_url.text)).body == post_data['body'],\
            "Тело не соответствует ожидаемому"
        created_post = json.loads(responce_from_url.text)
        assert created_post['userId'] == str(post_data['userId']), "userId не соответствует ожидаемому"
        assert 'id' in created_post, "Отсутствует 'id' в ответе"

        Logger.info("Шаг 5. Отправьте запрос GET, и получите заданного пользователя.")
        responce_from_url = ApiUtils.r_get(ConfigManager.get_config_value("Users"))
        assert ApiUtils.get_content_type(responce_from_url), "Тело ответа не JSON"
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        assert (ApiUtils.get_value(responce_from_url, self._id_step_5, ConfigManager.get_config_value("Value"))
                == ApiUtils.give_expected_data()), "Данные пользователя не соответствуют ожидаемым"

        Logger.info("Шаг 6. Отправьте запрос GET,  с id=5 (/users/5).")
        responce_from_url = ApiUtils.r_get(ConfigManager.get_config_value("ParamUsers").format(str(self._id_step_5)))
        assert responce_from_url.status_code == requests.codes.ok, "Статус код не равен 200"
        assert User.from_dict(json.loads(responce_from_url.text)) == ApiUtils.give_expected_data(),\
            "Данные пользователя не соответствуют ожидаемым"
