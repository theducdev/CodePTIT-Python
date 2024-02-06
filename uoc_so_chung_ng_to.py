import math
def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0):
            return False
    return True

def sum(n):
    a = str(n)
    ans = 0
    for i in range (len(a)):
        ans += int(a[i])
    return ans


for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    if isPrime(sum(math.gcd(a,b))):
        print("YES")
    else:
        print("NO")
