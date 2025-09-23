
from datetime import datetime, timedelta
import time

def present_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def distance(d1, d2):
    a = datetime.fromisoformat(d1)
    b = datetime.fromisoformat(d2)
    return abs((b - a))

def make_format(d, fmt="%d-%m-%Y"):
    dt = datetime.fromisoformat(d)
    return dt.strftime(fmt)

def clock_sw(seconds=3):
    start = time.time()
    while time.time() - start < seconds:
        pass
    return round(time.time() - start, 2)

def tickdown(seconds=3):
    out = []
    for i in range(seconds, 0, -1):
        out.append(i)
        time.sleep(0)
    out.append("Go!")
    return out
