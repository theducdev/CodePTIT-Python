import math
f = []
for i in range(0,10):
    f.append(math.factorial(i))

def check(n):
    sum=0
    for i in n:
        sum+=f[int(i)]
    if sum==int(n): return True
    return False

for _ in range(int(input())):
    n = input()
    if check(n): print("Yes")
    else: print("No")


