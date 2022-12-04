def readFile():
    lines = []
    with open("day02.txt") as file:
        for line in file:
            line = line.strip()
            lines.append(line.split())
    return lines


def play(opp, sel):
    score = 0
    if sel == 'X':
        score += 1
        if opp == 'A':
            score += 3
        elif opp == 'B':
            score += 0
        elif opp == 'C':
            score += 6
    elif sel == 'Y':
        score += 2
        if opp == 'A':
            score += 6
        elif opp == 'B':
            score += 3
        elif opp == 'C':
            score += 0
    elif sel == 'Z':
        score += 3
        if opp == 'A':
            score += 0
        elif opp == 'B':
            score += 6
        elif opp == 'C':
            score += 3
    return score


def decrypt(opp, result):
    sel = ''
    if opp == 'A':
        if result == 'X':
            sel = 'Z'
        elif result == 'Y':
            sel = 'X'
        elif result == 'Z':
            sel = 'Y'
    elif opp == 'B':
        if result == 'X':
            sel = 'X'
        elif result == 'Y':
            sel = 'Y'
        elif result == 'Z':
            sel = 'Z'
    elif opp == 'C':
        if result == 'X':
            sel = 'Y'
        elif result == 'Y':
            sel = 'Z'
        elif result == 'Z':
            sel = 'X'
    return sel


def partOne():
    puzzle_input = readFile()
    total = 0
    for each_round in puzzle_input:
        total += play(each_round[0], each_round[1])
    return total


def partTwo():
    puzzle_input = readFile()
    total = 0
    for each_round in puzzle_input:
        move = decrypt(each_round[0], each_round[1])
        total += play(each_round[0], move)
    return total


def main():
    part1val = partOne()
    print(f"Part 1: {part1val}")
    part2val = partTwo()
    print(f"Part 1: {part2val}")


if __name__ == "__main__":
    main()
