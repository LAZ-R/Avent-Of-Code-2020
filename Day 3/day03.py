def day03SlopeR1D1():
    with open("day 3\input.txt", "r") as f:
        listOne=f.read().split()
        i=0
        j=0
        treeCountOne=0
        while i < len(listOne): 
            line=listOne[i]
            if j >= len(line):
                j-=(len(line))
            character=line[j]
            if character == ".":
                pass
            elif character == "#":
                treeCountOne+=1
            i+=1
            j+=1
        print("SlopeR1D1", treeCountOne)
    return treeCountOne
        
def day03SlopeR3D1():
    with open("day 3\input.txt", "r") as f:
        listOne=f.read().split()
        i=0
        j=0
        treeCountTwo=0
        while i < len(listOne): 
            line=listOne[i]
            if j >= len(line):
                j-=(len(line))
            character=line[j]
            if character == ".":
                pass
            elif character == "#":
                treeCountTwo+=1
            i+=1
            j+=3
        print("SlopeR3D1", treeCountTwo)
        return treeCountTwo

def day03SlopeR5D1():
    with open("day 3\input.txt", "r") as f:
        listOne=f.read().split()
        i=0
        j=0
        treeCountThree=0
        while i < len(listOne): 
            line=listOne[i]
            if j >= len(line):
                j-=(len(line))
            character=line[j]
            if character == ".":
                pass
            elif character == "#":
                treeCountThree+=1
            i+=1
            j+=5
        print("SlopeR5D1", treeCountThree)
        return treeCountThree

def day03SlopeR7D1():
    with open("day 3\input.txt", "r") as f:
        listOne=f.read().split()
        i=0
        j=0
        treeCountFour=0
        while i < len(listOne): 
            line=listOne[i]
            if j >= len(line):
                j-=(len(line))
            character=line[j]
            if character == ".":
                pass
            elif character == "#":
                treeCountFour+=1
            i+=1
            j+=7
        print("SlopeR7D1", treeCountFour)
        return treeCountFour

def day03SlopeR1D2():
    with open("day 3\input.txt", "r") as f:
        listOne=f.read().split()
        i=0
        j=0
        treeCountFive=0
        while i < len(listOne): 
            line=listOne[i]
            if j >= len(line):
                j-=(len(line))
            character=line[j]
            if character == ".":
                pass
            elif character == "#":
                treeCountFive+=1
            i+=2
            j+=1
        print("SlopeR1D2", treeCountFive)
        return treeCountFive

def ansPartTwo():
    ans01=day03SlopeR1D1()
    ans02=day03SlopeR3D1()
    ans03=day03SlopeR5D1()
    ans04=day03SlopeR7D1()
    ans05=day03SlopeR1D2()
    finalAns=(ans01*ans02*ans03*ans04*ans05)
    
    print("Final Answer :", finalAns)

ansPartTwo()
