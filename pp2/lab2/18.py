n = int(input())
arr = [input().strip() for _ in range(n)]
b = {}
for i, s in enumerate(arr, 1):
    if s not in b:
        b[s] = i
for s in sorted(b):
    print(s, b[s])
