import pygame
from cell import Cell
from utility import valid


class Grid:
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

    def __init__(self, cols, rows, width, height, windows):
        self.cols = cols
        self.rows = rows
        self.width = width
        self.height = height
        self.windows = windows
        self.cells = [[Cell(i, j, self.board[i][j], width, height) for j in range(cols)] for i in range(rows)]
        self.board_model = None
        self.selected_cell = None

    def update_model_values(self):
        self.board_model = [[self.cells[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def selected(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cells[i][j].is_selected is True:
                    return True
                else:
                    return False

    def draw_grid(self, win):
        distance_width = self.width / 9
        distance_height = self.height / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                line_size = 5
            else:
                line_size = 2
            # Draw Horizontal
            pygame.draw.line(self.windows, (0, 0, 0), (0, i * distance_height), (self.width, i * distance_height),
                             line_size)
            # Draw Vertical
            pygame.draw.line(self.windows, (0, 0, 0), (i * distance_width, 0), (i * distance_width, self.height),
                             line_size)

        # Draw Boxes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw_cell(win)

    def select_cell(self, row, col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].is_selected = False

        if self.selected_cell == (row, col):
            self.increase_value()
        self.cells[row][col].is_selected = True
        self.selected_cell = (row, col)

    def click(self, pos):
        if pos[0] < self.width and pos[1] < self.height:
            distance_x = self.width / 9
            distance_y = self.height / 9
            x = pos[0] // distance_x
            y = pos[1] // distance_y
            return int(y), int(x)
        else:
            return None

    def clear_value(self):
        row, col = self.selected_cell
        if not self.cells[row][col].is_original:
            self.cells[row][col].is_wrong = False
            self.cells[row][col].value = 0

    def increase_value(self):
        row, col = self.selected_cell
        value = self.cells[row][col].value
        self.cells[row][col].is_wrong = False
        if value == 9 and self.cells[row][col].is_original is False:
            self.cells[row][col].value = 0
        elif self.cells[row][col].is_original is False:
            self.cells[row][col].value += 1
        self.update_model_values()

    def enter_value(self, val):
        row, col = self.selected_cell
        if not self.cells[row][col].is_original:
            self.cells[row][col].value = val
        self.update_model_values()

    def check_values(self):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = self.cells[i][j]
                if not cell.is_original and cell.value != 0:
                    cell.is_wrong = False
                    if not valid(self.board_model, cell.value, (cell.row, cell.col)):
                        cell.is_wrong = True
