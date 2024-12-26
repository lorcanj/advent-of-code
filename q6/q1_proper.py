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
    board.append(line.strip())

directions = {0: "^", 1: ">", 2: "v", 3: "<"}
direction_to_index = {"^": 0, ">": 1, "v": 2, "<": 3}


def is_wall(board_piece: str) -> bool:
    return board_piece == "#"


def populate_start_location(board, directions: dict) -> tuple:
    start, row_walls, col_walls = (-1, -1), {}, {}
    # board now a 2d matrix
    # populate helper dictionary and start position
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] in directions.values():
                return row, col


def in_bounds(i: int, j: int, board) -> bool:
    return -1 < i < len(board) and -1 < j < len(board[0])


start = populate_start_location(board, directions)
print(start)
direction = board[start[0]][start[1]]
def change_direction(direction, direction_to_index, directions) -> str:
    return directions[(direction_to_index[direction] + 1) % 4]


ans = 0
visited = set()

while in_bounds(start[0], start[1], board):
    i = start[0]
    j = start[1]
    if (i, j) not in visited:
        ans += 1
        visited.add((start[0], start[1]))
    match direction:
        case ">":
            if in_bounds(i, j+1, board) and is_wall(board[i][j+1]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            j += 1
        case "<":
            if in_bounds(i, j-1, board) and is_wall(board[i][j-1]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            j -= 1
        case "^":
            if in_bounds(i-1, j, board) and is_wall(board[i-1][j]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            i -= 1
        case "v":
            if in_bounds(i+1, j, board) and is_wall(board[i+1][j]):
                direction = change_direction(direction, direction_to_index, directions)
                continue
            i += 1
    start = (i, j)
print(ans)
print(len(visited))
