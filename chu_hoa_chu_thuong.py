s = input()
chuHoa = 0
chuThuong = 0
for i in range(0, len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        chuThuong+=1
    else:
        chuHoa+=1
if chuThuong >= chuHoa:
    print(s.lower())
else:
    print(s.upper())