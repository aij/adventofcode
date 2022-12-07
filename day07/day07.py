#!/usr/bin/env python3

import sys
import os
import re

with open(sys.argv[1]) as f:
    inp = f.read()

cmds = inp.rstrip().lstrip('$').split('\n$')

class Dir(dict):
    pass

fs = Dir()
#fs.parent = fs

def newdir(parent):
    d = Dir()
    d.parent = parent
    return d

cur = fs

for c in cmds:
    lines = c.split('\n')
    w = lines[0].split(' ')
    #print(w)
    #assert w[0] == '$'
    cmd = w[1]
    args = w[2:]
    output = lines[1:]
    #print(f"cmd = {cmd} args = {args} output = {output}")
    if cmd == 'cd':
        assert len(args) == 1
        a = args[0]
        if a == '/':
            cur = fs
        elif a == '..':
            cur = cur.parent
        else:
            if a not in cur:
                cur[a] = newdir(cur)
            cur = cur[a]
    elif cmd == "ls":
        for o in output:
            (size, name) = o.split(' ')
            if size == 'dir' and name not in cur:
                cur[name] = newdir(cur)
                continue
            size = int(size)
            cur[name] = size
    else:
        raise Exception(f"Unexpected command {cmd}")

#inp = inp.strip();

print(fs)

found = []
dirs = []

def dirsize(t, name):
    tot = 0
    for k,f in t.items():
        #print(f"adding {k} with {f}")
        if type(f) == int:
            tot += f
        elif type(f) == Dir:
            tot += dirsize(f, name+k+'/')
        else:
            raise Exception('Wat')
    if tot < 100000:
        found.append(tot)
    #print(f"returning {tot} for {name}")
    dirs.append((tot, name))
    return tot

used = dirsize(fs, '/')

print(sum(found))


total = 70000000
need = 30000000

free = total - used

to_free = need - free

print(f"free = {free} to_free = {to_free} used = {used}")
dirs.sort()

for (s,n) in dirs:
    if s > to_free:
        print(f"Closest match = {s} at {n}           <------")
        break
    #else:
    #    print(f"not {(s,n)}")
