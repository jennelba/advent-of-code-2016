#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:45:23 2016

@author: jbilbie

Advent of Code 2016
--- Day 4: Security Through Obscurity ---
"""

f = open('day04_input.txt', 'r')

sectorIDTotal = 0

for line in f:
    nameDict = {}
    encryptedName = line[:-12]
    sectorID = int(line[-11:-8])
    checksum = line[-7:-2]

    for letter in encryptedName:
        if letter == '-':
            continue
        if not letter in nameDict:
            nameDict[letter] = 0
        nameDict[letter] += 1
    
    sortedListOfTuples = sorted(nameDict.items(), key=lambda x: (-x[1],x[0]))

    letters = ''
    for ltr in range(5):
        letters += sortedListOfTuples[ltr][0]
    
    if letters == checksum:
        sectorIDTotal += sectorID

print('Sum of sector IDs: {}'.format(sectorIDTotal))