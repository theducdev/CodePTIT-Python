import math
def thuanNghich(num):
    for i in range(0, int(len(num)/2)):
        if num[i] != num[len(num)-i-1] :
            return False
    return True


for t in range(int(input())):
    text = input()
    sum=0
    for i in range(0, len(text)):
        sum+=(int(text[i]))
            
    if thuanNghich(str(sum)) and sum >9:
        print("YES")
    else:
        print("NO")