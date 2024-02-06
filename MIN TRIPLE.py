import heapq
for _ in range(int(input())):
    n = int(input())
    ans = 0
    a = [int(i) for i in input().split()]
    for x in heapq.nsmallest(3, a):
        ans += x
    print(ans)


