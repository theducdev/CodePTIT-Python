for t in range(int(input())):


    n = int(input())
    sum = 0
    st = 0
    if n%2==0:
        st = 2
    else:
        st = 1
    for i in range(st, n+1, 2):
        sum+=1/i
    print("{:.6f}".format(sum))