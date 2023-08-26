import socket
import threading

# Connection Data
HOST = '192.168.0.189'
PORT = 5050
ADDR = (HOST, PORT)
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
            print(f"--------------\n{message}\n----------------".encode('ascii'))
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            #nickname = nicknames[index]
            #broadcast('{} left!'.format(nickname).encode('ascii'))
            #nicknames.remove(nickname)
            break


def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        # client.send('NICK'.encode('ascii'))
        # nickname = client.recv(1024).decode('ascii')
        # nicknames.append(nickname)
        clients.append(client)
        #print(clients)
        # Print And Broadcast Nickname
        # print("Nickname is {}".format(nickname))
        # broadcast("{} joined!".format(nickname).encode('ascii'))
        # client.send('Connected to server!'.encode('ascii'))
        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


print(f"Server is listening on [{ADDR}]")
receive()
