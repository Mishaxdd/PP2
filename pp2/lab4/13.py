import json, re, sys

data = json.loads(input())
n = int(input())
for _ in range(n):
    q = input().strip()
    tokens = re.findall(r'[^\.\[\]]+|\[\d+\]', q)
    cur = data
    found = True
    for t in tokens:
        if t.startswith('['):
            idx = int(t[1:-1])
            if isinstance(cur, list) and idx < len(cur):
                cur = cur[idx]
            else:
                found = False
                break
        else:
            if isinstance(cur, dict) and t in cur:
                cur = cur[t]
            else:
                found = False
                break
    print(json.dumps(cur, separators=(',',':')) if found else "NOT_FOUND")