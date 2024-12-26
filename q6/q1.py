from typing import List

test = "test.txt"

input = "input.txt"

# build input
file = open(input)
board = []
visited = set()

# board is a List[str][str]
for line in file:
    board.append(line.strip())

# creates a set
directions = {0: "^", 1: ">", 2: "v", 3: "<"}
direction_to_index = {"^": 0, ">": 1, "v": 2, "<": 3}
row_movement = {"^", "v"}


# populates a dictionary
# is in order for each row and col list
def populate_helpers(board, directions: dict):
    start, row_walls, col_walls = (-1, -1), {}, {}
    # board now a 2d matrix
    # populate helper dictionary and start position
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '#':
                if row not in row_walls:
                    row_walls[row] = []
                row_walls[row].append(col)
                if col not in col_walls:
                    col_walls[col] = []
                col_walls[col].append(row)
            elif board[row][col] in directions.values():
                start = (row, col)
    assert start != (-1, -1)
    for value in row_walls.values():
        value.sort()
    for value in col_walls.values():
        value.sort()
    return start, row_walls, col_walls


# need to pass in the list
def getNextWallIndex(rowOrCol_Walls: list, direction: str, i: int, j: int, board) -> tuple:
    # need to work out which list to check

    # problem with the + - 1 error causing bad counting
    match direction:
        # subtracting or adding 1 to return the index of the valid space

        # below loop currently wrong
        # should be fine if pass in the right list
        case ">":
            for index in range(len(rowOrCol_Walls)):
                if rowOrCol_Walls[index] > j:
                    return i, rowOrCol_Walls[index] - 1
            return i, len(board[0])
        case "<":
            for index in range(len(rowOrCol_Walls) - 1, -1, -1):
                if rowOrCol_Walls[index] < j:
                    return i, rowOrCol_Walls[index] + 1
            return i, -1
        case "^":
            for index in range(len(rowOrCol_Walls) - 1, -1, -1):
                if rowOrCol_Walls[index] < i:
                    return rowOrCol_Walls[index] + 1, j
            return -1, j
        case "v":
            for index in range(len(rowOrCol_Walls) - 1, -1, -1):
                if rowOrCol_Walls[index] > i:
                    return rowOrCol_Walls[index] - 1, j
            return len(board), j


# checks to see if we are out of bounds or not
def in_bounds(i: int, j: int, board) -> bool:
    return -1 < i < len(board) and -1 < j < len(board[0])

# will always have either i == wall_i or j == wall_j
def calculate_distance(i: int, j: int, wall_i: int, wall_j: int):
    return abs(i - wall_i) + abs(j - wall_j)


start_direction, row_walls, col_walls = populate_helpers(board, directions)
visited.add((start_direction[0], start_direction[1]))


def add_and_check_visited(visited: set, point_from: tuple, point_to: tuple, board) -> int:
    number_already_visited = 0
    x1, y1 = point_from[0], point_from[1]
    x2, y2 = point_to[0], point_to[1]

    diff = 0
    # x cords are different
    # y cord are the same
    if x2 - x1 != 0:
        step = -1 if x2 - x1 > 0 else 1
        for i in range(x2, x1 + step, step):
            if (i, y1) in visited:
                number_already_visited += 1
            else:
                visited.add((i, y1))
    else:
        # x cords are the same
        # y cords are different
        step = -1 if y2 - y1 > 0 else 1
        for j in range(y2, y1 + step, step):
            if (x1, j) in visited:
                number_already_visited += 1
            else:
                visited.add((x1, j))
    # assert number_already_visited != 0
    return number_already_visited


print(col_walls)

ans = 2
direction = board[start_direction[0]][start_direction[1]]
# helper to let us turn right easily
direction_index = direction_to_index[direction]



while True:
    if direction in row_movement:
        next = getNextWallIndex(col_walls.get(start_direction[1], []), direction, start_direction[0],
                                start_direction[1], board)
    else:
        next = getNextWallIndex(row_walls.get(start_direction[0], []), direction, start_direction[0],
                                start_direction[1], board)

    ans += calculate_distance(start_direction[0], start_direction[1], next[0], next[1])

    # if out of bounds, correctly adjust the answer
    if not in_bounds(next[0], next[1], board):
        i = next[0]
        j = next[1]
        if i < 0:
            i += 1
        elif j < 0:
            j += 1
        elif i == len(board):
            i -= 1
        elif j == len(board):
            j -= 1
        ans -= add_and_check_visited(visited, (start_direction[0], start_direction[1]), (i, j), board)
        break

    ans -= add_and_check_visited(visited, (start_direction[0], start_direction[1]), (next[0], next[1]), board)
    # below lets us turn right
    direction_index = (direction_index + 1) % 4
    direction = directions[direction_index]
    start_direction = (next[0], next[1])
    print(ans)
# for v in visited:
#     print(v)
print(len(visited))
print(ans + len(row_walls) + 1)
