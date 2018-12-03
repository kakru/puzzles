#!/usr/bin/env python3
import re
from collections import namedtuple

# input_data_file = 'AOC_input_data/2018-12-03_0.txt'
input_data_file = 'AOC_input_data/2018-12-03_1.txt'
pattern = re.compile(r'^#(\d+)+\s@\s(\d+),(\d+):\s(\d+)x(\d+)$')
Claim = namedtuple('Claim', ['id', 'x', 'y', 'width','height'])


def overlap(input_data_file):
    MAX_BOARD_SIZE = 1000
    data = []
    board = [[0 for _ in range(MAX_BOARD_SIZE)] for _ in range(MAX_BOARD_SIZE)]
    for line in open(input_data_file, 'r').readlines():
        data.append( Claim(*(int(i) for i in re.match(pattern, line).groups())) )    
    for c in data:
        for x in range(c.width):
            for y in range(c.height):
                board[c.x + x][c.y + y] += 1
    
    # ------------------------ 2018-12-03 -- Part 1 ---------------------------
    ov = 0
    for x in range(MAX_BOARD_SIZE):
        for y in range(MAX_BOARD_SIZE):
            if board[x][y] > 1:
                ov += 1
    
    # ------------------------ 2018-12-03 -- Part 2 ---------------------------
    for c in data:
        q = 0
        for x in range(c.width):
            for y in range(c.height):
                q += board[c.x + x][c.y + y]
        if q == c.width * c.height:
            return ov, c.id


print(overlap(input_data_file))