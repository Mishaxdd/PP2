import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
d1, d2 = math.hypot(x1, y1), math.hypot(x2, y2)
dx, dy = x2 - x1, y2 - y1
t = -(x1*dx + y1*dy) / (dx*dx + dy*dy)
cp_dist = math.hypot(x1+t*dx, y1+t*dy) if 0 <= t <= 1 else min(d1, d2)

if cp_dist >= r:
    print(f"{math.hypot(dx, dy):.10f}")
else:
    theta = math.acos(max(-1, min(1, (x1*x2 + y1*y2)/(d1*d2))))
    alpha = theta - math.acos(r/d1) - math.acos(r/d2)
    length = math.sqrt(d1**2 - r**2) + math.sqrt(d2**2 - r**2) + r*alpha
    print(f"{length:.10f}")