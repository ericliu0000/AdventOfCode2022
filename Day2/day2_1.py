with open("input.txt") as n:
    lines = n.readlines()

    score = 0
    for line in lines:
        opp, play = line.lower().split()
        # turn abc and xyz into 123
        opp = opp.replace("a", "1").replace("b", "2").replace("c", "3")
        play = play.replace("x", "1").replace("y", "2").replace("z", "3")
        # A is rock, B is paper, C is scissors
        # X is rock, Y is paper, Z is scissors

        score += int(play)
        if opp == play:
            score += 3
        elif opp == "1" and play == "3" or opp == "2" and play == "1" or opp == "3" and play == "2":
            score += 0
        else:
            score += 6

    print(score)
        