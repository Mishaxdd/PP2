from collections import Counter
n = int(input())
numb = [input().strip() for _ in range(n)]
count = Counter(numb)
print(sum(1 for v in count.values() if v == 3))
