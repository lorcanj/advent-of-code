from collections import OrderedDict

test = "testinput.txt"
input = "input.txt"

# build input
file = open(input)
line = file.read()

prep = []
gaps = []
gap_sizes = {}
file_sizes = {}
file_starts = {}
id = 0
file_start_counter = 0

for i in range(len(line)):
    # index is even
    if i & 1 == 0:
        file_starts[id] = file_start_counter
        file_sizes[id] = 0
        for j in range(int(line[i])):
            file_sizes[id] += 1
            prep.append(id)
            file_start_counter += 1
        id += 1
    else:
        # not a gap if of length 0
        if line[i] == '0':
            continue
        prep_length = len(prep)
        gap_sizes[prep_length] = 0
        for j in range(int(line[i])):
            gaps.append(prep_length + j)
            gap_sizes[prep_length] += 1
            prep.append('g')
            file_start_counter += 1

print(prep)
print(file_sizes)
#print(gaps)
print(gap_sizes)
print(file_starts)




# can stop when prep index is less than lowest gap index

# want to incrememnt backwards
# don't swap the first index
for i in range(prep[-1], 0, -1):
    # will loop in order where for iteration i, j where j > i
    # gap_index_j > gap_index_i
    dictionary_keys = sorted(gap_sizes.keys())
    # can break here if no gaps or smallest gap < size of the chunk we're looking for
    for j in range(len(dictionary_keys)):
        gap_index = dictionary_keys[j]
        # means would be swapping for gaps on the RHS
        if gap_index > file_starts[i]:
            break
        if file_sizes[i] <= gap_sizes[gap_index]:
            for k in range(file_sizes[i]):
                prep[gap_index + k] = i
                prep[file_starts[i] + k] = 'g'
            # need to update the gap if we've swapped
            # if equal then have removed the gap
            if file_sizes[i] == gap_sizes[gap_index]:
                gap_sizes.pop(gap_index)
            else:
                gap_sizes[gap_index + file_sizes[i]] = gap_sizes[gap_index] - file_sizes[i]
                gap_sizes.pop(gap_index)
            break

ans = 0
for i in range(len(prep)):
    if prep[i] != 'g':
        ans += prep[i] * i
print(ans)
