import socket


def request_file(file_name):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))
    client_socket.sendall(file_name.encode())
    data = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        data += chunk
    client_socket.close()
    return data


file_name = input("qual o nome do arquivo? ")
data = request_file(file_name)
print("Arquivo '{}' recebido:\n{}".format(file_name, data.decode()))
