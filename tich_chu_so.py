import math


for t in range(int(input())):
    text = input()
    sum=1
    for i in range(0, len(text)):
        if text[i] != '0':
             sum*=int(text[i])

    print(sum)