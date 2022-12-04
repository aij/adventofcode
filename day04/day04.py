#!/usr/bin/env python3

import sys

# True if a contains b
def contains(a, b):
    return a[0] <= b[0] and a[1] >= b[1]

# A fully before b
def before(a,b):
    return a[1] < b[0]


def overlaps(a,b):
    return not(before(a,b) or before(b,a))

count = 0
count2 = 0

for l in sys.stdin.readlines():
    l = l.strip()
    pairs = l.split(',')
    a,b = (x.split('-') for x in pairs)
    a = [int(x) for x in a]
    b = [int(x) for x in b]
    if (contains(a,b)) or contains(b,a):
        count += 1
    if overlaps(a,b):
        count2 +=1


print(count)
print(count2)
