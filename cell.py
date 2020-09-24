import pygame

class Cell:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.temp = 0
        self.selected = None

    def draw(self, win):
        font = pygame.font.SysFont("comicsans", 40)
        gap = self.width / 9
        x = self.cols * gap
        y = self.rows * gap

        if self.temp != 0 and self.value == 0:
            text = font.render(str(self.temp), 1, (128, 128, 128))
            win.blt(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = font.render(str(self.value)), 1, (0, 0, 0)
            win.blit(text, x + gap / 2 - text.get_width() / 2, y + (gap / 2 - text.get_height() / 2))

    def draw_change(self, win, g=True):
        pass

    def set_temp(self, val):
        self.temp = val

    def set(self, val):
        self.value = val