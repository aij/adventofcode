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
    print(l, flush=True)
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

#m = maxi(30, valves[start], [], start)
#print(m)


class State():
    def __init__(self):
        self.time = 26
        self.at = [valves[start], valves[start] ]
        self.open = []
        #self.frm = [None, None]

state = State()

class Move():
    def __init__(self, p, to):
        self.p = p
        self.to = to
    def move(self):
        p = self.p
        self.frm = state.at[p]
        #state.frm[p] = self.frm
        state.at[p] = self.to
        return (0, self.frm)
    def unmove(self):
        p = self.p
        state.at[p] = self.frm

class Open():
    def __init__(self, p):
        self.p = p
    def move(self):
        p = self.p
        at = state.at[p]
        state.open.append(at)
        self.at = at
        return (at.rate * state.time, None)
    def unmove(self):
        pop = state.open.pop()
        assert pop is self.at

def moves(p, frm):
    at = state.at[p]
    canopen = at not in state.open
    m = [Move(p, valves[x]) for x in at.near if x not in frm ]
    if canopen: m.append(Open(p))
    return m

def max2(frm):
    if state.time == 0 or len(state.open) == openable:
        return 0

    best = 0

    movesme = moves(0, frm)
    movesit = moves(1, frm)
    state.time -= 1
    for m in movesme:
        s1,f1 = m.move()
        for n in movesit:
            s2,f2 = n.move()
            s = s1 + s2 + max2([f1,f2])
            if s > best:
                best = s
                if state.time == 25:
                    print(f"Best so far: {best}", flush=True)
            if state.time > 7:
                print(f'Unmoving time={state.time} additional_score={s} best at this level = {best}', flush=True)
            n.unmove()
        m.unmove()
    state.time += 1
    return best

print(max2(''))


# New plan: Build a strongy connected graph with interesting nodes and distances between them. Only consider moves to unopened nodes.
# Moves will take variable amounts of time.
