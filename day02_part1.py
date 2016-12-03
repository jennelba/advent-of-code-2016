#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:12:12 2016

@author: jbilbie

Advent of Code 2016
--- Day 2: Bathroom Security ---
"""

movesDict = {1: {'L': 1, 'R': 2, 'U': 1, 'D': 4},
             2: {'L': 1, 'R': 3, 'U': 2, 'D': 5},
             3: {'L': 2, 'R': 3, 'U': 3, 'D': 6},
             4: {'L': 4, 'R': 5, 'U': 1, 'D': 7},
             5: {'L': 4, 'R': 6, 'U': 2, 'D': 8},
             6: {'L': 5, 'R': 6, 'U': 3, 'D': 9},
             7: {'L': 7, 'R': 8, 'U': 4, 'D': 7},
             8: {'L': 7, 'R': 9, 'U': 5, 'D': 8},
             9: {'L': 8, 'R': 9, 'U': 6, 'D': 9}}

f = open('day02_input.txt', 'r')
             
startPos = 5
code = ''

for line in f:
    for char in line.rstrip():
        startPos = movesDict[startPos][char]
    code += str(startPos)
print('Code: {}'.format(code))