import socket
import threading

# Connection Data
HOST = '192.168.0.189'
PORT = 5050
ADDR = (HOST, PORT)
FORMAT = 'utf-8'
# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()

# Lists For Clients and Their Nicknames
clients = []
# nicknames = []


def broadcast(message):
    print(f"--------------\n{message}\n----------------")
    for client in clients:
        client.send(message)


def handle(client):
    print(f"--------------\n{client}\n----------------")
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            print(f"--------------\n{message}\n----------------".encode(FORMAT))
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(f"Server is listening on [{ADDR}]")
receive()
