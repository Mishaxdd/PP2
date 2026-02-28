def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

n = int(input())
res = []
for f in fib(n):
    res.append(str(f))
print(",".join(res))