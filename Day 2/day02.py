def day02part01():
    with open(r"Day 2\input.txt", "r") as f:
        validPasswords=0
        fullList=(f.read().split())
        i=0
        while i < len(fullList):
            a = fullList[i].split("-")
            low = int(a[0]) # lowest iteration of the searched letter you have to have to get your password validated
            high = int(a[1]) # highest iteration of the searched letter you have to have to get your password validated
            b = fullList[i+1].split(":")
            searchedLetter = b[0] # searched letter
            password = fullList[i+2] # actual password
            rankInStr=0
            iteration=0
            while rankInStr<len(password):
                individualCharacter=password[rankInStr]
                if  individualCharacter == searchedLetter:
                    iteration+=1
                rankInStr+=1
            if low <= iteration <= high:
                validPasswords+=1
            i+=3
        print("\nNumber of valid passwords :", validPasswords)
     
def day02part02():
    with open(r"Day 2\input.txt", "r") as f:
        validPasswords=0
        fullList=(f.read().split())
        i=0
        while i < len(fullList):
            a = fullList[i].split("-")
            positionOne = int(a[0]) # lowest iteration of the searched letter you have to have to get your password validated
            positionTwo = int(a[1]) # highest iteration of the searched letter you have to have to get your password validated
            b = fullList[i+1].split(":")
            searchedLetter = b[0] # searched letter
            password = fullList[i+2] # actual password
            rankInStr=0
            iteration=0
            while rankInStr<len(password):
                individualCharacter=password[rankInStr]
                if  individualCharacter == searchedLetter:
                    if rankInStr == positionOne-1:                    
                        iteration+=1
                    if rankInStr == positionTwo-1:
                        iteration+=1
                rankInStr+=1
            if iteration == 1:
                validPasswords+=1
            i+=3
        print("\nNumber of valid passwords :", validPasswords)

print("\n\tDAY 02 - Part 01")
day02part01()
print("\n\tDAY 02 - Part 02")
day02part02()