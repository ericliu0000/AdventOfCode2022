import string

with open("input.txt") as n:
    lines = n.readlines()

    sum = 0
    for line in lines:
        same = ""
        first, second = line[:len(line) // 2], line[len(line) // 2:]

        for char in first:
            if char in second:
                same = char
        
        sum += string.ascii_letters.index(same) + 1

print(sum)
