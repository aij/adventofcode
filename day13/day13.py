#!/usr/bin/env python3

import sys
import os
import re

filename = 'example'
filename = 'input'

with open(filename) as f:
    inp = f.read()

groups = inp.rstrip('\n').split('\n\n')

pairs = [ x.split('\n') for x in groups ]
pairs = [ (eval(l), eval(r)) for (l,r) in pairs ]

def checkbad(pair):
    l,r = pair
    if l < r:
        return True
    return False

def check(pair):
    l,r = pair

    match pair:
        case (int(l), int(r)):
            if l < r:
                return True
            if l > r:
                return False

        case ([l, *lr], [r, *rr] ):
            rec = check((l,r))
            if rec is not None:
                return rec
            rec = check((lr,rr))
            if rec is not None:
                return rec
        case ([l, *lr], [] ):
            return False
        case ([], [r, *rr] ):
            return True
        case (int(l), r):
             rec = check(([l], r))
             if rec is not None:
                return rec
        case (l, int(r)):
             rec = check((l, [r]))
             if rec is not None:
                return rec
        case ([],[]):
            return None
        case _:
          raise Exception(f"missing chcek: {pair}")


ok_indices = 0

for i,v in enumerate(pairs):
    #print(f"Checking {v}")
    if check(v):
        ok_indices += i+1

print(ok_indices)


packets = [x for p in pairs for x in p  ]

divider1 = [[2]]
divider2 = [[6]]

packets += [ divider1, divider2 ]

def cmp(a,b):
    match check((a,b)):
        case None: return 0
        case True: return -1
        case False: return 1
        case _: raise Exception("no cmp")

from functools import cmp_to_key
packets.sort(key=cmp_to_key(cmp))

i1 = packets.index(divider1) + 1
i2 = packets.index(divider2) + 1

print(i1*i2)
