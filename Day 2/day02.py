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
        while rankInStr<len(password):
            iteration=0
            individualCharacter=password[rankInStr]
            if  individualCharacter == searchedLetter:
                iteration+=1
            rankInStr+=1
        if low <= iteration <= high:
            print(low, high, searchedLetter, password, "OK")
            validPasswords+=1
        i+=3
    print("\n Number of valid passwords :", validPasswords)       