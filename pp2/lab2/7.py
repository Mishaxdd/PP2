n = int(input())
num = list(map(int,input().split()))
max = num[0]
count = 1
for i in num:
    if i > max:
        count+=1
        max = i

print(count)