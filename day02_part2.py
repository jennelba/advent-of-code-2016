#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:32:21 2016

@author: jbilbie

Advent of Code 2016
--- Day 2: Bathroom Security ---
"""

movesDict = {1: {'L': 1, 'R': 1, 'U': 1, 'D': 3},
             2: {'L': 2, 'R': 3, 'U': 2, 'D': 6},
             3: {'L': 2, 'R': 4, 'U': 1, 'D': 7},
             4: {'L': 3, 'R': 4, 'U': 4, 'D': 8},
             5: {'L': 5, 'R': 6, 'U': 5, 'D': 5},
             6: {'L': 5, 'R': 7, 'U': 2, 'D': 'A'},
             7: {'L': 6, 'R': 8, 'U': 3, 'D': 'B'},
             8: {'L': 7, 'R': 9, 'U': 4, 'D': 'C'},
             9: {'L': 8, 'R': 9, 'U': 9, 'D': 9},
             'A': {'L': 'A', 'R': 'B', 'U': 6, 'D': 'A'},
             'B': {'L': 'A', 'R': 'C', 'U': 7, 'D': 'D'},
             'C': {'L': 'B', 'R': 'C', 'U': 8, 'D': 'C'},
             'D': {'L': 'D', 'R': 'D', 'U': 'B', 'D': 'D'}}

f = open('day02_input.txt', 'r')
             
startPos = 5
code = ''

for line in f:
    for char in line.rstrip():
        startPos = movesDict[startPos][char]
    code += str(startPos)
print('Code: {}'.format(code))