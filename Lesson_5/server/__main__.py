import json
import socket
import logging
from routes import resolve
from protocol import *
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger('server_log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s- %(message)s')
handler = TimedRotatingFileHandler('server.log', when="W1")

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


sock = socket.socket()
sock.bind(('', 7777))
sock.listen(5)

try:
    while True:
        client, address = sock.accept()
        logger.debug(f'User connected: {address}')
        data = client.recv(1024)
        client_request = json.loads(data.decode('utf-8'))

        if validate_request(client_request):
            controller = resolve(client_request.get('action'))
            if controller:
                try:
                    response = controller(client_request)
                    logger.debug(f'Response formed:{response}.')
                except Exception:
                    response = make_response(client_request, 500, 'Internal server error')
                    logger.error('code 500: Internal server error.')
            else:
                response = make_404(client_request)
                logger.error(make_404(client_request))
        else:
            response = make_404(client_request)
            logger.error(make_404(client_request))

        response_string = json.dumps(response)
        client.send(response_string.encode('utf-8'))
        client.close()

except KeyboardInterrupt:
    logger.critical('Connection lost.')
    sock.close()
