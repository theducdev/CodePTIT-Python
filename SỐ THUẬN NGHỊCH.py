
digits = ''.join(str(i) for i in range(100000))
def custom_base_repr(number, base=2, padding=0):

    num = abs(number)
    res = []
    while num:
        res.append(digits[num % base])
        num //= base
    if padding:
        res.append('0' * padding)
    if number < 0:
        res.append('-')
    return ''.join(reversed(res or '0'))



a,b,M = [int(i) for i in input().split()]
cnt = 0
for i in range(a, b+1):
    for j in range(2, M+1):
        n = custom_base_repr(i, j)
        if n==n[::-1]: cnt+=1
print(cnt)
