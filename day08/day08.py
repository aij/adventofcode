#!/usr/bin/env python3

import sys
import os
import re

with open(sys.argv[1]) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')

width = len(lines[0])
height = len(lines)

assert width == height

assert all(len(x) == width for x in lines)

grid = ''.join(lines)

visible = [False] * (width*height)

def line(start, step):
    h = -1
    for i in range(width):
        p = start + i * step
        n = grid[p]
        n = int(n)
        if n > h:
            visible[p] = True
            h = n

def scan(start, stepa, stepb):
    for i in range(height):
        p = start + i * stepa
        line(p, stepb)

scan(0, width, 1)
scan(0, 1, width)
end = width*height-1

scan(end, -width, -1)
scan(end, -1, -width)

c  = sum(1 for x in visible if x)

print(c)
