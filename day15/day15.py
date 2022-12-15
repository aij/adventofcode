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

    def __repr__(self):
        return f"{self.s} {self.b} d {m.d}"

    def perimeter(self):
        d1 = self.d + 1
        top = self.s.y - d1
        bottom = self.s.y + d1
        start = -top if top < 0 else 0
        stop = box.stop - top if bottom > box.stop else 2*d1+1
        for i in range(start, stop):
            y = top+i
            #if y not in box:
            #    continue # TODO: Optimize?
            assert y in box
            j = i if i < d1 else 2*d1 - i
            x1 = self.s.x + j
            x2 = self.s.x - j
            if x1 in box:
                yield vec2(y,x1)
            if x2 in box:
                yield vec2(y,x2)


sensors = []
beacons = []

filename = 'example'; num=10; box = range(21)
filename = 'input'; num = 2000000; box = range(4000001)
#filename = 'oddone'; num = 2000000; box = range(4000001)

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
        print(m)
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


for m in sensors:
    print(f"Checking {m}")
    for v in m.perimeter():
        if not covered(v):
            print(v)
            tf = 4000000 * v.x + v.y
            print(tf)

# That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 56000011.)

print('done')
