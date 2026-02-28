import sys
from datetime import datetime, timedelta, timezone

def get_dt(n):
    date_p, time_p, tz_p = n.strip().split()
    y, m, d = map(int, date_p.split('-'))
    hh, mm, ss = map(int, time_p.split(':'))
    sign = 1 if tz_p[3] == '+' else -1
    tz_h, tz_m = map(int, tz_p[4:].split(':'))
    tz = timezone(sign * timedelta(hours=tz_h, minutes=tz_m))
    return datetime(y, m, d, hh, mm, ss, tzinfo=tz).astimezone(timezone.utc)

t1 = get_dt(sys.stdin.readline())
t2 = get_dt(sys.stdin.readline())
print(int(abs((t2 - t1).total_seconds())))