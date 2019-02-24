#/usr/bin/env python3
import unittest

class Solution:  # backtracking, 68 ms (83.26%)
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        result = []
        def helper(candidates, target, combination):
            if target == 0:
                result.append(sorted(combination))
            for i, candidate in enumerate(candidates):
                if candidate <= target:
                    helper(candidates[i:], target - candidate, combination + [candidate])
                else:
                    break
        helper(sorted(candidates), target, [])
        return result


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [2,3,6,7], 7
        expected_output = [[7],
                           [2,2,3]]
        output = Solution().combinationSum(*input_)
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_2(self):
        input_ = [2,3,5], 8
        expected_output = [[2,2,2,2],
                           [2,3,3],
                           [3,5]]
        output = Solution().combinationSum(*input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)