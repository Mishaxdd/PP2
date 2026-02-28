import math

r = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx, dy = x2 - x1, y2 - y1
a = dx**2 + dy**2
if a == 0:
    print(f"{r if math.hypot(x1, y1) <= r else 0.0:.10f}")
else:
    b = 2 * (dx * x1 + dy * y1)
    c = x1**2 + y1**2 - r**2
    discr = b**2 - 4 * a * c
    if discr <= 0:
        print("0.0000000000")
    else:
        sqrt_d = math.sqrt(discr)
        t1, t2 = (-b - sqrt_d) / (2 * a), (-b + sqrt_d) / (2 * a)
        t_start, t_end = max(0, min(t1, t2)), min(1, max(t1, t2))
        print(f"{math.hypot(dx, dy) * (t_end - t_start) if t_start < t_end else 0.0:.10f}")