import math
n = int(input())
a = []
max_num = 0
check = 1
while len(a) < n:
    input_str = input()
    numbers = input_str.split()
    for x in numbers:
        a.append(int(x))
        max_num = max(int(x), max_num)
for i in range(1, max_num):
    if i not in a:
        print(i)
        check = 0
if check:
    print("Excellent!")


