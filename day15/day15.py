#!/usr/bin/env python3

import sys
import os
import re

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

origin = vec2(0,0)

def md(a,b):
    return abs(a.x - b.x) + abs(a.y - b.y)

class M():
    def __init__(self, s, b):
        self.s = s
        self.b = b
        self.d = md(s,b)


sensors = []
beacons = []

filename = 'example'; num=10
filename = 'input'; num = 2000000

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')

r = re.compile('[=,:]')

for l in lines:
    #print(l)
    match r.split(l):
      #case ['Sensor at x', int(sx), ' y', int(sy), ' closest beacon is at x', int(bx), ' y', int(by)]:
      case ['Sensor at x', sx, ' y', sy, ' closest beacon is at x', bx, ' y', by]:
        s = vec2(int(sx),int(sy))
        b = vec2(int(bx),int(by))
        m = M(s,b)
        #d = md(s, b)
        print(f"{s} {b} d {m.d}")
        #if num not in range(b.y - m.d, b.y + m.d)
        #if md(s, origin) > m.d + 20:
        #    print(f"Ignoring")
        #    continue
        sensors.append(m)
        beacons.append(b)
      case x:
        raise Exception("unmatched: "+repr(x))


leftmost = min(m.s.x - m.d for m in sensors)
rightmost = max(m.s.x + m.d for m in sensors)

def covered(v):
    #if v in beacons:
    #    return True
    for m in sensors:
        if md(v, m.s) <= m.d:
            return True

def part1():

    y = num
    covered = 0
    for x in range(leftmost, rightmost):
        v = vec2(x,y)
        if v in beacons:
            continue
        for m in sensors:
            if md(v, m.s) <= m.d:
                covered += 1
                break
    print(covered)
    return covered

for y in range(21):
    for x in range(21):
        if not covered(vec2(x,y)):
            print((x,y))
            tf = 4000000 * x + y
            print(tf)

# That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 56000011.)

print('done')
