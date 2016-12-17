#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 15:56:57 2016

@author: jbilbie

Advent of Code 2016
--- Day 12: Leonardo's Monorail ---
"""

def cpy(x, y, dict, index):
    if x in dict:
        dict[y] = dict[x]
    else:
        dict[y] = int(x)
    index += 1
    return dict, index
    
def inc(x, dict, index):
    dict[x] += 1
    index += 1
    return dict, index
    
def dec(y, dict, index):
    dict[y] -= 1
    index += 1
    return dict, index

def jnz(x, y, dict, index):
    if x in dict:
        if dict[x] != 0:
            index += int(y)
            return index
        else:
            index += 1
            return index
    elif int(x) != 0:
        index += int(y)
        return index
    index += 1
    return index
        

f = open('day12_input.txt', 'r')
g = f.readlines()
instructions = []
for item in g:
    instructions.append(item.rstrip().split(' '))
    
registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}

index = 0
while index < len(instructions):
    command = instructions[index][0]
    value1 = instructions[index][1]
    if len(instructions[index]) == 3:
        value2 = instructions[index][2]
        
    if command == 'cpy':
        registers, index = cpy(value1, value2, registers, index)
    elif command == 'inc':
        registers, index = inc(value1, registers, index)
    elif command == 'dec':
        registers, index = dec(value1, registers, index)
    else:
        index = jnz(value1, value2, registers, index)

print('The value in register a is {}.'.format(registers['a']))
