

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
        pass

    def draw_change(self, win, g=True):
        pass

    def set_temp(self, val):
        self.temp = val

    def set(self, val):
        self.value = val