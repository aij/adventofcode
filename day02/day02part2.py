#!/usr/bin/env python3

import sys

class RPS:
    def __init__(self, s):
        self.score = s
        self.val = s-1
    pass

rock = RPS(1)
paper = RPS(2)
scissors = RPS(3)

vals = [rock, paper, scissors]

def parseABC(c):
    if c == 'A':
        return rock
    if c == 'B':
        return paper
    if c == 'C':
        return scissors
    assert false, "Unexpected ABCXYZ value"

def parseXYZ(c):
    if c == 'X':
        return -1 # lose
    if c == 'Y':
        return 0 # draw
    if c == 'Z':
        return 1 # win

def play(them, me):
    if them == me:
        return 3
    if (them.val+1) % 3 == me.val:
        return 6
    return 0

total_score = 0
for l in sys.stdin.readlines():
    (them, me) = l.strip().split()
    them = parseABC(them)
    me = parseXYZ(me)
    me = vals[(them.val + me + 3)%3]

    score = me.score + play(them, me)
    total_score += score

print(total_score)
