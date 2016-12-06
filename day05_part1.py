#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 13:04:56 2016

@author: jbilbie

Advent of Code 2016
--- Day 5: How About a Nice Game of Chess? ---
"""

import hashlib

m = hashlib.md5()
decimal = 0
result = ''
password = ''

doorID = 'ugkcyxxp'

while len(password) != 8:
    test = (doorID + str(decimal)).encode('utf-8')
    m.update(test)
    result = m.hexdigest()
    
    if result.startswith('00000'):
        password += result[5]

    decimal += 1
    m = hashlib.md5()

print('The password is {}'.format(password))