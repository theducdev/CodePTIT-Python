import collections
for _ in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    st = collections.deque()
    used = [1]*n
    ans = []
    for i in range(n):
        if not len(st) or a[i] < a[i-1]:
            ans.append(used[i])
        else:
            while len(st) and a[i] >= a[st[-1]]:
                used[i]+=used[st[-1]]
                st.pop()
            ans.append(used[i])
        st.append(i)
    for x in ans:
        print(x, end=" ")
    print()



