def check(a, o, b, ans):
    if o == '+' and ans == a+b: return True
    if o == '-' and ans == a-b: return True
    if o == '*' and ans == a*b: return True
    if o == '/': return False
    return False

def gena(a):
    ans = []
    if a[0] =='?' and a[1] != '?':
        for i in range(1,10):
            ans.append(int(str(i) + a[1]))
    elif a[1] =='?' and a[0] != '?':
        for i in range(0,10):
            ans.append(int(a[0] + str(i)))
    elif a[0]=='?' and a[1] == '?':
        for i in range(10, 100):
            ans.append(int(i))
    else:
        ans.append(int(a))
    return ans

def geno(o):
    ans = ['+', '-', '*', '/']
    if o == '?':
        return ans
    else:
        return [o]
def solve(tmp):
    ok = 0
    a = gena(tmp[0])
    o = geno(tmp[1])
    b = gena(tmp[2])
    kq = gena(tmp[4])
    for x in a:
        for y in o:
            # if y=='/': continue
            for z in b:
                # if int(x)%int(z)!=0 and y =='/': continue
                for t in kq:
                    if check(x, y, z, t):
                        ok =1
                        print(x, y, z,"=", t)
                        return
    if ok == 0: print("WRONG PROBLEM!")


for _ in range(int(input())):
    tmp = input().split()
    solve(tmp)
    

