from random import sample
from copy import deepcopy

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

base = 3
side = base * base
solution_list = []


def valid(bo, number, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == number and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == number and pos[0] != i:
            return False

    # Check box

    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x * 3, box_x * 3 + 3):
        for j in range(box_y * 3, box_y * 3 + 3):
            if bo[i][j] == number and (i, j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("----------------------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


def shuffle(s): return sample(s, len(s))


def pattern(r, c): return (base * (r % base) + r // base + c) % side


def generate_board(difficulty):
    global board
    global solution_list
    solution_list.clear()

    r_base = range(base)  # 3
    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
    nums = shuffle(range(1, base * base + 1))

    # produce board using randomized baseline pattern
    board = [[nums[pattern(r, c)] for c in cols] for r in rows]

    empties = 0
    squares = side * side  # 81
    if difficulty == "Easy":
        empties = 20
    elif difficulty == "Medium":
        empties = 30
    elif difficulty == "Hard":
        empties = 40
    elif difficulty == "Very Hard":
        empties = 50

    for p in sample(range(squares), empties):
        board[p // side][p % side] = 0

    solve()

    # print(solution_list)
    if len(solution_list) > 1:
        generate_board(difficulty)
    else:
        return board

    return board


def solve():
    global board
    global solution_list
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for n in range(1, 10):
                    if valid(board, n, (i, j)):
                        board[i][j] = n
                        solve()
                        board[i][j] = 0
                return
    solution = deepcopy(board)
    solution_list.append(solution)
    if len(solution_list) > 1:
        return solution_list


def valid_grid(grid):
    for i in range(len(grid.cells)):
        for j in range(len(grid.cells[0])):
            if valid(grid.cells, grid.cells[i][j].value, (i,j)):
                pass
            else:
                return False
    return True
