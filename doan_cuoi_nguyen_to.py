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
    if checkSnt(int(text[-4:])):
        print("YES")
    else:
        print("NO")