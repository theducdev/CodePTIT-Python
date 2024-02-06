import re
def hop(s1, s2):
    s3 = set()
    s3.update(s1)
    s3.update(s2)
    return sorted(s3)

def giao(s1, s2):
    giao = set()
    for x in s1:
        if x in s2:
            giao.add(x)
    return sorted(giao)




s1 = set(re.split(r'\s+', input().lower()))
s2 = set(re.split(r'\s+', input().lower()))
print(*hop(s1, s2), sep=" ")
print(*giao(s1,s2), sep=" ")

