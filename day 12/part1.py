from typing import List

test = "test.txt"
test2 = "test2.txt"
test3 = "test3.txt"
input = "input.txt"


# area is just the number of letters in the island
# perimeter is more complex
# could do 4 * area - number of connections for each island part
# passing the set by reference so should be updating the visited set and not need to return it
def dfs_islands(_row: int, _col: int, island: List[List[str]], visited_islands: set, island_letter: str):
    # can do this check here or before to prevent some bfs_island calls
    # if not in_bounds(_row, _col, island): return
    if island[_row][_col] != island_letter: return
    if (_row, _col) in visited_islands: return

    visited_islands.add((_row, _col))
    # allows us to move +1 in a cardinal direction
    dirs = [-1, 0, 1, 0, -1]
    is_valid = 0
    for index in range(len(dirs) - 1):
        new_row, new_col = _row + dirs[index], _col + dirs[index + 1]
        if in_bounds(new_row, new_col, matrix) and (new_row, new_col) not in visited_islands:
            dfs_islands(new_row, new_col, island, visited_islands, island_letter)


def in_bounds(_row, _col, island):
    return -1 < _row < len(island) and -1 < _col < len(island[0])


# n ^ 2 algo to check all pairs where order matters too
def count_connections(set_of_points):
    to_remove = 0
    for point in set_of_points:
        for second_point in set_of_points:
            # should be ok because tuple is a value?
            if point != second_point and is_connected(point, second_point):
                to_remove += 1
    return 4 * len(set_of_points) - to_remove


# is connected when share a coord and other variable is of dist 1 away
def is_connected(point_a: tuple, point_b: tuple) -> bool:
    connected = point_a[0] == point_b[0] and abs(point_a[1] - point_b[1]) == 1
    return connected or point_a[1] == point_b[1] and abs(point_a[0] - point_b[0]) == 1


# build input
file = open(input)
# island is a n x n matrix
matrix = []
for line in file:
    matrix.append([c for c in line.strip()])

visited = set()
separate_islands = []
ans = 0

for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if (row, col) not in visited:
            # was wrong because assuming couldn't find new letter when going across the cols
            before_set = visited.copy()
            letter = matrix[row][col]
            dfs_islands(row, col, matrix, visited, letter)
            actual = visited - before_set
            separate_islands.append(list(actual))

            # part 1 calc
            # # area is number of segments
            # area = len(actual)
            #
            # # perimeter is more complicated
            # perimeter = count_connections(actual)
            # ans += (area * perimeter)


