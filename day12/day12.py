#!/usr/bin/env python3

import sys
import os
import re

filename = 'example'
filename = 'input'

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')

width = len(lines[0])
height = len(lines)

#assert width == height NOPE
print(f"Width {width} Height {height}")

assert all(len(x) == width for x in lines)

grid = ''.join(lines)

def H(p):
    c = grid[p]
    match c:
      case 'S':
        return 'a'
      case 'E':
        return 'z'
      case c:
        return c

def pos(x,y):
    return x + y*width

dirs = {
    'R': (0,1),
    'U': (1,0),
    'L': (0,-1),
    'D': (-1,0)
}


def v2add(a, b):
    return (a[0]+b[0], a[1]+b[1])

def v2sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def neighbors(x,y):
    if x > 0:
        yield (x-1, y)
    if y > 0:
        yield (x, y-1)
    if x < width-1:
        yield (x+1, y)
    if y < height-1:
        yield x, y+1

class Node():
    def __init__(self, xy):
        x,y = xy
        self.x = x
        self.y = y
        self.pos = pos(x,y)
        self.char = grid[self.pos]
        self.height = H(self.pos)
        self.h = ord(self.height)
        self.edges = []
    def __lt__(self, other):
        return self.pos < other.pos

    def __repr__(self):
        e = [str(e) for e in self.edges]
        return f"({self.x},{self.y})@{self.height} edges=({e})"

    def __str__(self):
        return f"({self.x},{self.y})@{self.height}"

nodes = {}

for x in range(width):
    for y in range(height):
        nodes[(x,y)] = Node((x,y))


for x in range(width):
    for y in range(height):
        m = nodes[(x,y)]
        for ni in neighbors(x,y):
            n = nodes[ni]
            if (n.h - m.h) <= 1:
                m.edges.append(n)
                # reverse edge not tracked
            if m.char == 'S':
                print(f'Neighbor of S: {n}')
        if m.char == 'S':
            start = m
        elif m.char == 'E':
            end = m

assert len(nodes) == len(grid)

for k,n in nodes.items():
    print(repr(n))

# From https://github.com/norvig/pytudes/blob/main/ipynb/Advent%20of%20Code.ipynb
from heapq       import heappop, heappush
def astar_search(start, h_func, moves_func):
    "Find a shortest sequence of states from start to a goal state (a state s with h_func(s) == 0)."
    frontier  = [(h_func(start), start)] # A priority queue, ordered by path length, f = g + h
    previous  = {start: None}  # start state has no previous state; other states will
    path_cost = {start: 0}     # The cost of the best path to a state.
    while frontier:
        (f, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in moves_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))

def Path(previous, s):
    "Return a list of states that lead to state s, according to the previous dict."
    return ([] if (s is None) else Path(previous, previous[s]) + [s])

def h_func(n):
    if n == end:
        return 0
    return abs(end.x - n.x) + abs(end.y - n.y)

path = astar_search(start, h_func, lambda n: n.edges)

print(path)
print(len(path)-1)
