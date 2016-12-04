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

for line in f:
    nums = [int(n) for n in line.split()]
    nums.sort()
    if nums.pop() < sum(nums):
        count += 1

print('There are {} triangles.'.format(count))