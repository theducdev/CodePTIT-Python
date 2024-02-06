def doicho(n):
    x = "-1"
    a = [int(i) for i in n]
    ds = [(a[len(a)-1], len(a)-1)]
    for i in range(len(a)-1, 0, -1):
        if a[i] >= a[i-1]:
            ds.append((int(a[i]),i))
        else:
            ds.append((int(a[i]),i))
            ds.sort(key=lambda x : (-x[0], x[1]))
            tmp = a[i-1]
            j = 0
            while ds[j][0] >= tmp: j+=1
            max_value = ds[j][0]
            max_index = ds[j][1]
            a[i-1] = max_value
            a[max_index] = tmp
            x = ''.join(map(str, a))
            break
    return x

for _ in range(int(input())):
    n = input()
    if doicho(n)[0] == '0': print("-1")
    else: print(doicho(n))


