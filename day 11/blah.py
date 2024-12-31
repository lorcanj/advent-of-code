import math

test = "test.txt"
input = "input.txt"
test2 = "test2.txt"

# Dictionaries to store the computed values for memoization
cached_stones = {}
cached_stone_blinks = {}


def update_stone(_stone: int) -> []:
    """Transform the stone according to the problem's rules and memoize the result."""
    if _stone == 0:
        return [1]

    if _stone in cached_stones:
        return cached_stones[_stone]

    else:
        digits = math.floor(math.log(_stone, 10) + 1)
        if digits % 2 == 0:  # Even number of digits
            left_num = 0
            right_num = 0
            half = digits // 2
            checker = 0
            # Loop to split the stone into left and right parts
            while _stone != 0:
                rem = _stone % 10
                if checker < half:
                    right_num += rem * (10 ** checker)
                else:
                    left_num += rem * (10 ** (checker - half))
                _stone //= 10
                checker += 1
            result = [left_num, right_num]
        else:  # Odd number of digits
            result = [_stone * 2024]

    cached_stones[_stone] = result
    return result


# Read input from the file
with open(input) as file:
    stones = [int(number) for number in file.readline().strip().split(" ")]

blinks = 75


def calculate_stones(_stone: int, _blinks: int):
    if _blinks == 0:
        return 1
    """Recursive function that calculates the number of transformations."""
    # Check if the result is already in the cache
    # means that we could have situation where if have stone 0 and 75 blinks remaining
    # already have the answer rather than doing all of the recursive calls again
    if (_stone, _blinks) in cached_stone_blinks:
        return cached_stone_blinks[(_stone, _blinks)]

    # Base case for recursion: If no more blinks, return 1 (final count)
    result = 0
    # Transform the stone using the update_stone function
    transformed_stones = update_stone(_stone)

    # Apply the transformation recursively for each new stone
    for transformed_stone in transformed_stones:
        result += calculate_stones(transformed_stone, _blinks - 1)

    # Store the result in the cache
    cached_stone_blinks[(_stone, _blinks)] = result
    return result


# Calculate the final answer by summing up the results for all stones
ans = 0
for stone in stones:
    ans += calculate_stones(stone, blinks)

# Output the result
print(f"Answer: {ans}")
