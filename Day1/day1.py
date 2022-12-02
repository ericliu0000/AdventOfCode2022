elves = []
with open("input.txt") as n:
    elf = 0
    for line in n.readlines():
        if line == "\n":
            elves.append(elf)
            elf = 0
        else:
            elf += int(line)

# part 1
print(max(elves))

# part 2
elves.sort(reverse=True)
print(sum(elves[:3]))
