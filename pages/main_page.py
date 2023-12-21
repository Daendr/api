import requests
from utilities.jsonlogger import JsonLogger


class MainPage:

    @staticmethod
    def post(message, post_data, directory, status):
        log_data = {
            'message': message,
            'data': []
        }
        url = 'https://jsonplaceholder.typicode.com/{}'.format(directory)
        response = requests.post(url, json=post_data)
        assert response.status_code == status, f"Ошибка при запросе: {response.status_code}"
        posts = response.json()
        log_data['data'] = posts
        JsonLogger.log_to_json(log_data)
        created_post = response.json()
        assert created_post['title'] == post_data['title']
        assert created_post['body'] == post_data['body']
        assert created_post['userId'] == post_data['userId']
        assert 'id' in created_post, "Отсутствует 'id' в ответе"

    @staticmethod
    def get(message, status, directory, user_id=''):
        log_data = {
            'message': message,
            'data': []
        }
        url = 'https://jsonplaceholder.typicode.com/{0}/{1}'.format(directory, str(user_id))
        response = requests.get(url)
        assert response.status_code == status, f"Ошибка при запросе: {response.status_code}"
        posts = response.json()
        if posts:
            log_data['data'] = posts
        if user_id and status != 404:
            assert log_data['data']['id'] == user_id
        JsonLogger.log_to_json(log_data, str(user_id))
