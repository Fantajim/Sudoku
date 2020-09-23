import pygame
from grid import Grid
from cell import Cell
import time

window_size = (800, 600)
grid_size = 9
window = pygame.display.set_mode(window_size)
pygame.font.init()


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j  # row, col


def valid(bo, num, pos):
    # row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # box
    box_x = pos[1] / 3
    box_y = pos[0] / 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False

    return True


def redraw_window(win, board, t):
    win.fill((255, 255, 255))  # make window white
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render("Time " + format_time(t), 1, (0, 0, 0))
    window.blit(text, (window_size[0] - 100, window_size[1]))
    board.draw()


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    return f"{minute}:{sec}"


def main():
    pygame.display.set_caption("Sudoku")
    board = Grid(grid_size, grid_size, window_size[0], window_size[1], window)
    key = None
    running = True
    start = time.time()

    while running:
        play_time = round(time.time() - start)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                    key = 1
                if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                    key = 2
                if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                    key = 3
                if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                    key = 4
                if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                    key = 5
                if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                    key = 6
                if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                    key = 7
                if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                    key = 8
                if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    pass
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_RETURN:
                    pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

        if board.selected and key is not None:
            board.sketch(key)

        redraw_window(window, board, play_time)
        pygame.display.update()


main()
pygame.quit()
