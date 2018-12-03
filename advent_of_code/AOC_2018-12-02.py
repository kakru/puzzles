#!/usr/bin/env python3
from collections import Counter

# input_data_file = 'AOC_input_data/2018-12-02_0.txt'
input_data_file = 'AOC_input_data/2018-12-02_1.txt'


# ------------------------ 2018-12-02 -- Part 1 -------------------------------
def lines_with_exactly_two_and_three_repeated_characters():
    counter_2, counter_3 = 0, 0
    for line in open(input_data_file, 'r').readlines():
        ch = Counter(line)
        repeated = set(ch.values())
        counter_2 += (2 in repeated)
        counter_3 += (3 in repeated)
    return counter_2 * counter_3

# ------------------------ 2018-12-02 -- Part 2 -------------------------------
def lines_that_have_a_twin_line_different_by_only_one_character():
    lines = open(input_data_file, 'r').readlines()
    for skip in range(len(lines[0])):
        seen = set()
        for line in lines:
            v = line[:skip] + line[skip+1:]
            if v in seen:
                return v[:-1]  # skipping the '\n' character
            else:
                seen.add(v)
    return None


print(lines_with_exactly_two_and_three_repeated_characters())
print(lines_that_have_a_twin_line_different_by_only_one_character())
