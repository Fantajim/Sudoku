import pygame
from grid import Grid
import time
import pygame_gui

window_size = (900, 900)
game_size = window_size[0], window_size[1]-100
grid_size = 9
window = pygame.display.set_mode(window_size)
pygame.font.init()


def redraw_window(win, grid, t):
    win.fill((255, 255, 255))  # make window white
    font = pygame.font.SysFont("comicsans", 40)
    text = font.render("Time " + format_time(t), 1, (0, 0, 0))
    win.blit(text, (window_size[0] - (text.get_width()+20), window_size[1]-(text.get_height()/2+50)))
    grid.draw_grid(win)


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    return f"{minute}:{sec}"


def main():
    pygame.display.set_caption("Sudoku")
    grid = Grid(grid_size, grid_size, game_size[0], game_size[1], window)
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
                    grid.clear_value()
                    key = None
                if event.key == pygame.K_SPACE:
                    pass
                if event.key == pygame.K_RETURN:
                    if grid.check_values():
                        print("Success")
                    key = None

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_click = grid.click(mouse_pos)
                if mouse_click:
                    grid.select_cell(mouse_click[0], mouse_click[1])
                    key = None

        if grid.selected_cell and key is not None:
            grid.enter_value(key)

        redraw_window(window, grid, play_time)
        pygame.display.update()


main()
pygame.quit()
