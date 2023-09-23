import socket
import threading
from online import set_game_for_player
from game import start_local_game
import tkinter as tk

def multiplayer():
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


    def broadcast(message, c=None):
        print(f"--------------\n{message}\n----------------")

        if c is not None:
            for client in clients:
                if client != c:
                    client.send(message) # send restart game message
        else:
            for client in clients:
                client.send(message)


    def handle(client):

        print(f"--------------\n{client}\n----------------")
        while True:
            try:
                # Broadcasting Messages
                message = client.recv(1024)
                print(f"--------------\n{message}\n----------------".encode(FORMAT))
                if message == "restart":
                    broadcast(message, client)
                else:
                    broadcast(message)
            except:
                # Removing And Closing Clients
                # index = clients.index(client)
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

if __name__ == "__main__":
    def start_game(option, window):
        if option == "lan":
            window.destroy()
            try:
                multiplayer()
                set_game_for_player()
            except OSError:
                set_game_for_player()
        else:
            window.destroy()
            start_local_game()


    root = tk.Tk()
    info_label = tk.Label(root, text="Choose your mode", font=("Tahoma", 20))
    info_label.pack()
    local_1v1_button = tk.Button(root, text="Local 1v1", command=lambda: start_game("local", root))
    local_1v1_button.pack()
    lan_1v1_button = tk.Button(root, text="LAN 1v1", command=lambda: start_game("lan", root))
    lan_1v1_button.pack()
    root.mainloop()
