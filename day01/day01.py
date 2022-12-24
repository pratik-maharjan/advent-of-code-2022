def readFile():
    lines = []
    with open("day01-input.txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


def get_calories(lines):
    elves = []
    current = 0
    for line in lines:
        if line != '':
            current = current + int(line)
        else:
            elves.append(current)
            current = 0
    elves.append(current)
    # print(f"Unsorted Elves:\n {elves}")
    elves.sort()
    # print(f"Sorted Elves:\n {elves}")
    return elves


def partOne():
    puzzle_input = readFile()
    calories = get_calories(puzzle_input)
    result = calories[-1]
    return result


def partTwo():
    puzzle_input = readFile()
    calories = get_calories(puzzle_input)
    result = sum(calories[-3:])
    return result


def main():
    part1val = partOne()
    print(f"Part 1: {part1val}")
    part2val = partTwo()
    print(f"Part 2: {part2val}")


if __name__ == "__main__":
    main()
