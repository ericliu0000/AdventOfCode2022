with open("input.txt") as n:
    states = {i: "" for i in range(1, 10)}
    for i in range(8):
        ln = n.readline()[1::4]
        print(ln)
        for i in range(len(ln)):
            letter = ln[i]
            if letter != " ":
                states[i + 1] += letter
    # clear out two lines i think
    n.readline()
    n.readline()

    for line in n.readlines():
        print(states)

        line = line[5:]
        count, rest = line.split(" from ")
        fro, to = rest.split(" to ")

        for i in range(int(count)):
            states[int(to)] = states[int(fro)][0] + states[int(to)]
            states[int(fro)] = states[int(fro)][1:]

    for k, v in states.items():
        print(states[k][0], end="")

    print(states)