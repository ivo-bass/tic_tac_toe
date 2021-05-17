from utils.constants import EMPTY_CELL, BOARD_SIZE
from utils.prints import print_board


class Board:
    def __init__(self):
        self.matrix = []

    def fill_board_numbers(self):
        cell_number = 1
        for row_i in range(BOARD_SIZE):
            row = []
            for col_i in range(BOARD_SIZE):
                row.append(str(cell_number))
                cell_number += 1
            self.matrix.append(row)

    def show_board(self):
        print_board(self.matrix)

    def clean_board(self):
        self.matrix = [[EMPTY_CELL for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
