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

def H(p):
    return int(grid[p])

def pos(x,y):
    return x + y*height

def line_score(h, range):
    score = 0
    for p in range:
        score += 1
        n = H(p)
        if n > h:
            break
    return score

def scenic_score(x,y):
    h = H(pos(x,y))
    score = 1
    score *= line_score(h, (pos(x,i) for i in range(y+1, width)))
    score *= line_score(h, (pos(x,i) for i in range(y-1, -1, -1)))
    score *= line_score(h, (pos(i,y) for i in range(x+1, width)))
    score *= line_score(h, (pos(i,y) for i in range(x-1, -1, -1)))
    return score

m = max(scenic_score(x,y) for x in range(width) for y in range(width))
print(m)

# 5752800 is too high
# That's not the right answer; your answer is too high. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 5752800.)
