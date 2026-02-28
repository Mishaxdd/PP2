import sys
from datetime import datetime, timedelta

def get_utc(n):
    parts = n.strip().split()
    date_part, tz_part = parts[0], parts[1]
    y, m, d = map(int, date_part.split('-'))
    sign = 1 if tz_part[3] == '+' else -1
    h, mins = map(int, tz_part[4:].split(':'))
    offset = sign * (h * 3600 + mins * 60)
    return datetime(y, m, d) - timedelta(seconds=offset)

t1 = get_utc(sys.stdin.readline())
t2 = get_utc(sys.stdin.readline())
print(int(abs((t1 - t2).total_seconds()) // 86400))