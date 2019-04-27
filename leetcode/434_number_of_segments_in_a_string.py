#!/usr/bin/env python3

class Solution:
    def countSegments(self, s: str) -> int:
        length = len(s)
        if length == 0: return 0
        counter, last_non_space = 0, None
        for idx, ch in enumerate(s):
            if ch == " " and idx-1 == last_non_space:  # end of the word
                counter += 1
            elif ch != " ":
                last_non_space = idx
        if s[-1] != " ": counter += 1
        return counter