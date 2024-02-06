for t in range(int(input())):
    n = int(input())
    cnt = 0
    sum = 0
    if n%7 == 0:
        print(n)
    else:
        while cnt <= 1000:
            sum = n + int(str(n)[::-1])
            if sum%7 == 0:
                break
            n = sum
            cnt+=1
        if sum % 7 == 0:
            print(sum)
        else:
            print(-1)   
        
