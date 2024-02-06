import math

for t in range(int(input())):
    text = input()
    tichChan=1
    tongLe=0
    for i in range(0, len(text)):
        if i%2!=0:
            tongLe+=int(text[i])
        elif i%2==0 and text[i] != '0':
            tichChan*=int(text[i])


    print(tichChan, tongLe)