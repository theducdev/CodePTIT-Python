import math
def checkSnt(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for t in range(int(input())):
    num = input()
    ngto = 0
    for i in range (0, len(num)):
        if (checkSnt(int(num[i]))):
            ngto+=1
    if len(num) >=3 and checkSnt(len(num)) and ngto > len(num) - ngto:
        print("YES")
    else:
        print("NO")