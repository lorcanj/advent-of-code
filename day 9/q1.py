import heapq

test = "testinput.txt"

input = "input.txt"

# build input
file = open(input)
line = file.read()

prep = []
id = 0
gaps = []

for i in range(len(line)):
    # index is even
    if i & 1 == 0:
        for j in range(int(line[i])):
            prep.append(id)
        id += 1
    else:
        # not a gap if of length 0
        if line[i] == '0':
            continue
        prep_length = len(prep)
        for j in range(int(line[i])):
            gaps.append(prep_length + j)
            prep.append('g')

#print(prep)
#print(gaps)
heapq.heapify(gaps)
#gaps_sum = sum(gaps)
ans = []
#print(len(gaps))

gaps_index = 0
prep_index = len(prep) - 1
gap_swaps = 0
# gaps is a min heap, storing the indicies of the haps in our list
# gaps[0] stores the min index element which contains 'g' in prep
while gaps:
    if prep_index < 0 or prep_index < gaps[0]:
        break
    if prep[prep_index] != 'g':
        # pop min element
        min_g_index = heapq.heappop(gaps)
        prep[min_g_index], prep[prep_index] = prep[prep_index], prep[min_g_index]
        heapq.heappush(gaps, prep_index)
        gap_swaps += 1

    prep_index -= 1

counter = 0
answer = 0

while prep[counter] != 'g':
    answer += (prep[counter] * counter)
    counter += 1
print(answer)




