#!/usr/bin/env python3

import sys

def points(c):
    if c >= 'a' and c <= 'z':
        return ord(c) + 1 - ord('a')
    return ord(c) + 27 - ord('A')

sum = 0
sum2 = 0
num = 0
threes = set()
for l in sys.stdin.readlines():
    l = l.strip()
    size = len(l)//2
    a = l[:size]
    b = l[size:]
    A = set(a)
    B = set(b)
    i = A.intersection(B)
    print(f"A {A} B {B} i {i}")
    common = i.pop()
    assert not i
    sum += points(common)
    num += 1
    if num == 1:
        threes = set(l)
    else:
        threes = threes.intersection(set(l))
    if num == 3:
        num = 0
        badge = threes.pop()
        assert not threes
        sum2 += points(badge)

print(sum)
print(sum2)
