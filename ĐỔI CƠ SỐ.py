
def chuyen(n):
    if n >= 0 and n<=9: return n
    else :
        return chr(n+55)

t = int(input())
for _ in range(t):
    n, b = [int(x) for x in input().split()]
    ans = ""
    while True:
        if n==0: break
        ans+=str(chuyen(n%b))
        n=n//b
    print(ans[::-1])

