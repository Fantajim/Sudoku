import pygame


class Cell:
    rows = 9
    cols = 9

    def __init__(self, row, col, value, width, height):
        self.col = col
        self.row = row
        self.value = value
        self.width = width
        self.height = height
        self.is_selected = False
        self.is_wrong = False

        if self.value != 0:
            self.is_original = True
        else:
            self.is_original = False

    def draw_cell(self, win):
        font = pygame.font.SysFont("couriersans", 40)
        distance_x = self.width / 9
        distance_y = self.height / 9
        x = distance_x * self.col
        y = distance_y * self.row

        if not self.is_original and self.value != 0:
            text = font.render(str(self.value), 1, (128, 128, 128))
            win.blit(text, (x + (distance_x / 2 - text.get_width() / 2), y + (distance_y / 2 - text.get_height() / 2)))
        elif not self.value == 0:
            text = font.render(str(self.value), 1, (0, 0, 0))
            win.blit(text, (x + (distance_x / 2 - text.get_width() / 2), y + (distance_y / 2 - text.get_height() / 2)))

        if self.is_wrong:
            pygame.draw.rect(win, (255, 0, 0), (x, y + 1, distance_x, distance_y), 4)
        elif self.is_selected:
            pygame.draw.rect(win, (0, 0, 255), (x, y + 1, distance_x, distance_y), 4)


