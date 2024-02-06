def sum(n):
    a = str(n)
    ans = 0
    for i in range (len(a)):
        ans += int(a[i])
    return ans

def check(n):
    a = str(n)
    for i in range (len(a)-1):
        if int(a[i]) - int(a[i+1]) != 2 and int(a[i]) - int(a[i+1]) != -2:
            return False
    return True


for t in range(int(input())):
    num = int(input())
    if check(num) and sum(num) % 10 == 0:
        print("YES")
    else:
        print("NO")

