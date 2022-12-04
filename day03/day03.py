def readFile():
    lines = []
    with open("day03-input.txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


def get_common(first_part, second_part):
    in_both = ''
    for item in first_part:
        if item in second_part and item not in in_both:
            in_both += item
    return in_both


def get_priority(common):
    ascii_value = ord(common)
    if ascii_value >= 97:
        priority = ascii_value - 96
    else:
        priority = ascii_value - 38
    return priority


def partOne():
    rucksacks = readFile()
    priority_sum = 0
    for sack in rucksacks:
        first_compartment, second_compartment = sack[:len(sack) // 2], sack[len(sack) // 2:]
        common = get_common(first_compartment, second_compartment)
        priority_sum += get_priority(common)
    return priority_sum


def partTwo():
    pass


def main():
    part1val = partOne()
    print(f"Part 1: {part1val}")
    # part2val = partTwo()
    # print(f"Part 1: {part2val}")


if __name__ == "__main__":
    main()
