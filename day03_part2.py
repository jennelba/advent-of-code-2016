#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:15:34 2016

@author: jbilbie

Advent of Code 2016
--- Day 3: Squares With Three Sides ---
"""

f = open('day03_input.txt', 'r')

count = 0
a, b, c = [], [], []

for line in f:
    nums = [int(n)for n in line.split()]
    a.append(nums[0])
    b.append(nums[1])
    c.append(nums[2])

    if len(c) == 3:
        for lst in a, b, c:
            lst.sort()
            if lst.pop() < sum(lst):
                count += 1
            a, b, c = [], [], []
    else:
        continue
    
print('There are {} triangles.'.format(count))