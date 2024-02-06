for t in range(int(input())):
    nums = int(input())
    num = str(nums)
    if num[len(num)-2]=='8' and num[len(num)-1]=='6':
        print("YES")
    else: 
        print("NO")
