#/usr/bin/env python3
import unittest

# class Solution:  # Time Limit Exceeded
#     def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
#         results = []
#         for num, i in queries:
#             A[i] += num
#             results.append(sum(A[i] for i in range(len(A)) if A[i]%2 == 0))
#         return results

# class Solution:  # 180 ms (39.35%)
#     # def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
#     def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
#         evens = [x%2 == 0 for x in A]
#         evens_sum = sum([A[i] for i in range(len(A)) if evens[i]])
#         results = []
#         for num, i in queries:
#             if evens[i] == True:
#                 evens_sum -= A[i]
#                 if num%2 == 1:
#                     evens[i] = False
#                     A[i] += num
#                 else: 
#                     A[i] += num
#                     evens_sum += A[i]
#             else:
#                 if num%2 == 1:
#                     evens[i] = True
#                     A[i] += num
#                     evens_sum += A[i]
#                 else:
#                     A[i] += num
#             results.append(evens_sum)
#         return results


class Solution:  # 180 ms (39.35%) = the same
    # def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        sum_ = sum(x for x in A if x%2 == 0)
        results = []
        for num, i in queries:
            if A[i] % 2 == 0: sum_ -= A[i]
            A[i] += num
            if A[i] % 2 == 0: sum_ += A[i]
            results.append(sum_)
        return results


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,2,3,4], [[1,0],[-3,1],[-4,0],[2,3]]
        expected_output = [8,6,2,4]
        output = Solution().sumEvenAfterQueries(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1], [[4,0]]
        expected_output = [0]
        output = Solution().sumEvenAfterQueries(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
