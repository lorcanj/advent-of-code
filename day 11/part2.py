import math

test = "test.txt"
input = "input.txt"
test2 = "test2.txt"


# no return value because can return more than a single thing
def update_stone(_stone: int, arr: []) -> None:
    if _stone == 0:
        arr.append(1)
        return
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
        arr.append(left_num)
        arr.append(right_num)
    else:
        arr.append(_stone * 2024)


# build input
file = open(input)

stones = [int(number) for number in file.readline().strip().split(" ")]

blinks = 25

for i in range(blinks):
    new_output = []
    for stone in stones:
        update_stone(stone, new_output)
    stones = new_output
    #print(stones)

print(len(stones))