def prime_factors(n):
    factors = []
    i = 2
    while i*i<=n:
        if n % i:
            i+=1
        else:
            n//=i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


for t in range(int(input())):
    n = int(input())
    factors = []
    check = [0]*1000000
    i = 2
    while i*i<=n:
        if n % i:
            i+=1
        else:
            check[i]+=1
            n/=i
            factors.append(i)
    if n > 1:
        factors.append(int(n))
        check[int(n)]+=1
    cnt = 0
    print("1", end = "")

    for i in range(len(factors)):
        if check[factors[i]]>0:
            print(" * " + str(factors[i]) + "^" + str(check[factors[i]]), end = "" )
            check[factors[i]] = 0
    print()
            


