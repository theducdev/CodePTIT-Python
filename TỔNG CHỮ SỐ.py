n = input()
cnt = 0
while True:
    if int(n) >=0 and int(n) <=9: break
    cnt+=1
    sum = 0
    for x in n:
        sum+=ord(x)-48
    n = str(sum)

print(cnt)
