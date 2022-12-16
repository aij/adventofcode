#!/usr/bin/env python3

import sys
import os
import re

filename = 'example';
filename = 'input';

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')

r = re.compile('^Valve (..) has flow rate=([0-9]*); tunnels? leads? to valves? (.*)$')

class Node():
    def __init__(self, name, rate, near):
        self.name = name
        self.rate = rate
        self.near = near

valves = {}

for l in lines:
    print(l)
    #m = r.
    (name, rate, ne) = r.search(l).groups()
    rate = int(rate)
    near = ne.split(', ')
    valves[name] = Node(name, rate, near)

start = 'AA'

openable = len([x for x in valves.values() if x.rate > 0])

def maxi(time, at, open, frm):
    if time <= 0 or len(open) == openable:
        return 0

    bestother =  max((maxi(time-1, valves[n], open, at.name) for n in at.near if n != frm), default=0)

    if at.rate > 0 and at not in open:
        besthere = (time-1)*at.rate + max(maxi(time-2, valves[n], open + [at], at.name) for n in at.near)
        if besthere > bestother:
            return besthere
    return bestother

m = maxi(30, valves[start], [], start)
print(m)
