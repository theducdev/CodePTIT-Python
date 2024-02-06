def thuanNghich(num):
    for i in range(0, int(len(num)/2)):
        if num[i] != num[len(num)-i-1] or int(num[i])%2!=0:
            return False
    return True;

for t in range(int(input())):
    n = int(input())
    for num in range(22, n, 2):
        if thuanNghich(str(num)) and len(str(num))%2==0:
            print(num, end = " ")
    print()




