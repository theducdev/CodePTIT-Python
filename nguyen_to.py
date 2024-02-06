def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check_coprime(a, b):
    return gcd(a, b) == 1


t = int(input())
while t:
    n = int(input())
    k = 0
    check = 1
    for i in range(1, n):
        if check_coprime(i, n):
            k+=1
    for i in range(2,k):
        if k % i == 0:
            check = 0
    if k == 1 or k == 0:
        check = 0
    if check == 0:
        print("NO")
    else:
        print("YES")

    t-=1
