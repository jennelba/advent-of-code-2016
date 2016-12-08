#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:41:57 2016

@author: jbilbie

Advent of Code 2016
--- Day 7: Internet Protocol Version 7 ---
"""

def findABBA(i):
    for j in range(len(i)-3):
        if i[j+1] == i[j+2] and i[j] == i[j+3] and i[j] != i[j+1]:
            return True
    return False
    
f = open('day07_input.txt', 'r')

count = 0

for line in f:
    sequence = line.rstrip()
    supernetSeq = []
    hypernetSeq = []
    
    while len(sequence) > 0:
        part = sequence.partition('[')
        supernetSeq.append(part[0])
        sequence = part[2]
        part = sequence.partition(']')
        if part[0] != '':
            hypernetSeq.append(part[0])
        sequence = part[2]
    
    for hypernetSegment in hypernetSeq:
        hypernetHasABBA = findABBA(hypernetSegment)
        if hypernetHasABBA:
            break
    
    if not hypernetHasABBA:       
        for supernetSegment in supernetSeq:
            supernetHasABBA = findABBA(supernetSegment)
            if supernetHasABBA:
                count += 1
                break
            
print('{} IPs support TLS'.format(count))