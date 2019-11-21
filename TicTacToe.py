#!/usr/bin/python3


def display_board(board):
    print("\n")
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|" + "      |1|2|3|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|" + "      |4|5|6|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|" + "      |7|8|9|")
    print("\n")


def play_game():
    # Game setup
    board = [
        '_', '_', '_',
        '_', '_', '_',
        '_', '_', '_'
    ]
    current_player = "X"
    display_board(board)

    # Game loop
    while True:
        handle_turn(board, current_player)
        if game_is_over(board): break
        current_player = flipped_player(current_player)

    # Game over
    winner = get_winner_if_available(board)
    if winner == "X" or winner == "O":
        print("\n" + str(winner) + " won!")
    elif winner is None:
        print("It's a TIE.")


def handle_turn(board, player):
    print(player + "'s turn now.")
    position = input("Choose a position from 1 to 9: ")
    valid = False
    while not valid:
        while position not in [str(n) for n in range(1, 10)]:  # note to bro: това се нарича list comprehension, което е причината да обичам python :D
            position = input("Choose a position from 1 to 9: ")
        position = int(position) - 1
        if board[position] == "_":
            valid = True
        else:
            print("You can't go there. Go again.")
    board[position] = player
    display_board(board)


def game_is_over(board):
    winner = get_winner_if_available(board)
    is_full = board_is_full(board)
    return winner is not None or is_full


def get_winner_if_available(board):
    row_winner = check_rows(board)
    column_winner = check_columns(board)
    diagonal_winner = check_diagonals(board)
    if row_winner:
        return row_winner
    elif column_winner:
        return column_winner
    elif diagonal_winner:
        return diagonal_winner
    else:
        return None


def check_rows(board):
    row_1 = board[0] == board[1] == board[2] != "_"
    row_2 = board[3] == board[4] == board[5] != "_"
    row_3 = board[6] == board[7] == board[8] != "_"
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return None


def check_columns(board):
    column_1 = board[0] == board[3] == board[6] != "_"
    column_2 = board[1] == board[4] == board[7] != "_"
    column_3 = board[2] == board[5] == board[8] != "_"
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]
    return None


def check_diagonals(board):
    diagonal_1 = board[0] == board[4] == board[8] != "_"
    diagonal_2 = board[6] == board[4] == board[2] != "_"
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[6]
    return None


def board_is_full(board):
    return "_" not in board


def flipped_player(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"


def main():
    while True:
        prompt = input("Start another game? [y/n]: ")
        game_is_requested = prompt.lower() in ('y', 'yes', 'da', 'aidi')
        if not game_is_requested: break
        play_game()

    input("Press any key to quit the game.")

if __name__ == "__main__":  # Това нещо ще го виждаш често, забранява на следващия код да се изпълнява, когато файлът бива import-нат в друг; изъплнява се само когато рънваме текущия файл
    main()
