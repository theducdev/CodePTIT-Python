import re
from collections import Counter
N, k = [int(i) for i in input().split()]
all_words = []
for _ in range(N):
    line = input().lower()
    words = re.findall(r'\b\w+\b', line)
    all_words.extend(words)
words_counts = Counter(all_words)
sorted_words = sorted(words_counts.items(), key=lambda x:(-x[1], x[0]))
for word, count in sorted_words:
    if count>=k:
        print(word, end = " ")
        print(count)

