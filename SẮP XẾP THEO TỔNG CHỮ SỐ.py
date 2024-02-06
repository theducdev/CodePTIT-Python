def tongchuso(x):
    a = [int(i) for i in str(x)]
    return sum(a)


for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    my_dict = {}
    for x in a:
        my_dict[x] = tongchuso(x)
    ans = sorted(my_dict, key = lambda x : (my_dict[x], x))
    for x in ans:
        print(x, end=" ")
    print()
