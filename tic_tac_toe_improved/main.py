import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 15200))
server.listen(1)

print("Server started!")

# accept incoming connections
client_socket, client_address = server.accept()
print("Accepted connection from ", client_address)


while True:
    data = client_socket.recv(2048)
    data = data.decode('utf-8')
    print("Received: ", data)

    client_socket.send(data.encode())
