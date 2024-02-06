num = input()
revnum = ""
for i in range (len(num)):
    revnum = num[i] + revnum
ans = ""
for i in range (len(num)):
    ans+=revnum[i]
    if (i+1)%3==0 and i+1!=len(num):
        ans+=","
tmp = ""
for i in range (len(ans)):
    tmp = ans[i] + tmp
print(tmp)
