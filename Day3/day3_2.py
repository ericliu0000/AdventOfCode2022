import string

with open("input.txt") as n:
    lines = n.readlines()

    sum = 0
    for i in range(0, len(lines), 3):
        l1, l2, l3 = lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip()
        same = ""

        for char in l1 + l2 + l3:
            if char in l1 and char in l2 and char in l3:
                same = char
        
        sum += string.ascii_letters.index(same) + 1

print(sum)

