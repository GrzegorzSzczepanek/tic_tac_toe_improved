import socket
import threading

HEADER = 64 # bytes
PORT = 5050
SERVER = "192.168.0.108"
#SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
# print(socket.gethostname())
# print(socket.gethostbyaddr("192.168.0.189"))
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDR)


messages = []
connections = []

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connections.append(addr)
    connected = True

    message_length = conn.recv(HEADER).decode(FORMAT)
    if message_length:
        message_length = int(message_length)
        message = conn.recv(message_length).decode(FORMAT)
        messages.append(message)

        # print(f"[{addr}] {message}")
        for i in messages:
            #if addr == i:
            conn.send(f"{i}\n".encode(FORMAT))

        print(messages, connected, connections, sep="\n")
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # When the new connection occurs we store IP adress of that connection
        # and port and object that's going to allow us to communicate back
        conn, addr = server.accept()
        # When a new connection occurs we pass that connection to handle clients
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CPNNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()



