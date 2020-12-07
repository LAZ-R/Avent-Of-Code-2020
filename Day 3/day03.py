def day03Slope(rightSlope, downSlope):
    with open("day 3\input.txt", "r") as f:
        listOne = f.read().split()
        i = 0
        j = 0
        treeCount = 0
        while i < len(listOne):
            line = listOne[i]
            if j >= len(line):
                j -= (len(line))
            character = line[j]
            if character == ".":
                pass
            elif character == "#":
                treeCount += 1
            i += downSlope
            j += rightSlope
        print("Slope  R", rightSlope, "D", downSlope, "=", treeCount)
    return treeCount


def ansPartTwo():
    ans01 = day03Slope(1, 1)
    ans02 = day03Slope(3, 1)
    ans03 = day03Slope(5, 1)
    ans04 = day03Slope(7, 1)
    ans05 = day03Slope(1, 2)
    finalAns = (ans01*ans02*ans03*ans04*ans05)

    print("Final Answer :", finalAns)


ansPartTwo()
