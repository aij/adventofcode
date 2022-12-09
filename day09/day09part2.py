#!/usr/bin/env python3

import sys
import os
import re

filename = 'example2'
filename = 'input'

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')

visited = set()

start = (0,0)

visited.add(start)

rope = [start] * 10


def near(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    m = max(abs(dx), abs(dy))
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

def movetail(i, head, tail):
    if near(head, tail):
        return
    vec = v2sub(head, tail)
    vec = tuple(bound(i) for i in vec)
    newtail = v2add(tail, vec)
    rope[i] = newtail
    if i == 9:
        visited.add(newtail)
    #print(f"Moved tail = {tail}, head = {head}")

def step(where):
    head = rope[0]
    print(f"head { head} where {where}")
    head = v2add(head, where)
    rope[0] = head
    #print(f"tail = {tail}, head = {head}")
    for i in range(1, len(rope)):
        movetail(i, rope[i-1], rope[i])

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


# That's not the right answer. If you're stuck, make sure you're using the full input data; there are also some general tips on the about page, or you can ask for hints on the subreddit. Please wait one minute before trying again. (You guessed 2532.)

# Right answer was 2533... visited.add(tail) instead visited.add(newtail) meant I missed the last tail position
