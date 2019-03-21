import json
import socket
import logging
from datetime import datetime


logger = logging.getLogger('client_log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s- %(message)s')
handler = logging.FileHandler('client.log')

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost', 7777))

    action = input('Введите команду: ')
    data = input('Введите текст: ')

    request_string = json.dumps({'action': action,
                                 'time': datetime.now().timestamp(),
                                 'data': data})

    sock.send(request_string.encode())

    while True:
        response = sock.recv(1024)

        if response:
            print(response.decode())
            response_log = logger.debug(f'Response received: {response.decode()}')
            sock.close()
            break
