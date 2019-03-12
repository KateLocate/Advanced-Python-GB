import json
import re
import time


PORT_SETTINGS = ('localhost', 7777)
PACK = 1024
ENCODING = 'utf-8'
RESPONSES = {100: 'базовое уведомление',
             101: 'важное уведомление',
             200: 'OK',
             201: 'объект создан',
             202: 'подтверждение',
             400: 'неправильный запрос/JSON-объект',
             401: 'не авторизован',
             402: 'неправильный логин/пароль',
             403: 'пользователь заблокирован',
             404: 'пользователь/чат отсутствует на сервере',
             409: 'уже имеется подключение с указанным логином',
             410: 'адресат существует, но недоступен (offline)',
             500: 'ошибка сервера'}


def write_request_to_json(action):

    def get_unix_time():
        unix_time = int(time.time())
        return unix_time

    dict_to_json = {'action': int(action),
                    'date': get_unix_time()}

    json_data = json.dumps(dict_to_json)

    return json_data.encode(encoding=ENCODING)


def read_request_from_json(json_data):
    action = json.loads(json_data)

    match = action['action']
    return match


def write_response_to_json(response, alert=None):

    dict_to_json = {'response': int(response),
                    'alert': alert}

    json_data = json.dumps(dict_to_json)
    return json_data.encode(encoding=ENCODING)


def read_response_from_json(json_data):
    request = json.loads(json_data)

    code_match = request['response']
    alert_match = request['alert']

    matches = [code_match, alert_match]
    return matches
