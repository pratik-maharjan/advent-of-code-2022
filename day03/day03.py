def readFile():
    lines = []
    with open("day03-input.txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line)
    return lines


def get_common(first_part, second_part, third_part=None):
    if third_part is None:
        in_both = ''
        for item in first_part:
            if item in second_part and item not in in_both:
                in_both += item
        return in_both
    else:
        in_three = ''
        for item in first_part:
            if item in second_part and item not in in_three:
                if item in third_part and item not in in_three:
                    in_three += item
        return in_three


def get_priority(common):
    ascii_value = ord(common)
    if ascii_value >= 97:
        priority = ascii_value - 96
    else:
        priority = ascii_value - 38
    return priority


def get_groups(sacks):
    groups = []
    for i in range(0, len(sacks), 3):
        group = [sacks[i], sacks[i + 1], sacks[i + 2]]
        groups.append(group)
    return groups


def partOne():
    rucksacks = readFile()
    priority_sum = 0
    for sack in rucksacks:
        first_compartment, second_compartment = sack[:len(sack) // 2], sack[len(sack) // 2:]
        common = get_common(first_compartment, second_compartment)
        priority_sum += get_priority(common)
    return priority_sum


def partTwo():
    rucksacks = readFile()
    elf_groups = get_groups(rucksacks)
    priority_sum = 0
    for group in elf_groups:
        common = get_common(group[0], group[1], group[2])
        priority_sum += get_priority(common)
    return priority_sum


def main():
    part1val = partOne()
    print(f"Part 1: {part1val}")
    part2val = partTwo()
    print(f"Part 2: {part2val}")


if __name__ == "__main__":
    main()
