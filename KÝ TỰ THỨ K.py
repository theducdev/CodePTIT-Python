f = []
f.append(1)
for i in range (1,28):
    f.append(int(f[i-1])*2+1)

def find(n, k):
    if k==(f[n]+1)/2: return n-1
    if k < (f[n]+1)/2: return find(n-1, k)
    if k > (f[n]+1)/2: return find(n-1, k-(f[n]+1)/2)

for _ in range(int(input())):
    n, k = [int(x) for x in input().split()]
    print(chr(find(n,k) + 66))

