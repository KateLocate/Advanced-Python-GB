import socket


server_socket = socket.socket()
server_socket.bind(('', 7777))
server_socket.listen(5)

while True:
    client, client_address = server_socket.accept()
    print(f'Получен запрос на соединение от {str(client_address)}')
    response_string = 'Соединение произведено'
    client.send(response_string.encode('utf-8'))
    client.close()
