import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 5))
while True:
    msg = input()
    if msg == "exit":
        client_socket.close()
    else:
        client_socket.send(msg.encode())
