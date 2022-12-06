#!/usr/bin/env python

import sys
import os
import re

with open(sys.argv[1]) as f:
    inp = f.read()

lines = inp.split('\n') #[:-1]

for l in lines:
    print(l)
