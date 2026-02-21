n = int(input())
arr = list(map(int, input().split()))
q = int(input())

for _ in range(q):
    command = input().split()
    op = command[0]
    
    if op == "abs":
        for i in range(n):
            arr[i] = abs(arr[i])
    elif op == "add":
        x = int(command[1])
        for i in range(n):
            arr[i] = arr[i] + x
    elif op == "multiply":
        x = int(command[1])
        for i in range(n):
            arr[i] = arr[i] * x
    elif op == "power":
        x = int(command[1])
        for i in range(n):
            arr[i] = arr[i] ** x

print(*(arr))