def readFile(stripped):
    lines = []
    with open("day06-input.txt") as file:
        if stripped:
            for line in file:
                line = line.strip()
                lines.append(line)
        else:
            for line in file:
                lines.append(line)
    return lines


def get_packet_marker(input):
    packet = ''
    for i in range(0, len(input) - 4):
        packet = input[i:i + 4]
        verify = set(packet)
        if len(verify) == 4:
            marker = i + 4
            return marker
    return None


def get_message_marker(input):
    message = ''
    for i in range(0, len(input) - 14):
        message = input[i:i + 14]
        verify = set(message)
        if len(verify) == 14:
            marker = i + 14
            return marker
    return None


def partOne():
    strip_input = readFile(True)
    input = strip_input[0]
    result = get_packet_marker(input)
    return result


def partTwo():
    strip_input = readFile(True)
    input = strip_input[0]
    result = get_message_marker(input)
    return result


def main():
    part1val = partOne()
    print(f"Part 1: {part1val}")
    part2val = partTwo()
    print(f"Part 2: {part2val}")


if __name__ == "__main__":
    main()
