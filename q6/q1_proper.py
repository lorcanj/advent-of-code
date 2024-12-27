import copy
from typing import List

test = "test.txt"

input = "input.txt"

# build input
file = open(input)
board = []
visited = set()
walls = set()

# board is a List[str][str]
for line in file:
    _line = line.strip()
    arr = []
    for l in _line:
        arr.append(l)
    board.append(arr)
#print(board)
directions = {0: "^", 1: ">", 2: "v", 3: "<"}
direction_to_index = {"^": 0, ">": 1, "v": 2, "<": 3}

board_copy = copy.deepcopy(board)


def is_wall(board_piece: str) -> bool:
    return board_piece == "#"


def populate_start_location(board, directions: dict) -> tuple:
    start: tuple = -1, -1
    walls: set = set()
    # board now a 2d matrix
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] in directions.values():
                start = row, col
            elif is_wall(board[row][col]):
                walls.add((row, col))
    return start, walls


def in_bounds(i: int, j: int, board) -> bool:
    return -1 < i < len(board) and -1 < j < len(board[0])


def change_direction(direction, direction_to_index, directions) -> str:
    return directions[(direction_to_index[direction] + 1) % 4]

start, walls = populate_start_location(board, directions)

direction = board[start[0]][start[1]]

initial_direction = direction

# want to save the start location as cannot place a wall there
initial_start: tuple = start
initial_path = set()

# this gives us the path which we then alter the board to count the number of things
while in_bounds(start[0], start[1], board):
    i = start[0]
    j = start[1]
    if (i, j) not in initial_path:
        initial_path.add((start[0], start[1], direction))
    match direction:
        case ">":
            if in_bounds(i, j + 1, board) and is_wall(board[i][j + 1]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            j += 1
        case "<":
            if in_bounds(i, j - 1, board) and is_wall(board[i][j - 1]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            j -= 1
        case "^":
            if in_bounds(i - 1, j, board) and is_wall(board[i - 1][j]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            i -= 1
        case "v":
            if in_bounds(i + 1, j, board) and is_wall(board[i + 1][j]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            i += 1
    start = (i, j)

# return true if we can't place the wall 
def cant_place_wall(row: int, col: int, board, walls: set, start_position: tuple) -> bool:
    return (not in_bounds(row, col, board)) or is_wall(board[row][col]) or (row == start_position[0] and col == start_position[1])

def updated_index(row, col, direction):
    match direction:
        case ">":
            col += 1
        case "<":
            col -= 1
        case "^":
            row -= 1
        case "v":
            row += 1
    return row, col


# want to loop through the path and add the wall
def add_wall(row: int, col: int, board, direction) -> tuple:
    match direction:
        case ">":
            col += 1
        case "<":
            col -= 1
        case "^":
            row -= 1
        case "v":
            row += 1
    board[row][col] = "#"
    return row, col

def undo_add_wall(row, col, board):
    board[row][col] = "."

def is_looping(start_row, start_col, board, direction) -> bool:
    i = start_row
    j = start_col
    _dir = direction
    visited = set()

    while in_bounds(i, j, board):
        if (i, j, _dir) in visited:
            return True
        visited.add((i, j, _dir))
        match _dir:
            case ">":
                if in_bounds(i, j + 1, board) and is_wall(board[i][j + 1]):
                    _dir = change_direction(_dir, direction_to_index, directions)
                    continue
                j += 1
            case "<":
                if in_bounds(i, j - 1, board) and is_wall(board[i][j - 1]):
                    _dir = change_direction(_dir, direction_to_index, directions)
                    continue
                j -= 1
            case "^":
                if in_bounds(i - 1, j, board) and is_wall(board[i - 1][j]):
                    _dir = change_direction(_dir, direction_to_index, directions)
                    continue
                i -= 1
            case "v":
                if in_bounds(i + 1, j, board) and is_wall(board[i + 1][j]):
                    _dir = change_direction(_dir, direction_to_index, directions)
                    continue
                i += 1

    return False

def check_same(board, original):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != original[i][j]:
                return False
    return True

def print_matrix(board):
    for b in board:
        for c in b:
            print(c, end="")
        print()


ans = set()
counter = 0
for point in initial_path:
    i = point[0]
    j = point[1]
    _dir = point[2]
    update = updated_index(i, j, _dir)
    # if can't place wall then skip and check the next point
    if cant_place_wall(update[0], update[1], board, set(), (initial_start[0], initial_start[1])):
        continue

    # else
    #print_matrix(board)
    changed_points = add_wall(i, j, board, _dir)
    #print("**********************")
    #print_matrix(board)

    # want to traverse here
    # but starting from just before hitting the wall
    if is_looping(initial_start[0], initial_start[1], board, initial_direction):
        # print("******************")
        # print("Wall added below:")
        # print(update[0])
        # print(update[1])
        # print("******************")
        ans.add((update[0], update[1]))
    # undo the change
    undo_add_wall(changed_points[0], changed_points[1], board)
    # print("************************")
    # print(print_matrix(board))
    #print(counter)
    #counter += 1
    assert(check_same(board, board_copy) is True)


# print(ans)
#print(counter)
print(len(ans))


