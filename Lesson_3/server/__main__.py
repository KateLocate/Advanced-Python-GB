import socket
from helpers.jim import *


server_socket = socket.socket()
server_socket.bind(PORT_SETTINGS)
server_socket.listen(5)
client, client_address = server_socket.accept()

while True:
    print(f'Получен запрос на соединение от {str(client_address)}')
    response_string = 'Соединение произведено'
    client.send(response_string.encode(encoding=ENCODING))
    while True:
        message = client.recv(PACK)
        print('Запрос от клиента: ', message.decode())
        request_code = int(read_request_from_json(message.decode()))
        print('Код запроса:', request_code)
        if request_code in RESPONSES.keys():
            response_alert = RESPONSES[request_code]
            answer = write_response_to_json(request_code, response_alert)
        else:
            answer = 'error'

        client.send(answer)
        print(f'Код ответа: {request_code}, сообщение от сервера: {response_alert}.')
        break
    break

client.close()
