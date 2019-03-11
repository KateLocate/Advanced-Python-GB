import socket


client_socket = socket.socket()
client_socket.connect(('localhost', 7777))
message = client_socket.recv(1024)
client_socket.close()

print(f'Отчет о соединении: {message.decode()}')
