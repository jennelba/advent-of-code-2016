#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:45:23 2016

@author: jbilbie

Advent of Code 2016
--- Day 4: Security Through Obscurity ---
"""

import string

f = open('day04_input.txt', 'r')

for line in f:
    nameDict = {}
    encryptedName = line[:-12]
    sectorID = int(line[-11:-8])
    checksum = line[-7:-2]

    shift = sectorID % 26
    shift_dict = {'-': ' '}
    for i in range(26-shift):
        shift_dict[string.ascii_lowercase[i]] = string.ascii_lowercase[i+shift]
    for i in range(26-shift, 26):
        shift_dict[string.ascii_lowercase[i]] = string.ascii_lowercase[i-(26-shift)]
    
    targetRoom = 'northpole object storage'
    roomName = ''
    for char in encryptedName:
        roomName += shift_dict[char]
        if roomName == targetRoom:
            print('{} is in sector ID {}'.format(targetRoom, sectorID))