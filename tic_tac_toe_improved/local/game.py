import random
from tkinter import *


def button_press(row, column):
    global player

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


def check_winner(row, column):
    # check left
    x = row
    y = column
    check = 0

    while y >= 0:
        try:
            if buttons[x][y]['text'] == player:
                check += 1
                y -= 1
                print(check)
                if check == 5:
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
                check += 1
                y += 1
                # print(check)
                if check == 5:
                    return True
            else:
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
                check += 1
                x -= 1
                # print(check)
                if check == 5:
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
                check += 1
                x += 1
                # print(check)
                if check == 5:
                    return True
            else:
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
                check += 1
                x += 1
                y += 1
                if check == 5:
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
                x -= 1
                y -= 1
                check += 1
                if check == 5:
                    return True
            else:
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
                x += 1
                y -= 1
                check += 1
                if check == 5:
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
                x -= 1
                y += 1
                check += 1
                if check == 5:
                    return True
            else:
                break
        except Exception:
            break

    return False
    player_text.set(player + " turn")


def end_game(winner):
    player_text.set(winner + " wins!")
    restart_game()


def generate_board():
    # window setup
    window.title("Tic Tac Toe 2")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (480/2))
    y_cordinate = int((screen_height/2) - (600/2))

    window.geometry("{}x{}+{}+{}".format(480, 600, x_cordinate, y_cordinate))

    window.resizable(False, False)
    window.grid_rowconfigure(1, weight=1)
    window.grid_columnconfigure(0, weight=1)

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # window.geometry("%dx%d" % (480, 600))
    frame = Frame(window, bg="black")
    frame.grid(row=1, column=1, sticky="nsew")

    option_buttons_frame = Frame(window, width=500, bg="black")

    restart_btn = Button(frame,
                                text="Restart Game",
                                bg="#000",
                                width=2,
                                height=1,
                                fg="white",
                                command=restart_game).grid(row=2, column=2)

    player_text.set(player + "'s" + " turn")
    turn_label = Label(window, textvariable=player_text, font=('consolas', 30))
    turn_label.grid(row=2, column=1)

    for row in range(25):
        buttons.append([])
        for column in range(25):
            buttons[row].append(column)

    # setting fields for the game
    for row in range(0, 20):
        for column in range(0, 20):
            buttons[row][column] = Button(frame,
                                          text="",
                                          bg="#000",
                                          width=2,
                                          height=1,
                                          fg="white",
                                          command=lambda row=row, column=column: button_press(row, column))
            buttons[row][column].grid(row=row, column=column)


def restart_game():
    pass


window = Tk()

player_text = StringVar()
players = ["o", "x"]
# variable used to check who's starting
player = random.choice(players)
buttons = []

generate_board()


window.mainloop()

