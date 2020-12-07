def fieldValueCheck(name, val):
    if name == "byr":
        if len(val) != 4:
            return False
        val = int(val)
        if 1920 <= val <= 2002:
            return True
    elif name == "iyr":
        if len(val) != 4:
            return False
        val = int(val)
        if 2010 <= val <= 2020:
            return True
    elif name == "eyr":
        if len(val) != 4:
            return False
        val = int(val)
        if 2020 <= val <= 2030:
            return True
    elif name == "hgt":
        if val[-1] == "n":
            if len(val) != 4:
                return False
            val = val[0:2]
            val = int(val)
            if 59 <= val <= 76:
                return True
        elif val[-1] == "m":
            if len(val) != 5:
                return False
            val = val[0:3]
            val = int(val)
            if 150 <= val <= 193:
                return True
        else:
            return False
    elif name == "hcl":
        if len(val) != 7:
            return False
        if val[0] != "#":
            return False
        hclRank = 1
        while hclRank < len(val):
            hclMatches = ["a", "b", "c", "d", "e", "f", "0",
                          "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            characterAnalysis = val[hclRank]
            if characterAnalysis not in hclMatches:
                return False
            hclRank += 1
        return True
    elif name == "ecl":
        eclmatches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if val in eclmatches:
            return True
    elif name == "pid":
        if len(val) == 9:
            try:
                val = int(val)
                return True
            except:
                return False
    elif name == "cid":
        return True


def day04():
    with open("day 04\input.bat", "r") as f:
        goodPasseport = 0
        passportList = f.read().split("\n\n")
        i = 0
        while i < len(passportList):
            individualPassportFieldList = passportList[i].split()
            j = 0
            goodField = 0
            matches = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
            while j < len(individualPassportFieldList):
                field = individualPassportFieldList[j]
                fieldPart = field.split(":")
                fieldName = fieldPart[0]
                fieldValue = fieldPart[1]
                if fieldName in matches:
                    matches.remove(fieldName)
                    if fieldValueCheck(fieldName, fieldValue):
                        goodField += 1
                j += 1
            if goodField < 7:
                pass
            elif goodField == 7:
                if matches == ["cid"]:
                    goodPasseport += 1
                else:
                    pass
            elif goodField == 8:
                goodPasseport += 1
            i += 1
    print(goodPasseport)


day04()
