#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 10:41:57 2016

@author: jbilbie

Advent of Code 2016
--- Day 7: Internet Protocol Version 7 ---
"""

def findBABs(sequence):
    babs = []
    for i in sequence:
        for j in range(len(i)-2):
            if i[j] == i[j+2] and i[j] != i[j+1]:
                babs.append(i[j:j+3])
    return babs

def makeABAs(babs):
    abas = []
    for bab in babs:
        abas.append(bab[1] + bab[0] + bab[1])
    return abas

def findABA(aba, supernetSequence):
    for i in supernetSequence:
        if aba in i:
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

    allTheBABs = findBABs(hypernetSeq)
    
    if allTheBABs != []:    
        allTheABAs = makeABAs(allTheBABs)                        
        for aba in allTheABAs:
            supernetHasABA = findABA(aba, supernetSeq)
            if supernetHasABA:
                count += 1
                break

print('{} IPs support SSL'.format(count))