import random
from tkinter import *
import socket


def restart_game():
    pass


def disable_all_buttons():
    for row in range(0, 20):
        for column in range(0, 20):
            buttons[row][column].config(state="disabled")


def end_game(winner):
    player_text.set(winner + " wins!")
    disable_all_buttons()


def button_press(row, column):
    global player
    clicked_button = str(row) + "," + str(column)
    client.send(clicked_button.encode())
    data = client.recv(2048)
    data = data.decode('utf-8')
    received_data = list(map(int, data.split(",")))
    row = received_data[0]
    column = received_data[1]
    print("received: ", data)

    buttons[row][column].config(state="disabled")

    if buttons[row][column]['text'] == "" and check_winner(row, column) is False:
        if player == players[0]:
            buttons[row][column]['text'] = player

            # print(buttons[row][column]['text'])
            if check_winner(row, column):
                end_game(player)
                return ""

            # change to other player
            player = players[1]
        else:
            buttons[row][column]['text'] = player

            if check_winner(row, column):
                end_game(player)
                return ""

            # change to other player
            player = players[0]

    # inform about another players turn
    player_text.set(player + " turn")

# check is number of current player symbols in row or column


def color_winner(cords):
    for i in cords:
        buttons[i[0]][i[1]].config(bg="green")


def check_winner(row, column):
    # check left
    x = row
    y = column
    check = 0
    winning = []
    while y >= 0:
        print(winning)
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
    player_text.set(player + " turn")


def generate_board():
    # window setup
    window.title("Tic Tac Toe 2")
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    button_fields = 20
    font_size = 20
    button_width = 2
    button_height = 1
    window_width = (button_fields - 1) * button_width * font_size
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
                        command=restart_game)
    restart_btn.grid(row=0, column=2)


    player_text.set(player + "'s" + " turn")
    turn_label = Label(info_frame,
                        bg="white",
                        fg="black",
                        textvariable=player_text,
                        font=('consolas', 30))
    # turn_label.pack()
    turn_label.grid(row=0, column=1)

    wins_label = Label(info_frame,
                        text="X: 1 | O: 0",
                        bg="white",
                        fg="black",
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


window = Tk()

player_text = StringVar()
players = ["o", "x"]
# variable used to check who's starting
player = random.choice(players)
buttons = []

generate_board()


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 15200))
window.mainloop()
client.close()
