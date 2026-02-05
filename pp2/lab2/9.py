n = int(input())
num = list(map(int,input().split()))
max = num[0]
min = num[0]
for i in num:
    if i > max:
        max = i

for j in num:
    if j < min:
        min = j

for i in range(n):
    if num[i] == max:
        num[i] = min


print(*num)
    
