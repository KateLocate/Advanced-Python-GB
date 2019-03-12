import socket
from helpers.jim import *


client_socket = socket.socket()
client_socket.connect(PORT_SETTINGS)
message = client_socket.recv(PACK)
print(f'Отчет о соединении: {message.decode()}\n')

while True:
    client_request = input('Введите трехзначный код ответа сервера, чтобы получить расшифровку(e.g. 100, 200):')
    try:
        RESPONSES[int(client_request)] is True

    except KeyError:
        print("Введен несуществующий код")
        continue
    client_request_in_json = write_request_to_json(client_request)
    client_socket.send(client_request_in_json)

    server_response = client_socket.recv(PACK)
    response = read_response_from_json(server_response)
    print(f'Код ответа: {response[0]}, сообщение от сервера: {response[1]}.')
    break

client_socket.close()
