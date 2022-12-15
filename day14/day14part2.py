#!/usr/bin/env python3

import sys
import os
import re

def bound(i):
    if i == 0:
        return 0
    if i > 0:
        return 1
    if i < 0:
        return -1
    assert False

class vec2():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def bound(self):
        return vec2(bound(self.x), bound(self.y))

    def __add__(self, other):
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vec2(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return self.__str__()


def line(a,b):
    assert a.x == b.x or a.y == b.y
    dir = (b-a).bound()
    i = a
    yield i
    while i != b:
        i += dir
        yield i

filename = 'example'
filename = 'input'

lines = []
with open(filename) as f:
    for l in f:
        #print(l)
        points = [vec2(*(int(i) for i in p.split(','))) for p in l.rstrip().split(' -> ')]
        lines += [points[i:i+2] for i in range(len(points)-1)]

source = vec2(500,0)

leftmost = min(v.x for p in lines for v in p)
bottom = max(v.y for p in lines for v in p)
rightmost = max(v.x for p in lines for v in p)

lower_left = vec2(leftmost, bottom)

height = bottom + 2

#width = 1 + 2 * max(source.x - leftmost, rightmost - source.x)
width = 1 + height * 2

grid = [None] * width * height

left = 500 - width // 2

def at(v):
    x = v.x
    y = v.y
    return (x-left) + y * width

def print_grid():
    print('----------')
    for i,p in enumerate(grid):
        match p:
            case None: c = '.'
            case b: c = b
        print(c, end='')
        if i % width == width-1:
            print()

for (a,b) in lines:
    #print((a,b))
    for p in line(a,b):
        #print(f"Rock at {p} = {at(p)}, left={leftmost}, width={width}, height={height}, len={len(grid)}")
        grid[at(p)] = '#'


falldirs = [vec2(0,1), vec2(-1,1), vec2(1,1)]

units = 0

while True:
    s = source
    for y in range(height-1):
        for d in falldirs:
            c = s + d
            if not grid[at(c)]:
                s = c
                break
        else:
            grid[at(s)] = 'o'
            units += 1
            if y == 0:
                print(units)
                print_grid()
                exit(0)
            break
    else:
        grid[at(s)] = 'O'
        units += 1
    #print_grid()
#print(units)
