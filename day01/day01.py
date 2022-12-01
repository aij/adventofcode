#!/usr/bin/env python3

import sys

def groups():
    cur=0
    for l in sys.stdin.readlines():
        l = l.strip()
        if l:
            cur += int(l)
        else:
            yield cur
            cur = 0
    yield cur

all = list(groups())

print(f"Part 1: {max(all)}")

top3 = sorted(all)[-3:]
print(repr(top3))
print(f"Part two: Sum of top 3: {sum(top3)}")
