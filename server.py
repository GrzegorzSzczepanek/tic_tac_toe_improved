import socket
import threading


def multiplayer():
    # Connection Data

    HOST = "192.168.0.189"
    PORT = 5050
    ADDR = (HOST, PORT)
    FORMAT = "utf-8"
    # Starting Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    clients = []

    def broadcast(message, c=None):
        if c is not None:
            for client in clients:
                if client != c:
                    client.send(message)  # send restart game message
        else:
            for client in clients:
                client.send(message)

    def handle(client):
        while True:
            try:
                # Broadcasting Messages
                message = client.recv(1024)

                print(f"--------------\n{message}\n----------------".encode(FORMAT))
                if message == "restart":
                    broadcast(message)
                else:
                    broadcast(message)
            except:
                clients.remove(client)
                client.close()
                server.close()
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
