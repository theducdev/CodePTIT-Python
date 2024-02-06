import re
from collections import Counter


def chuyen(a):
    ans = ""
    for i in range(len(a)):
        if a[i].isalpha():
            ans += a[i]
    return ans


N = int(input())
all_words = []
for _ in range(N):
    line = input().lower()
    a = re.findall(r'\b\w+\b', line)
    for x in a:
        if chuyen(x)!= "":
            all_words.append(chuyen(x))
word_count = Counter(all_words)
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
for word, count in sorted_words:
    print(word, count)
