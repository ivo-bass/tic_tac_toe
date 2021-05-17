MSG_CREATE_PLAYER1 = "Player 1 please type your name: "
MSG_CREATE_PLAYER2 = "Player 2 please type your name: "
MSG_ASSIGN_SYMBOLS = "%s would you like to play with 'X' or 'O'?: "
MSG_ASK_FOR_POSITION = '%s choose a free position [1-9]: '
MSG_PLAY_NEW_GAME = "Play new game? [y/n]: "


# TODO: String formatting does not work


def print_tie():
    print('\nIt\'s a tie')


def print_winner(name):
    print(f'\n{name} won!')


def print_invalid_symbol_msg(s):
    print(f'"{s}" is invalid symbol.')


def print_invalid_position_msg(p):
    print(f'"{p}" is invalid position.')


def print_show_board_numbers_msg():
    print('This is the numeration of the board:')


def print_results(pl1, pl2):
    print()
    print(pl1)
    print(pl2)


def print_start_msg():
    print('\nLet\'s go!\n')


def print_goodbye_msg():
    print('See you soon!')


def print_shuffled_players(name):
    print('\nShuffling players...')
    print(f'{name} starts the game.')


def print_board(board):
    print("\nBoard:")
    for row in board:
        print("|" + "|".join(row) + "|")