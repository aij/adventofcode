#!/usr/bin/env python3

import sys

# True if a contains b
def contains(a, b):
    return a[0] <= b[0] and a[1] >= b[1]

count = 0

for l in sys.stdin.readlines():
    l = l.strip()
    pairs = l.split(',')
    a,b = (x.split('-') for x in pairs)
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    if (contains(a,b)) or contains(b,a):
        count += 1

print(count)
