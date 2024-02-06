def tachdoi(n):
    i = len(n)//2
    nuadau = n[:i]
    nuasau = n[i:len(n)]
    return str(int((nuadau)) + int((nuasau)))


num = input()
while(len(num) > 1):
    a = tachdoi(num)
    print(a)
    num = a


