import numpy as np
# build input
test = "test.txt"
input = "input.txt"


# creates a list of tuples, with button A, B and result
def create_button_data(path: str) -> list:
    file = open(path)

    buttons = []
    temp = []
    for line in file:
        if line.isspace():
            continue

        line = line.strip()

        split_parts = line.split(":")

        if split_parts[0] == 'Prize':
            further_split = split_parts[1].split("=")
            temp.append((further_split[1].split(',')[0], further_split[2]))
            buttons.append(temp)
            temp = []
            continue

        x_value = split_parts[1].split('+')[1].split(',')[0]
        y_value = split_parts[1].split('+')[2]
        temp.append((x_value, y_value))
    return buttons


buttons = create_button_data(input)
ans = 0

for trio in buttons:
    button_a = trio[0]
    button_b = trio[1]
    goal = trio[2]

    a = np.array([[int(button_a[0]), int(button_b[0])], [int(button_a[1]), int(button_b[1])]])
    b = np.array([int(goal[0]), int(goal[1])])
    linear_ans = np.linalg.solve(a, b)

    x_as_int = round(linear_ans[0])
    y_as_int = round(linear_ans[1])

    # problems with numpy
    delta = 0.000000001
    if np.isclose(linear_ans[0], x_as_int, delta) and np.isclose(linear_ans[1], y_as_int, delta):
        curr = (linear_ans[0] * 3) + linear_ans[1]

        ans += curr
    # if linear_ans[0] % 1 == 0 and linear_ans[1] % 1 == 0:
    #     #print(linear_ans)


print(int(ans))



