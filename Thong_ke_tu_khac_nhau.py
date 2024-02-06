import re
from collections import Counter
N = int(input())
all_words = []

for _ in range(N):
    line = input().lower()
    words = re.findall(r'\b\w+\b', line)
    all_words.extend(words)

word_counts = Counter(all_words)

sorted_words = sorted(word_counts.items(), key = lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word, end = " ")
    print(count)
