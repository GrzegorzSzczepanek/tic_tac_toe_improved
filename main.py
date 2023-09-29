import tkinter as tk
from online import set_game_for_player
from game import start_local_game

if __name__ == "__main__":
    def start_game(option, window):
        window.destroy()
        if option == "lan":
            set_game_for_player()
        else:
            start_local_game()

    root = tk.Tk()
    info_label = tk.Label(root, text="Choose your mode", font=("Tahoma", 20))
    info_label.pack()
    local_1v1_button = tk.Button(root, text="Local 1v1", command=lambda: start_game("local", root))
    local_1v1_button.pack()
    lan_1v1_button = tk.Button(root, text="LAN 1v1", command=lambda: start_game("lan", root))
    lan_1v1_button.pack()
    root.mainloop()