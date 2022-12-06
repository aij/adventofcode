#!/usr/bin/env python

import sys
import os
import re

with open(sys.argv[1]) as f:
    inp = f.read()

lines = inp.split('\n') #[:-1]

for l in lines:
    print(l)

inp = inp.strip();

for i in range(len(inp)-5):
    mark = inp[i:i+4]
    if len(set(mark)) == 4:
        print(i+4)
        break
    print('not ' +mark)

for i in range(len(inp)-5):
    mark = inp[i:i+14]
    if len(set(mark)) == len(mark):
        print(i+14)
        break
    print('not ' +mark)
