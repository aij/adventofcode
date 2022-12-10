#!/usr/bin/env python3

#filename = 'example'
filename = 'input'

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')

X = 1
history = []
def cycle():
    history.append(X)

for l in lines:
    l = l.split(' ')
    if l[0] == 'noop':
        cycle()
    elif l[0] == 'addx':
        n = int(l[1])
        cycle()
        cycle()
        X += n
    else:
        assert False

s = sum(history[i-1] * i for i in range(20, 221, 40))
print(s)

for (i,v) in enumerate(history):
    cycle = i+1
    c = i%40 + 1
    if abs(c-(v+1)) <= 1:
        char = '#'
    else:
        char = ' '
    print(char, end='')
    if i%5 == 4: # Extra space between characters for readability (not to spec)
        print('  ', end='')
    if i%40 == 39:
        print()
