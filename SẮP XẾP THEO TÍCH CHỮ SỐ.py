def tichchuso(x):
    a = [int(i) for i in str(x)]
    sum = 1
    for x in a:
        sum*=x
    return sum


for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    my_dict = {}
    for x in a:
        my_dict[x] = tichchuso(x)
    ans = sorted(my_dict, key = lambda x : (my_dict[x], x))
    for x in ans:
        print(x, end=" ")
    print()
