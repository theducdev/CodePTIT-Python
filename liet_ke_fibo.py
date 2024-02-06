for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    fibo = [0]*100
    fibo[1] = 1
    fibo[2] = 1
    for i in range(3, 93):
        fibo[i] = fibo[i-1] + fibo[i-2]
    for i in range(a, b+1):
        print(fibo[i], end=" ")
    print()
