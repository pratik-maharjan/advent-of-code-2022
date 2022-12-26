def readFile(stripped):
    lines = []
    with open("day05-input.txt") as file:
        if stripped:
            for line in file:
                line = line.strip()
                lines.append(line)
        else:
            for line in file:
                lines.append(line)
    return lines


def get_layout(input):
    modified_input = []
    for i in input:
        modified_input.append(i.replace("\n", ""))

    layout = []
    for i in modified_input:
        if i != '':
            layout.append(i)
        else:
            break
    return layout


def get_last_row(layout):
    last = layout[len(layout) - 1]
    return last


def reverse_list(listed):
    for arr in listed:
        arr.reverse()
    return listed


def get_total_stacks(last):
    return int(last[len(last) - 1])


def get_stack_layout(layout, columns, numbering):
    stacks = []
    for i in range(0, columns):
        temp = []
        stacks.append(temp)
    for crate in layout:
        for i in range(1, len(crate), 4):
            if crate[i] != ' ':
                position = int(numbering[i])
                stacks[position - 1].append(crate[i])
    stacks = reverse_list(stacks)
    return stacks


def get_instructions(input):
    start_index = 0
    for index in range(0, len(input)):
        if input[index] == '':
            start_index = index + 1
    guidelines = input[start_index:]
    return guidelines


def strip_instructions(input):
    result = []
    for line in input:
        line = line.split()
        result.append(line)
    for item in result:
        for i in ['move', 'from', 'to']:
            item.remove(i)
    return result


def crane_9000(num, start, end, arr):
    for i in range(0, num):
        item = arr[start-1].pop()
        arr[end-1].append(item)
    return arr


def crane_9001(num, start, end, arr):
    buffer = []
    for i in range(0, num):
        item = arr[start-1].pop()
        buffer.append(item)
    buffer.reverse()
    arr[end-1] = arr[end-1] + buffer
    return arr


def play(command, state, part):
    if part == 1:
        for c in command:
            crane_9000(int(c[0]), int(c[1]), int(c[2]), state)
    elif part == 2:
        for c in command:
            crane_9001(int(c[0]), int(c[1]), int(c[2]), state)
    else:
        return None
    return state


def get_result(state):
    res = ''
    for arr in state:
        res += arr[len(arr)-1]
    return res


def partOne():
    strip_input = readFile(True)
    raw_input = readFile(False)
    layout = get_layout(raw_input)
    last_row = get_last_row(layout)
    total_stacks = get_total_stacks(last_row)
    start_state = get_stack_layout(layout[:-1], total_stacks, last_row)
    print("Start: {}".format(start_state))

    instructions = get_instructions(strip_input)
    arr_instructions = strip_instructions(instructions)

    final_state = play(arr_instructions, start_state, 1)
    answer = get_result(final_state)
    print("Final: {}".format(final_state))
    return answer


def partTwo():
    strip_input = readFile(True)
    raw_input = readFile(False)
    layout = get_layout(raw_input)
    last_row = get_last_row(layout)
    total_stacks = get_total_stacks(last_row)
    start_state = get_stack_layout(layout[:-1], total_stacks, last_row)
    print("Start: {}".format(start_state))
    instructions = get_instructions(strip_input)
    arr_instructions = strip_instructions(instructions)

    final_state = play(arr_instructions, start_state, 2)
    answer = get_result(final_state)
    print("Final: {}".format(final_state))
    return answer


def main():
    part1val = partOne()
    print(f"Part 1: {part1val}")
    print()
    part2val = partTwo()
    print(f"Part 2: {part2val}")


if __name__ == "__main__":
    main()
