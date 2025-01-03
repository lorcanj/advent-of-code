import math
from functools import cache

test = "test.txt"
input = "input.txt"
test2 = "test2.txt.txt"

cached_stones = {}

cached_stone_blinks = {}

# no return value because can return more than a single thing
@cache
def update_stone(_stone: int) -> []:
    if _stone == 0:
        return [1]
    digits = math.floor(math.log(_stone, 10) + 1)
    if digits & 1 == 0:
        left_num = 0
        right_num = 0
        # can we do this without converting digits to a string?
        # loop from the right to the left of the number
        # add up the numbers
        # want 10 ^ i * that stone's digit
        half = digits // 2
        checker = 0
        while _stone != 0:
            rem = _stone % 10
            if checker < half:
                right_num += (10 ** checker) * rem
            else:
                left_num += (10 ** (checker - half)) * rem
            _stone -= rem
            _stone //= 10
            checker += 1
        return [left_num, right_num]
    else:
        return [_stone * 2024]


# build input
file = open(test2)

stones = [int(number) for number in file.readline().strip().split(" ")]

blinks = 2

# want to cache the function below


@cache
def calculate_stones(_stone: int, _blinks: int):
    if _blinks == 0:
        return 1
    # can be an array of 1 or 2 stones
    transformed_stones = update_stone(_stone)
    return sum(calculate_stones(num, _blinks - 1) for num in transformed_stones)


ans = 0
for stone in stones:
    ans += calculate_stones(stone, blinks)
    print(ans)

print(ans)
