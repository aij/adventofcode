#!/usr/bin/env python3

import sys

big=0
cur=0

for l in sys.stdin.readlines():
    l = l.strip()
    if l:
        cur += int(l)
    else:
        big = max(big, cur)
        cur = 0

print(big)
