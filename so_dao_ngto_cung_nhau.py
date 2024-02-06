import math
for t in range(int(input())):
    a = input()
    b=""
    for i in range (len(a)):
        b = a[i] + b
    if math.gcd(int(a), int(b)) == 1:
        print("YES")
    else:
        print("NO")