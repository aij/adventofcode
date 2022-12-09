#!/usr/bin/env python3

import sys
import os
import re

filename = 'example'
filename = 'input'

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')

visited = set()

start = (0,0)

head = start
tail = start

visited.add(start)

def near(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    m = max(abs(dx), abs(dy))
    #print(f"{dx} {dy} {m} {p1},{p2} head={head}, tail={tail}")
    return m <= 1

def v2add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def v2sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def bound(i):
    if i == 0:
        return 0
    if i > 0:
        return 1
    if i < 0:
        return -1
    assert False

def movetail():
    global tail
    vec = v2sub(head, tail)
    vec = tuple(bound(i) for i in vec)
    tail = v2add(tail, vec)
    visited.add(tail)
    #print(f"Moved tail = {tail}, head = {head}")

def step(where):
    global head
    head = v2add(head, where)
    print(f"tail = {tail}, head = {head}")
    if near(head, tail):
        return
    movetail()

dirs = {
    'R': (0,1),
    'U': (1,0),
    'L': (0,-1),
    'D': (-1,0)
}

for l in lines:
    (d,s) = l.split()
    s = int(s)
    print(l)
    where = dirs[d]
    for i in range(s):
        step(where)

print(len(visited))

print('---------')
