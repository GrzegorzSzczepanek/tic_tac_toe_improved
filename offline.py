import random
import tkinter as tk
# from game_functions import restart_game, end_game, restart_game, color_winner
import game_functions as game


players = ["o", "x"]
# variable used to check who's starting
player = random.choice(players)
x_wins, o_wins = 0, 0


def start_local_game():
    global x_wins, o_wins

    window = tk.Tk()
    buttons = []
    player_text = tk.StringVar()
    win_balance = tk.StringVar()
    win_balance.set(f"x: {x_wins} | o: {o_wins}")

    def button_press(row, column):
        global player
        buttons[row][column].config(state="disabled")

        if buttons[row][column]["text"] == "" and check_winner(row, column) is False:
            if player == players[0]:
                buttons[row][column]["text"] = player

                if check_winner(row, column):
                    game.end_game(player, player_text, win_balance, buttons)
                    return
                # change to other player
                player = players[1]
            else:
                buttons[row][column]["text"] = player

                if check_winner(row, column):
                    game.end_game(player, player_text, win_balance, buttons)
                    return
                # change to other player
                player = players[0]

        # inform about another players turn if no one won
        player_text.set(player + " turn")

    # check is number of current player symbols in row or column

    def check_row(row, column):
        x = row
        y = column
        check = 0
        winning = []
        while y >= 0:
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    check += 1
                    y -= 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True
                else:
                    break
            except:  # it repairs 'int object is no subscriptable errors
                break
        # check right
        y = column + 1
        while y <= len(buttons):
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    check += 1
                    y += 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True

                else:
                    winning = []
                    break
            except:
                break

    def check_column(row, column):
        winning = []
       # check top
        x = row
        y = column
        check = 0
        while x >= 0:
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    check += 1
                    x -= 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True

                else:
                    break
            except:  # it repairs 'int object is no subscriptable errors
                break
        # check bottom
        x = row + 1
        while x <= len(buttons):
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    check += 1
                    x += 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True

                else:
                    winning = []
                    break
            except:
                break

    def check_left_to_right_diagonal(row, column):
        # right-bottom diagonal
        x = row
        y = column
        check = 0
        winning = []

        while x <= len(buttons) and y <= len(buttons):
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    check += 1
                    x += 1
                    y += 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True

                else:
                    break
            except:
                break
        # top-left diagonal
        x = row - 1
        y = column - 1

        while x >= 0 and y >= 0:
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    x -= 1
                    y -= 1
                    check += 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True

                else:
                    winning = []
                    break
            except:
                break

    def check_right_to_left_diagonal(row, column):
        # bottom-left diagonal
        # bottom-left diagonal
        x = row
        y = column
        winning = []
        check = 0
        while x <= len(buttons) and y <= len(buttons):
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    x += 1
                    y -= 1
                    check += 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True

                else:
                    break
            except:
                break
        # top-right diagonal

        x = row - 1
        y = column + 1

        while x >= 0 and y <= len(buttons):
            try:
                if buttons[x][y]["text"] == player:
                    winning.append([x, y])
                    x -= 1
                    y += 1
                    check += 1
                    if check == 5:
                        game.color_winner(winning, buttons)
                        return True

                else:
                    winning = []
                    break
            except:
                break

    def check_winner(row, column):
        if not (check_column(row, column) or
                check_row(row, column) or
                check_left_to_right_diagonal(row, column) or
                check_right_to_left_diagonal(row, column)):
            return False
        return True

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
        frame = tk.Frame(window, bg="black")
        frame.grid(row=1, column=1, sticky="nsew")
        # option_buttons_frame = Frame(window, width=500, bg="black")

        info_frame = tk.Frame(window, bg="white", width=window_width)
        info_frame.grid(row=2, column=1, sticky="nsew")
        info_frame.grid_columnconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=1)
        info_frame.grid_columnconfigure(2, weight=1)

        restart_btn = tk.Button(
            info_frame,
            text="Restart Game",
            bg="white",
            fg="black",
            font=("consolas", 15),
            padx=0,
            pady=0,
            command=lambda: game.restart_game(buttons),
        )
        restart_btn.grid(row=0, column=2)

        player_text.set(player + "'s" + " turn")
        turn_label = tk.Label(
            info_frame,
            bg="white",
            fg="black",
            padx=0,
            pady=0,
            textvariable=player_text,
            font=("consolas", 30),
        )
        # turn_label.pack()
        turn_label.grid(row=0, column=1)

        wins_label = tk.Label(
            info_frame,
            textvariable=win_balance,
            bg="white",
            fg="black",
            padx=0,
            pady=0,
            text="X: 1 | O: 0",
            font=("consolas", 15),
        )
        wins_label.grid(row=0, column=0)

        # setting fields for the game
        for row in range(0, button_fields):
            buttons.append([])
            for column in range(0, button_fields):
                buttons[row].append(
                    tk.Button(
                        frame,
                        text="",
                        bg="#000",
                        fg="white",
                        width=button_width,
                        height=button_height,
                        font=("consolas", font_size),
                        padx=0,
                        pady=0,
                        command=lambda row=row, column=column: button_press(
                            row, column
                        ),
                    )
                )
                buttons[row][column].grid(row=row, column=column)

    generate_board()
    window.mainloop()
