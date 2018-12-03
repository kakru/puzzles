import unittest

# class Solution:  # naive solution with O(n) time
#     def findRotationPoint(self, words):
#         """
#         :type A: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         length = len(words)
#         if length == 0:
#             return None
#         elif length == 1:
#             return 0
#         index = 1
#         prev = now = words[0]
#         while index < length:
#             prev, now = now, words[index]
#             if prev > now:
#                 return index
#             index += 1

class Solution:  # with binary search O(logn)
    def findRotationPoint(self, words):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        length = len(words)
        left, right = 0, length-1
        while True:
            middle = (left + right)//2
            if words[left] < words[middle] > words[right]:
                left = middle
            elif words[left] > words[middle] < words[right]:
                right = middle
            else:
                break
        if right-left == length-1:  # middle index never moved
            return 0
        else:
            return middle+1


class BasicTest(unittest.TestCase):
    def test_not_rotated(self):
        input_ = [
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage',
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
        ]
        expected_output = 0
        output = Solution().findRotationPoint(input_)
        self.assertEqual(output, expected_output)

    def test_1(self):
        input_ = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage',
        ]
        expected_output = 5
        output = Solution().findRotationPoint(input_)
        self.assertEqual(output, expected_output)


    def test_2(self):
        input_ = [
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage',
        ]
        expected_output = 4
        output = Solution().findRotationPoint(input_)
        self.assertEqual(output, expected_output)


    def test_3(self):
        input_ = [
            'ptolemaic',
            'retrograde',
            'supplant',
            'undulate',
            'xenoepist',
            'zzzzzz',
            'asymptote',  # <-- rotates here!
            'babka',
            'banoffee',
            'engender',
            'karpatka',
            'othellolagkage',
        ]
        expected_output = 6
        output = Solution().findRotationPoint(input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)