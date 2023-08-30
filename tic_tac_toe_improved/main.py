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

clients = []
players = ["o", "x"]


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
    player_x_name_set = False
    player_o_name_set = False
    while True:
        # Accept Connection
        client, address = server.accept()
        clients.append(client)
        print("Connected with {}".format(str(address)))
        if not player_x_name_set:
            clients[0].send("x".encode(FORMAT))
            player_x_name_set = True
        if not player_o_name_set and len(clients) == 2:
            clients[1].send("o".encode(FORMAT))
            player_o_name_set = True

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(f"Server is listening on [{ADDR}]")
receive()



"""
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

clients = []
players = ["o", "x"]


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
    player_x_name_set = False
    player_o_name_set = False
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        clients.append(client)

        if not player_x_name_set:
            clients[0].send("x".encode(FORMAT))
            player_x_name_set = True
        if not player_o_name_set and len(clients) == 2:
            try:
                clients[1].send("o".encode(FORMAT))
                player_o_name_set = True
            except:
                print("Client disconnected before sending 'o' name")


        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(f"Server is listening on [{ADDR}]")
receive()


"""