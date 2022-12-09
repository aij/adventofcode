#!/usr/bin/env python3

import sys
import os
import re

filename = 'example'
#filename = 'input'

with open(filename) as f:
    inp = f.read()

lines = inp.rstrip('\n').split('\n')


for l in lines:
    print(l)
