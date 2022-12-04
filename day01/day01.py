lines = []
part1val = 0
with open("day01-input.txt") as file:
    for line in file:
        line = line.strip()
        lines.append(line)

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
part1val = elves[-1]
print(f"Part 1: {part1val}")

part2val = sum(elves[-3:])
print(f"Part 2: {part2val}")
