n = int(input())
num = list(map(int,input().split()))
b = sorted(num,reverse=True)
print(*b)