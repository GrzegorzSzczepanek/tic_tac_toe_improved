import random
import socket
import threading
from tkinter import *



# HEADER = 64
PORT = 5050
FORMAT = "utf-8"
# DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.189"
ADDR = (SERVER, PORT)
# SERVER = socket.gethostbyname(socket.gethostname())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

window = Tk()

player_text = StringVar()
players = ["o", "x"]
# variable used to check who's starting
player = random.choice(players)
buttons = []
x_wins, o_wins = 0, 0
win_balance = StringVar()
win_balance.set(f"X: {x_wins} | O: {o_wins}")
wins_label = Label


# p as third argument stands for player. I couldn't name it player because it wouldn't change
# between players at all
def set_buttons_for_players(row, column, p):
    print(p)
    buttons[row][column].config(state="disabled")
    # if buttons[row][column]['text'] == "" and check_winner(row, column, p) is False:
    if p == players[0]:
        buttons[row][column]['text'] = p

        if check_winner(row, column, p):
            end_game(p)
            return
    else:
        buttons[row][column]['text'] = p

        if check_winner(row, column, p):
            end_game(p)
            return


def write(row, column, player):
    client.send(f"{row},{column},{player}".encode(FORMAT))
    return


def receive():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "NICK":
                client.send(player.encode("ascii"))
            else:
                print(message)
            # message = list(map(lambda x: int(x), message.split(",")))
            message = message.split(",")
            print(message)

        except:
            print("An error occurred!")
            client.close()
            break
        if len(message) > 1:
            set_buttons_for_players(int(message[0]), int(message[1]), message[2])



def button_press(row, column):
    global player
    #write(row, column, player)
    write(row, column, player)
    # player change
    for i in players:
        if i != player:
            player = i
            break
    player_text.set(player + " turn")


def restart_game():
    for row in range(0, 20):
        for column in range(0, 20):
            buttons[row][column].config(state="normal",
                                        text="",
                                        bg="black")


def disable_all_buttons():
    for row in range(0, 20):
        for column in range(0, 20):
            buttons[row][column].config(state="disabled")


def end_game(winner):
    global x_wins, o_wins
    disable_all_buttons()
    player_text.set(winner + " wins!")
    if winner == "X":
        x_wins += 1
    else:
        o_wins += 1
    win_balance.set(f"x: {x_wins} | o: {o_wins}")


def use_message(cords):
    print(cords)


def color_winner(cords):
    for i in cords:
        buttons[i[0]][i[1]].config(bg="green")


def check_winner(row, column, player):
    # check left
    x = row
    y = column
    check = 0
    winning = []
    while y >= 0:
        # print(winning)
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                check += 1
                y -= 1
                # print(check)
                if check == 5:
                    color_winner(winning)
                    return True
            else:
                break
        except Exception:  # it repairs 'int object is no subscriptable errors
            break
    # check right
    y = column + 1
    while y <= len(buttons):
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                check += 1
                y += 1
                # print(check)
                if check == 5:
                    color_winner(winning)
                    return True

            else:
                winning = []
                break
        except Exception:
            break
    # check top
    x = row
    y = column
    check = 0

    while x >= 0:
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                check += 1
                x -= 1
                # print(check)
                if check == 5:
                    color_winner(winning)
                    return True

            else:
                break
        except Exception:  # it repairs 'int object is no subscriptable errors
            break
    # check bottom
    x = row + 1
    while x <= len(buttons):
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                check += 1
                x += 1
                # print(check)
                if check == 5:
                    color_winner(winning)
                    return True

            else:
                winning = []
                break
        except Exception:
            break
    # right-bottom diagonal
    x = row
    y = column
    check = 0

    while x <= len(buttons) and y <= len(buttons):
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                check += 1
                x += 1
                y += 1
                if check == 5:
                    color_winner(winning)
                    return True

            else:
                break
        except Exception:
            break
    # top-left diagonal
    x = row - 1
    y = column - 1

    while x >= 0 and y >= 0:
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                x -= 1
                y -= 1
                check += 1
                if check == 5:
                    color_winner(winning)
                    return True

            else:
                winning = []
                break
        except Exception:
            break
    # bottom-left diagonal
    x = row
    y = column
    check = 0
    while x <= len(buttons) and y <= len(buttons):
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                x += 1
                y -= 1
                check += 1
                if check == 5:
                    color_winner(winning)
                    return True

            else:
                break
        except Exception:
            break
    # top-right diagonal

    x = row - 1
    y = column + 1

    while x >= 0 and y <= len(buttons):
        try:
            if buttons[x][y]['text'] == player:
                winning.append([x, y])
                x -= 1
                y += 1
                check += 1
                # buttons.append()
                if check == 5:
                    color_winner(winning)
                    return True

            else:
                winning = []
                break
        except Exception:
            break

    return False


def generate_board():
    # window setup
    window.title("Tic Tac Toe 2")
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.resizable(False, False)

    button_fields = 20
    font_size = 20
    button_width = 2
    button_height = 1
    window_width = (button_fields - 1) * button_width * font_size
    window_height = button_fields * button_width * font_size + 10
    window_height = button_fields * button_width * font_size


    window.geometry("%dx%d" % (window_width, window_height))
    frame = Frame(window, bg="black")
    frame.grid(row=1, column=1, sticky="nsew")
    #option_buttons_frame = Frame(window, width=500, bg="black")

    info_frame = Frame(window,
                        bg="white",
                        width=window_width)
    info_frame.grid(row=2, column=1, sticky="nsew")
    info_frame.grid_columnconfigure(0, weight=1)
    info_frame.grid_columnconfigure(1, weight=1)
    info_frame.grid_columnconfigure(2, weight=1)

    restart_btn = Button(info_frame,
                        text="Restart Game",
                        bg="white",
                        fg="black",
                        font=('consolas', 15),
                        padx=0, pady=0,
                        command=restart_game)
    restart_btn.grid(row=0, column=2)


    player_text.set(player + "'s" + " turn")
    turn_label = Label(info_frame,
                        bg="white",
                        fg="black",
                        padx=0, pady=0,
                        textvariable=player_text,
                        font=('consolas', 30))
    # turn_label.pack()
    turn_label.grid(row=0, column=1)

    wins_label = Label(info_frame,
                        textvariable=win_balance,
                        bg="white",
                        fg="black",
                        padx=0, pady=0,
                        text="X: 1 | O: 0",
                        font=('consolas', 15))
    wins_label.grid(row=0, column=0)

    # setting fields for the game
    for row in range(0, button_fields):
        buttons.append([])
        for column in range(0, button_fields):
            buttons[row].append(Button(frame,
                                          text="",
                                          bg="#000",
                                          fg="white",
                                          width=button_width,
                                          height=button_height,
                                          font=('consolas',font_size),
                                          padx=0,
                                          pady=0,
                                          command=lambda row=row, column=column: button_press(row, column)))
            buttons[row][column].grid(row=row, column=column)



receive_thread = threading.Thread(target=receive)
receive_thread.start()

# write_thread = threading.Thread(target=write)
# write_thread.start()

generate_board()

#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.connect(("127.0.0.1", 15200))
window.mainloop()
#client.close()
