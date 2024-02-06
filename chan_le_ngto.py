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
    sum=0
    for i in range(0, len(text)):
        if i%2==0 and int(text[i])%2!=0:
            check = 0
        elif i%2!=0 and int(text[i])%2==0:
            check = 0
        sum+=int(text[i])
    if checkSnt(sum) and check:
        print("YES")
    else:
        print("NO")