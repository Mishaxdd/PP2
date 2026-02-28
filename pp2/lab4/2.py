def even(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
first = True
for ev in even(n):
    if not first:
        print(",", end="")
    print(ev, end="")
    first = False