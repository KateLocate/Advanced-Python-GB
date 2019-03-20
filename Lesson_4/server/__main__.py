import json
import socket
from .text import *
from .routes import *


def get_server_response(client_request):
    action = client_request.get('action')
    resolved_routes = list(filter(lambda itm: itm.get('action') == action, get_server_routes()))
    route = resolved_routes[0] if resolved_routes else None
    if route:
        controller = route.get('controller')
        response = controller(client_request.get('data'))

    else:
        response = 'Команда не существует, попробуйте снова.'

    return response


if __name__ == '__main__':
    sock = socket.socket()
    sock.bind(('', 7777))
    sock.listen(5)

    while True:
        client, address = sock.accept()
        print(f'Соединение с пользователем: {address}')
        data = client.recv(1024)
        request = json.loads(
            data.decode('utf-8')
        )

        response_string = get_server_response(request)

        client.send(response_string.encode('utf-8'))
        client.close()
