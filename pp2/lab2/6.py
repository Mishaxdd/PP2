n = int(input())
num = list(map(int, input().split()))
max_num = num[0]
pos = 1 
for i in range(n):
    if num[i] > max_num:
        max_num = num[i]
        pos = i + 1  
print(pos)
