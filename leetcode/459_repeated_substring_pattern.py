#!/usr/bin/env python3
from typing import *

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        if size == 0: return True
        elif size == 1: return False
        for substr_size in range(size//2, 0, -1):
            if size % substr_size != 0: continue
            multiplier = size // substr_size
            substr = s[:substr_size]
            for idx in range(substr_size):
                character = substr[idx]
                if any(character != s[j*substr_size + idx] for j in range(1, multiplier)): break
            else:
                return True
        return False
