from collections import Counter
n = int(input())
arr = list(map(int, input().split()))
freq = Counter(arr)
max_freq = max(freq.values())
most_frequent = min(k for k, v in freq.items() if v == max_freq)
print(most_frequent)
