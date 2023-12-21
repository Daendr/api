import pytest
from pages.main_page import MainPage
from utilities.generateRandomText import GenerateRandomText


class TestApi:

    @staticmethod
    @pytest.mark.test_api
    def test_api():
        log_message = "Шаг 1. Отправьте запрос GET, чтобы получить все сообщения (/posts)."
        MainPage.get(log_message, 200, 'posts')

        log_message = "Шаг 2. Отправьте запрос GET, чтобы получить пост с id=99 (/posts/99)."
        MainPage.get(log_message, 200, 'posts', 99)

        log_message = "Шаг 3. Отправьте запрос GET, чтобы получить пост с id=150 (/posts/150)."
        MainPage.get(log_message, 404, 'posts', 150)

        log_message = ("Шаг 4. Отправьте POST-запрос, чтобы создать сообщение с userId=1"
                   " и случайным телом и случайным заголовком (/posts).")
        post_data = {
            'title': GenerateRandomText.generate_random_text(),
            'body': GenerateRandomText.generate_random_text(),
            'userId': 1
        }
        MainPage.post(log_message, post_data, 'posts', 201)

        log_message = ("Шаг 5. Отправьте запрос GET, чтобы получить пользователей (/users).")
        MainPage.get(log_message, 200, 'users', 5)
