n = int(input())
used = [0]*100000
a = []
while (len(a) < n):
    for x in input().split():
        a.append(int(x))
        used[int(x)]+=1
check = 0
for i in range(1, max(a)+1):
    if used[i]==0:
        print(i)
        check = 1
if check==0:
    print("Excellent!")
