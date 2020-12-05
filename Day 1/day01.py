with open(r"input.txt","r") as f:
    expenseReport=[int(x) for x in f]

def partie01():
    for i in range(len(expenseReport)):
        nmbrOne=expenseReport[i]
        for j in range(len(expenseReport)):
            nmbrTwo=expenseReport[j]     
            ans=nmbrOne+nmbrTwo
            if ans==2020:
                if i==j:
                    pass
                print(nmbrOne,"+",nmbrTwo,"= 2020")
                print("Correct answer is:",nmbrOne*nmbrTwo)
                return
            j+=1
        i+=1
def partie02():
    for i in range(len(expenseReport)):
        nmbrOne=expenseReport[i]
        for j in range(len(expenseReport)):
            nmbrTwo=expenseReport[j]  
            for k in range(len(expenseReport)): 
                nmbrThree=expenseReport[k]  
                ans=nmbrOne+nmbrTwo+nmbrThree
                if ans==2020:
                    if i==j:
                        pass
                    elif i==k:
                        pass
                    elif j==k:
                        pass
                    print(nmbrOne,"+",nmbrTwo,"+",nmbrThree,"= 2020")
                    print("Correct answer is:",nmbrOne*nmbrTwo*nmbrThree)
                    return
                k+=1
            k=0
            j+=1
        j=0
        i+=1
print("\nDAY 01 - Part 01\n")
partie01()
print("\nDAY 01 - Part 02\n")
partie02()