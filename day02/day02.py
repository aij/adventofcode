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

def parse(c):
    if c == 'A':
        return rock
    if c == 'B':
        return paper
    if c == 'C':
        return scissors
    if c == 'X':
        return rock
    if c == 'Y':
        return paper
    if c == 'Z':
        return scissors
    assert false, "Unexpected ABCXYZ value"

def play(them, me):
    if them == me:
        return 3
    if (them.val+1) % 3 == me.val:
        return 6
    return 0

total_score = 0
for l in sys.stdin.readlines():
    (them, me) = (parse(s) for s in l.strip().split())
    score = me.score + play(them, me)
    total_score += score

print(total_score)
