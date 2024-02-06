import math
for t in range(int(input())):
    text = input();
    n = len(text)
    dao_text = text[::-1]
    check = 1
    for i in range(1, len(text)):
        if abs(ord(text[i]) - ord(text[i-1])) != abs(ord(dao_text[i]) - ord(dao_text[i-1])):
            check = 0
            break
    if check:
        print("YES")
    else:
        print("NO")

        

    
