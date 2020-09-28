import pygame
from grid import Grid
import time
import pygame_gui
from utility import find_empty, generate_board

window_size = (900, 900)
game_size = window_size[0], window_size[1] - 100
grid_size = 9
window = pygame.display.set_mode(window_size)
pygame.font.init()

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


def redraw_window(win, grid, t):
    win.fill((255, 255, 255))  # make window white
    font = pygame.font.Font("data/FiraCode-Regular.ttf", 40)
    text = font.render("Time " + format_time(t), 1, (0, 0, 0))
    win.blit(text, (window_size[0] - (text.get_width() + 20), window_size[1] - (text.get_height() / 2 + 50)))
    grid.draw_grid(win)


def format_time(secs):
    sec = secs % 60
    minute = secs // 60
    hour = minute // 60

    return f"{minute}:{sec}"


def main():
    pygame.display.set_caption("Sudoku")
    grid = Grid(grid_size, grid_size, game_size[0], game_size[1], board, window)
    key = None
    running = True
    start = time.time()
    # pygame GUI
    gui_manager = pygame_gui.UIManager(window_size, 'theme.json')
    clock = pygame.time.Clock()

    btn_auto_solve = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, window_size[1] - 75), (100, 50)),
                                                  text="Autosolve", manager=gui_manager)
    btn_generate = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((150, window_size[1] - 75), (120, 50)),
                                             text="Generate new", manager=gui_manager)

    while running:
        time_delta = clock.tick(60) / 1000
        play_time = round((time.time() - start))
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

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == btn_auto_solve:
                        grid.delay = 100.0
                        if not grid.solve_gui():
                            grid.clear_values()
                            grid.solve_gui()

                    if event.ui_element == btn_generate:
                        grid = Grid(grid_size, grid_size, game_size[0], game_size[1], generate_board(), window)
                        continue

            gui_manager.process_events(event)
        gui_manager.update(time_delta)

        if grid.selected_cell and key is not None:
            grid.enter_value(key)

        redraw_window(window, grid, play_time)
        gui_manager.draw_ui(window)
        pygame.display.update()


main()
pygame.quit()
