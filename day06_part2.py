#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 16:31:53 2016

@author: jbilbie

Advent of Code 2016
--- Day 6: Signals and Noise ---
"""

f = open('day06_input.txt', 'r')

letterCountDict = {}
correctMessage = ''

for line in f:
    for i in range(len(line)-1):
        if not i in letterCountDict.keys():
            letterCountDict[i] = {line[i]: 0}
        if not line[i] in letterCountDict[i]:
            letterCountDict[i][line[i]] = 0
        letterCountDict[i][line[i]] += 1

for key in letterCountDict:
    sortedByValue = sorted(letterCountDict[key].items(), key=lambda x: (x[1]))
    correctMessage += sortedByValue[0][0]

print('The original message from Santa is {}.'.format(correctMessage))     