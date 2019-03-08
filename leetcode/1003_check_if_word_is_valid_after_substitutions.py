#!/usr/bin/env python3

class Solution:
    def isValid(self, S: str) -> bool:
        if not S or len(S) % 3 != 0: return False
        stack = []
        for x in S:
            stack.append(x)
            if x == "c" and len(stack) >= 3 and stack[-3:] == ["a", "b", "c"]:
                for _ in range(3): stack.pop()
        return not bool(stack)

print(Solution().isValid("aabcbc")) 
print(Solution().isValid("abcabcababcc"))
