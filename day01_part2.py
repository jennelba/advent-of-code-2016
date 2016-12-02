#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:20:38 2016

@author: jbilbie

Advent of Code 2016
--- Day 1: No Time for a Taxicab ---
"""

NORTH = (0, 1)
SOUTH = (0, -1)
EAST = (1, 0)
WEST = (-1, 0)

TURNLEFT = {NORTH: WEST, SOUTH: EAST, EAST: NORTH, WEST: SOUTH}
TURNRIGHT = {NORTH: EAST, SOUTH: WEST, EAST: SOUTH, WEST: NORTH}


def makeTurn(direction, turn):    
    if turn == 'L':
        return TURNLEFT[direction]
    return TURNRIGHT[direction]

def takeSteps(position, direction, steps, locations, isVisited):
    for step in range(steps):
        nextStep = ((position[0] + direction[0]), (position[1] + direction[1]))        
        if nextStep in locations:
            isVisited = True
            return nextStep, locations, isVisited
        
        locations.append(nextStep)
        position = nextStep

    return nextStep, locations, isVisited
    
def computeBlocks(position):
    return abs(position[0]) + abs(position[1])
    
    
f = open('day01_input.txt')
input = f.read().split(', ')

position = (0, 0)
direction = NORTH
locations = [position]
isVisited = False
    
for command in input:
    turn = command[0]
    steps = int(command[1:])

    nextDirection = makeTurn(direction, turn)
    nextPosition, locations, isVisited = takeSteps(position, nextDirection, steps, locations, isVisited)
    
    if isVisited:
        print('No actually, Easter Bunny HQ is {} blocks away.'.format(computeBlocks(nextPosition)))
        break
    
    direction = nextDirection
    position = nextPosition