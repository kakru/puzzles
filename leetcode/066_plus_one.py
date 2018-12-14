#!/usr/bin/env python3

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index = len(digits) - 1
        while index >= 0:
            new_digit = digits[index] + 1
            if new_digit == 10:
                digits[index] = 0
                index -= 1
                continue
            else:
                digits[index] += 1
                break
        else:
            return [1] + digits  # 40 ms
            # digits.insert(0, 1)  # 44 ms
        return digits
