import math

for t in range(int(input())):
    text = input()
    check = 0
    tongChan=0
    tichLe=1
    for i in range(0, len(text)):
        if i%2==0:
            tongChan+=int(text[i])
        elif i%2!=0 and text[i] != '0':
            tichLe*=int(text[i])
        if i%2!=0 and text[i] != '0':
            check = 1


    print(tongChan, tichLe*check)