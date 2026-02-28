g = 0
def outer(commands):
    n = 0
    def inner():
        nonlocal n
        global g
        for cmd in commands:
            scope, val = cmd[0], int(cmd[1])
            if scope == "global": g += val
            elif scope == "nonlocal": n += val
    inner()
    return n

cmds = [input().split() for _ in range(int(input()))]
n_res = outer(cmds)
print(g, n_res)