#!/usr/bin/env python3

import sys
import os
import re

def v2add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def v2sub(a, b):
    return (a[0]-b[0], a[1]-b[1])

filename = 'example'
filename = 'input'

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')


X = 1
history = []
instrs = []
def cycle(i):
    history.append(X)
    instrs.append(i)

for l in lines:
    print(l)
    l = l.split(' ')
    if l[0] == 'noop':
        cycle(l)
    elif l[0] == 'addx':
        n = int(l[1])
        cycle(l)
        cycle(l)
        X += n
    else:
        assert False


s = sum(history[i-1] * i for i in range(20, 221, 40))
s = 0
for i in range(20, 221, 40):
    n = history[i-1] * i
    print(f"{i} * {history[i-1]} = {n} running {instrs[i-1]}" )
    s += n
print(s)

for (i,v) in enumerate(history):
    cycle = i+1
    if i%40 == 0:
        print()
    c = i%40 + 1
    if abs(c-(v+1)) <= 1:
        char = '#'
    else:
        char = '.'
    print(char, end='')
