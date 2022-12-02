with open("input.txt") as n:
    lines = n.readlines()

    score = 0
    for line in lines:
        opp, play = line.lower().split()

        opp = opp.replace("a", "1").replace("b", "2").replace("c", "3")

        if play == "x":
            if opp == "1":
                score += 3
            elif opp == "2":
                score += 1
            else:
                score += 2
        elif play == "y":
            score += 3
            score += int(opp)
        else:
            score += 6
            if opp == "1":
                score += 2
            elif opp == "2":
                score += 3
            else:
                score += 1


    print(score)
        