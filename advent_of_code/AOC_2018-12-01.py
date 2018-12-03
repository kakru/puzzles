#!/usr/bin/env python3
import re
import itertools

input_data_file = 'AOC_input_data/2018-12-01_1.txt'
pattern = re.compile(r'^([+-])(\d+)$')


# ------------------------ 2018-12-01 -- Part 1 -------------------------------
def resulting_frequency(input_data_file):
    result = 0
    for line in open(input_data_file, 'r').readlines():
        sign, number = re.match(pattern, line).groups()
        if sign=='-': result -= int(number)
        else: result += int(number)
    return result

# ------------------------ 2018-12-01 -- Part 2 -------------------------------
def first_frequency_reached_twice(input_data_file):
    seen = set([0])
    result = 0
    lines = open(input_data_file, 'r').readlines()
    for line in itertools.cycle(lines):
        sign, number = re.match(pattern, line).groups()
        if sign=='-': result -= int(number)
        else: result += int(number)
        if result in seen:
            return result
        else:
            seen.add(result)


print(resulting_frequency(input_data_file))

print(first_frequency_reached_twice(input_data_file))