import socket
import threading

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        client_socket.sendall(data)
        print(data.decode())
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5))
server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
