def passwordCheck01(min, max,  letter, pswrd):
    iteration = 0
    a = 0
    while a < len(pswrd):
        if pswrd[a] == letter:
            iteration += 1
        a += 1
    if iteration in range(min, max+1):
        return True


def day02part01():
    with open("day 2\input.txt", "r") as f:
        lineTotal = len(f.read().split("\n"))
    with open("day 2\input.txt", "r") as f:
        okPassword = 0
        lineNmbr = 0
        while lineNmbr < lineTotal:
            line = (f.readline().split())
            iterRange = line[0].split("-")
            iterMin = int(iterRange[0])
            iterMax = int(iterRange[1])
            letterToSearch = line[1].split(":")[0]
            password = line[2]
            if passwordCheck01(iterMin, iterMax, letterToSearch, password):
                okPassword += 1
            lineNmbr += 1
        print(okPassword)


def passwordCheck02(min, max,  letter, pswrd):
    iteration = 0
    a = 0
    while a < len(pswrd):
        if pswrd[a] == letter:
            if a+1 == min or a+1 == max:
                iteration += 1
        a += 1
    if iteration == 1:
        return True


def day02part02():
    with open("day 2\input.txt", "r") as f:
        lineTotal = len(f.read().split("\n"))
    with open("day 2\input.txt", "r") as f:
        okPassword = 0
        lineNmbr = 0
        while lineNmbr < lineTotal:
            line = (f.readline().split())
            iterRange = line[0].split("-")
            iterMin = int(iterRange[0])
            iterMax = int(iterRange[1])
            letterToSearch = line[1].split(":")[0]
            password = line[2]
            if passwordCheck02(iterMin, iterMax, letterToSearch, password):
                okPassword += 1
            lineNmbr += 1
        print(okPassword)


day02part01()
day02part02()
