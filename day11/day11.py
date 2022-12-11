#!/usr/bin/env python3

import re


filename = 'example'
filename = 'input'


with open(filename) as f:
    inp = f.read()

monks = inp.rstrip('\n').split('\n\n')

def mkoperation(left, op, right):
    assert left == 'old'
    if op == '+':
        operand = lambda x: lambda y: x + y
    elif op == '*':
        operand = lambda x: lambda y: x * y
    def fun(old):
        if right == 'old':
            r = old
        else:
            r = int(right)
        return operand(old)(r)
    return fun

class Monkey():
    def __init__(self, num, txt):
        lines = txt.split('\n')
        (name, starting, operation, test, true, false) = (x.strip() for x in lines)
        self.name = name.rstrip(':')
        self.num = num
        assert num == int(self.name.split(' ')[1])

        # '  Starting items: 79, 98'
        assert starting.startswith("Starting items: ")
        items = starting.split(': ')[1].split(', ')
        self.items = [int(x) for x in items]

        # '  Operation: new = old * 19'
        (left, op, right) = operation.removeprefix("Operation: new = ").split(' ')
        self.operation = mkoperation(left, op, right)

        # '  Test: divisible by 23'
        assert test.startswith("Test: divisible by ")
        self.test_divisible = int(test.split(" ")[-1])

        self.true = int(true.removeprefix("If true: throw to monkey "))
        self.false = int(false.removeprefix("If false: throw to monkey" ))

        self.inspections = 0

    def execute(self):
        global monkeys
        for item in self.items:
            self.inspections += 1
            worry = self.operation(item)
            worry = worry // 3
            if worry % self.test_divisible == 0:
                target = self.true
            else:
                target = self.false
            monkeys[target].items.append(worry)
        # All items are thrown
        self.items = []

        
monkeys = [Monkey(n,t) for (n,t) in enumerate(monks)]

for r in range(20):
    for m in monkeys:
        m.execute()

print(len(monkeys))

for m in monkeys:
    print(m.inspections)

a, b = sorted(m.inspections for m in monkeys)[-2:]

print(f"{a} * {b} = {a*b}")
