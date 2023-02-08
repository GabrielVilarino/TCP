import socket
import threading


def handle_client(client_socket, client_address):
    request = client_socket.recv(1024).decode()
    try:
        with open(request, "rb") as file:
            data = file.read()
            client_socket.sendall(data)
    except FileNotFoundError:
        client_socket.sendall("Arquivo não encontrado".encode())
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(5)
    print("Servidor escutando na porta 12345...")
    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexão estabelecida com: {}".format(client_address))
        client_thread = threading.Thread(target=handle_client,
                                         args=(client_socket, client_address))
        client_thread.start()


start_server()
