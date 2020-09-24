import pygame

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

    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win
        self.model = None
        self.update_model()
        self.selected = None
        self.cells = []

    def update_model(self):
        pass

    def place(self, val):
        pass

    def sketch(self, val):
        pass

    def draw(self):
       pass


    def select(self):
        pass

    def clear(self):
        pass

    def click(self, pos):
        pass

    def is_finished(self):
        pass

    def solve(self):
        pass

    def solve_gui(self):
        pass