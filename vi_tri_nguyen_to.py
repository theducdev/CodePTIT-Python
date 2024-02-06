import math
def checkSnt(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for t in range(int(input())):
    text = input()
    check = 1
    for i in range(0, len(text)):
        if checkSnt(i) and not checkSnt(int(text[i])):
            check = 0
        elif not checkSnt(i) and checkSnt(int(text[i])):
            check = 0
    if check:
        print("YES")
    else:
        print("NO")