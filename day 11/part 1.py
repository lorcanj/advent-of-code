import math

test = "test.txt"
input = "input.txt"
test2 = "test2.txt.txt"


# no return value because can return more than a single thing
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
        stone_value = _stone
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

# want stones to be a
stones = [(int(number), 0) for number in file.readline().strip().split(" ")]
#
stones.reverse()
# wrong
max_blinks = 6

ans = 0

print(ans)
