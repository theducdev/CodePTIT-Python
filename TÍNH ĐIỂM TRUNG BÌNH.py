import math

n = int(input())
a = sorted(float(i) for i in input().split())
Min = a[0]
Max = a[len(a)-1]
while Min in a:
    a.remove(Min)
while Max in a:
    a.remove(Max)
sum=0
for x in a:
    sum+=x
print("{:.2f}".format(sum/len(a)))




