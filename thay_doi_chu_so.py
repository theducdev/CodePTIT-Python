def chuyenMin(a, b, num):
    x = min(a, b)
    numchange = ""
    for i in range(len(num)):
        if num[i] == str(a) or num[i] == str(b):
            numchange += str(x)
        else:
            numchange += num[i]
    if numchange == "":
        return int(num)
    else:
        return int(numchange)


def chuyenMax(a, b, num):
    x = max(a, b)
    numchange = ""
    for i in range(len(num)):
        if num[i] == str(a) or num[i] == str(b):
            numchange += str(x)
        else:
            numchange += num[i]
    if numchange == "":
        return int(num)
    else:
        return int(numchange)


for _ in range(int(input())):
    a, b = [int(i) for i in input().split()]
    num1 = input()
    num2 = input()
    print(chuyenMin(a, b, num1) + chuyenMin(a, b, num2), chuyenMax(a, b, num1) + chuyenMax(a, b, num2))
