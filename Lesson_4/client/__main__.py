import json
import socket

if __name__ == '__main__':
    socket = socket.socket()
    socket.connect(('localhost', 7777))

    action = input('Введите команду: ')
    data = input('Введите текст: ')

    request_string = json.dumps({'action': action, 'data': data})

    socket.send(request_string.encode())

    while True:
        response = socket.recv(1024)

        if response:
            print(response.decode())
            socket.close()
            break
