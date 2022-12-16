#!/usr/bin/env python3

# Usage
# ./dotify.py >in.dot && dot in.dot -Tpdf -O && evince in.dot.pdf

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
    #print(l)
    #m = r.
    (name, rate, ne) = r.search(l).groups()
    rate = int(rate)
    near = ne.split(', ')
    valves[name] = Node(name, rate, near)

print('digraph valves {')

for k,v in valves.items():
    shape = 'circle' if v.rate == 0 else 'diamond'
    print(f"  {k} [shape={shape},label=\"{v.name}: {v.rate}\"]")

print()

for v in valves.values():
    for o in v.near:
        print(f"  {v.name} -> {o}")

print('}')
