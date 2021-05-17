from itertools import cycle
from random import shuffle

from board.board import Board
from player.player import Player
from symbol.symbol import Symbol
from utils.constants import *
from utils.prints import *


class Controller:
    players = []
    player_1 = None
    player_2 = None
    board = Board()

    @staticmethod
    def create_player(msg):
        return Player(input(msg))

    @staticmethod
    def __is_valid_position(board, position):
        if position in LEGAL_MOVES:
            row, col = LEGAL_MOVES[position]
            return board[row][col] == EMPTY_CELL

    @staticmethod
    def __is_full_board(board):
        for row in board:
            if EMPTY_CELL in row:
                return False
        return True

    @staticmethod
    def __is_winner(board, row, col, symbol):
        check_current_row = all([board[row][c] == symbol for c in range(BOARD_SIZE)])
        check_current_col = all([board[r][col] == symbol for r in range(BOARD_SIZE)])
        if (row, col) in DIAGONAL_CELLS:
            check_main_diagonal = all([board[d][d] == symbol for d in range(BOARD_SIZE)])
            check_second_diagonal = all([board[d][BOARD_SIZE - d - 1] == symbol for d in range(BOARD_SIZE)])
            return any((check_current_row, check_current_col, check_main_diagonal, check_second_diagonal))
        return any((check_current_row, check_current_col))

    @staticmethod
    def __get_coordinates(position):
        return LEGAL_MOVES[position]

    def show_results(self):
        print_results(self.player_1, self.player_2)

    def assign_players_symbols(self):
        while True:
            msg = MSG_ASSIGN_SYMBOLS % {self.player_1.name}
            prompt = input(msg).upper()
            if prompt in VALID_SYMBOLS:
                self.player_1.set_symbol(Symbol(prompt))
                char2 = "O" if prompt == "X" else "X"
                self.player_2.set_symbol(Symbol(char2))
                break
            else:
                print_invalid_symbol_msg(prompt)

    def setup(self):
        self.player_1 = self.create_player(MSG_CREATE_PLAYER1)
        self.player_2 = self.create_player(MSG_CREATE_PLAYER2)
        self.assign_players_symbols()
        self.players.append(self.player_1)
        self.players.append(self.player_2)

    def switch_symbols(self):
        self.player_1.symbol, self.player_2.symbol = self.player_2.symbol, self.player_1.symbol

    def shuffle_players(self):
        shuffle(self.players)
        return self.players[0]

    def ask_for_position(self, name: str):
        while True:
            position = input(MSG_ASK_FOR_POSITION) % name
            if self.__is_valid_position(self.board.matrix, position):
                return position
            print_invalid_position_msg(position)

    def draw_position_on_board(self, x, y, symbol):
        self.board.matrix[x][y] = symbol

    def game_loop(self):
        players = cycle(self.players)
        for player in players:
            position = self.ask_for_position(player.name)
            row, col = self.__get_coordinates(position)
            self.draw_position_on_board(row, col, player.symbol.char)
            self.board.show_board()
            if self.__is_winner(self.board.matrix, row, col, player.symbol.char):
                player.wins_a_game()
                loosing_player = [pl for pl in self.players if not pl == player][0]
                loosing_player.looses_a_game()
                print_winner(player.name)
                break
            if self.__is_full_board(self.board.matrix):
                [pl.draws_a_game() for pl in self.players]
                print_tie()
                break

    def play(self):
        self.board.fill_board_numbers()
        self.board.show_board()
        self.board.clean_board()
        print_start_msg()
        starting_player = self.shuffle_players()
        print_shuffled_players(starting_player.name)
        self.players[0].set_turn(1)
        self.players[1].set_turn(2)
        self.game_loop()
