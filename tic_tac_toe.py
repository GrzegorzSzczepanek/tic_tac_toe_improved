import tkinter as tk
from online import set_game_for_player
from game import start_local_game
from socket import inet_aton

if __name__ == "__main__":


    def join_to_host(window, ip_address, port):
        if not inet_aton(ip_address) or not port.isdigit() or int(port) not in range(1, 65535):
            tk.Label(window, text="IP address or port is invalid or such host doesn't exist").pack()
            return
        else:
            set_game_for_player(ip_address, port)


    def find_ip(window):
        for widget in window.winfo_children():
            widget.destroy()
        ip_label = tk.Label(window, text="host ip adrress")
        ip_label.pack()

        ip_entry = tk.Entry(window)
        ip_entry.pack()

        port_label = tk.Label(window, text="host port")
        port_label.pack()

        port_entry = tk.Entry(window)
        port_entry.pack()

        ip_submit = tk.Button(text="Find a game", command=lambda: join_to_host(window, ip_entry.get(), port_entry.get()))
        ip_submit.pack()


    def create_host(window, port):
        if port.isdigit() and int(port) in range(1, 65535):
            window.destroy()
            set_game_for_player(port=port)

    def create(window):
        for widget in window.winfo_children():
            widget.destroy()

        port_label = tk.Label(window, text="host port")
        port_label.pack()
        port_entry = tk.Entry(window)
        port_entry.pack()
        port_submit = tk.Button(text="Host a game", command=lambda: create_host(window, port_entry.get()))
        port_submit.pack()



    def start_game(option, window):
        if option == "lan":
            local_1v1_button.config(text="join a game", command=lambda: find_ip(window))
            lan_1v1_button.config(text="create a game", command=lambda: create(window))

        else:
            window.destroy()
            start_local_game()

    root = tk.Tk()
    info_label = tk.Label(root, text="Choose your mode", font=("Tahoma", 20))
    info_label.pack()
    local_1v1_button = tk.Button(
        root, text="Local 1v1", command=lambda: start_game("local", root)
    )
    local_1v1_button.pack()
    lan_1v1_button = tk.Button(
        root, text="LAN 1v1", command=lambda: start_game("lan", root)
    )
    lan_1v1_button.pack()
    root.mainloop()
