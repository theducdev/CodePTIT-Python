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
    cnt=0
    for i in range(0, len(text)):
        if checkSnt(int(text[i])):
            cnt+=1
    if checkSnt(len(text)) and len(text) - cnt < cnt:
        print("YES")
    else:
        print("NO")