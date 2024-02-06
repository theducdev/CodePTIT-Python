import math
n, k = input().split()
cnt = 0
for x in range(10**(int(k)-1), 10**(int(k))):
    if math.gcd(int(n), int(x)) == 1:
        print(x, end = " ")
        cnt+=1
        if cnt==10: 
            print()
            cnt = 0

