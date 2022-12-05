#!/usr/bin/env python3

import sys
import re

stacks = {}

def items(line):
    i = 0
    while len(line) >= 3:
        item = line[:3]
        line = line[4:]
        i += 1
        if item == '   ':
            pass # yield None
        else:
            yield (i, item[1])


(stackdata, instr) = sys.stdin.read().split('\n\n')

stackdata = stackdata.split('\n')[:-1]

for d in stackdata:
    for k,v in items(d):
        #print(f"adding {k}  {v}")
        s = stacks.get(k, [])
        s.append(v)
        stacks[k] = s

print(stacks)
for s in stacks.values():
    s.reverse()

print(stacks)
for l in instr.split('\n'):
    #print(l)
    if not l:
        continue
    (MOVE, move, FROM, frm, TO, to) = l.split(' ')
    move = int(move)
    frm = int(frm)
    to = int(to)
    for i in range(move):
        item = stacks[frm].pop()
        stacks[to].append(item)

res = ''
for s in range(1, len(stacks)+1):
    s = stacks[s]
    i = s[-1]
    res += i

print(res)
