import math

test = "test.txt"
input = "input.txt"
test2 = "test2.txt"


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

_cache = {}
ans = 0
#
# while stones:
#     number, blinks = stones.pop()
#     original_number = number
#     current_stone_answer = 0
#     broken = False
#
#     for current_blink in range(blinks, max_blinks):
#         # below should mean we can hit max_blinks using the value in the cache
#         if (number, max_blinks - current_blink) in _cache.keys():
#             ans += _cache[(number, max_blinks - current_blink)]
#             broken = True
#             break
#
#         checked = update_stone(number)
#
#         # is i + 1 because we've done a blink on it so should be counted
#         if len(checked) == 2:
#             stones.append((checked[1], current_blink + 1))
#             current_stone_answer += 1
#
#         number = checked[0]
#         current_stone_answer += 1
#
#         # believe this is wrong
#         # but can also do some further caching
#         # want to cache every number in the chain, not sure how to do this
#         _cache[(number, current_blink + 1)] = current_stone_answer + len(checked)
#
#         # can do this for the original number as blinks are correct
#
#         #_cache[(original_number, current_blink + 1)] = current_stone_answer + len(checked)
#
#     if not broken:
#         ans += current_stone_answer

print(ans)
