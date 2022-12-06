def readFile():
    lines = []
    with open("day04-input.txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line.split(","))
    return lines


def get_pairs_list():
    elves = []
    lines = readFile()
    for line in lines:
        pairs = []
        for pair in line:
            pairs.append(pair.split("-"))
        elves.append(pairs)
    return elves


def get_pairs_set():
    elves = get_pairs_list()
    pairs = []
    for line in elves:
        sets = []
        for elf in line:
            one = int(elf[0])
            two = int(elf[1])
            pair = set(range(one, two+1))
            sets.append(pair)
        pairs.append(sets)
    return pairs


def partOne():
    assign = get_pairs_set()
    overlap = 0
    for item in assign:
        setOne = item[0]
        setTwo = item[1]
        if setOne.issubset(setTwo) or setTwo.issubset(setOne):
            overlap += 1
    return overlap


def partTwo():
    assign = get_pairs_set()
    total_intersect = 0
    for item in assign:
        setOne = item[0]
        setTwo = item[1]
        intersect = setOne.intersection(setTwo)
        if len(intersect) > 0:
            total_intersect += 1
    return total_intersect


def main():
    part1val = partOne()
    print(f"Part 1: {part1val}")
    part2val = partTwo()
    print(f"Part 2: {part2val}")


if __name__ == "__main__":
    main()
