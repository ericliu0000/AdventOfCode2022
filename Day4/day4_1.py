with open("input.txt") as n:
    lines = n.readlines()

    count = 0

    for line in lines:
        first, second = line.split(",")
        fs, fl = first.split("-")
        ss, sl = second.split("-")

        fs, fl, ss, sl = int(fs), int(fl), int(ss), int(sl)

        if (fs <= ss and fl >= sl) or (ss <= fs and sl >= fl):
            count += 1

    print(count)
