import sys
from datetime import datetime, timedelta, timezone

def parse_line(s):
    date_part, tz_part = s.strip().split()
    y, m, d = map(int, date_part.split("-"))
    sign = 1 if tz_part[3] == '+' else -1
    hh, mm = map(int, tz_part[4:].split(':'))
    tz = timezone(sign * timedelta(hours=hh, minutes=mm))
    return y, m, d, tz, datetime(y, m, d, tzinfo=tz).astimezone(timezone.utc)

def is_leap(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)

def bday_utc(bm, bd, birth_tz, year):
    if bm == 2 and bd == 29 and not is_leap(year): bd = 28
    return datetime(year, bm, bd, tzinfo=birth_tz).astimezone(timezone.utc)

lines = sys.stdin.readlines()
_, bm, bd, birth_tz, _ = parse_line(lines[0])
cy, _, _, _, curr_utc = parse_line(lines[1])

cand = bday_utc(bm, bd, birth_tz, cy)
if cand < curr_utc: cand = bday_utc(bm, bd, birth_tz, cy + 1)
delta = (cand - curr_utc).total_seconds()
print(int((delta + 86399) // 86400) if delta > 0 else 0)