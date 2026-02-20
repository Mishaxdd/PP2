import sys

def solve():
    try:
        line1 = sys.stdin.readline()
        if not line1: return
        n = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2: return
        array = list(map(int, line2.split()))
        
        line3 = sys.stdin.readline()
        if not line3: return
        q = int(line3.strip())
    except ValueError:
        return
    for _ in range(q):
        op_line = sys.stdin.readline().strip().split()
        if not op_line: continue
        
        op_type = op_line[0]
        if op_type == "add":
            x = int(op_line[1])
            f = lambda a, val=x: a + val
        elif op_type == "multiply":
            x = int(op_line[1])
            f = lambda a, val=x: a * val
        elif op_type == "power":
            x = int(op_line[1])
            f = lambda a, val=x: a ** val
        elif op_type == "abs":
            f = lambda a: abs(a)
        else:
            continue
        array = [f(item) for item in array]
    print(*(array))

if __name__ == "__main__":
    solve()