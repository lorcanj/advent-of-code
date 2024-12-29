test = "test.txt"

input = "input.txt"

# build input
file = open(input)
# island is a n x n matrix
island = []
for line in file:
    island.append([int(c) for c in line.strip()])

starts = []

for i in range(len(island)):
    for j in range(len(island[i])):
        if island[i][j] == 0:
            starts.append((i, j))
#print(starts)


def in_bound(row, col, matrix) -> bool:
    return -1 < row < len(matrix) and -1 < col < len(matrix[row])


def valid_path(row, col, matrix, visited: set, found: set) -> (int, tuple):
    if not in_bound(row, col, matrix): return 0, found
    if (row, col) in visited: return 0, found
    if matrix[row][col] == 9 and (row, col) not in found:
        found.add((row, col))
        return 1, found
    visited.add((row, col))

    dirs = [-1, 0, 1, 0, -1]
    is_valid = 0
    for index in range(len(dirs) - 1):
        # below is wrong
        new_dir = (row + dirs[index], col + dirs[index + 1])
        if in_bound(new_dir[0], new_dir[1], matrix):
            if matrix[new_dir[0]][new_dir[1]] - matrix[row][col] == 1:
                things = valid_path(new_dir[0], new_dir[1], matrix, visited, found)
                is_valid += things[0]
                found = things[1]
    return is_valid, found


ans = 0
for start in starts:
    #print(f"{start[0]} and {start[1]}")
    thing = valid_path(start[0], start[1], island, set(), set())
    ans += thing[0]
    #print(thing)
print(ans)
