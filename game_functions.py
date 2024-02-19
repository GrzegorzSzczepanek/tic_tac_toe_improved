def restart_game(buttons):
    for row in range(0, 20):
        for column in range(0, 20):
            buttons[row][column].config(state="normal", text="", bg="black")


def disable_all_buttons(buttons):
    for row in range(0, 20):
        for column in range(0, 20):
            buttons[row][column].config(state="disabled")


def end_game(player, player_text, win_balance, buttons):
    disable_all_buttons(buttons)
    player_text.set(player + " wins!")
    # x: 1 | o: 0
    x_wins = int(win_balance.get().split(" ")[1])
    o_wins = int(win_balance.get().split(" ")[4])
    if player == "x":
        x_wins += 1
    else:
        o_wins += 1

    win_balance.set(f"x: {x_wins} | o: {o_wins}")


def color_winner(cords, buttons):
    for i in cords:
        buttons[i[0]][i[1]].config(bg="green")
