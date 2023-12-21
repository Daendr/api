import inspect
import os
import json
from datetime import datetime


class JsonLogger:

    @staticmethod
    def log_to_json(log_data, value=''):
        log_directory = os.path.join('..', 'logs')

        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        caller_frame = inspect.stack()[1]
        method_name = caller_frame[3]

        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

        log_filename = f'log_{method_name}_{value}_{timestamp}.json'
        log_path = os.path.join(log_directory, log_filename)

        with open(log_path, 'a', encoding='utf-8') as log_file:
            json.dump(log_data, log_file, ensure_ascii=False, indent=2)
