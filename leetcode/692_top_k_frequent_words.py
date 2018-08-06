import unittest
import heapq
from collections import Counter


class Solution(object):  # O(N + k*logN)
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [(-cnt, word) for word, cnt in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


# class Solution(object):  # O(N*logN)
#     def topKFrequent(self, words, k):
#         count = Counter(words)
#         candidates = list(count.keys())
#         candidates.sort(key = lambda w: (-count[w], w))
#         return candidates[:k]


class BasicTest(unittest.TestCase):
    def test_1(self):
        result = Solution().topKFrequent(['I', 'say', 'hello', 'to', 'hello', 'world'], k=2)
        self.assertEqual(result, ['hello', 'I'])

    def test_2(self):
        words = ['hello'] * 10000000
        words.append('world')
        result = Solution().topKFrequent(words, k=2)
        self.assertEqual(result, ['hello', 'world'])
    
    def test_leetcode_1(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k =2
        expected_result = ["i", "love"]
        result = Solution().topKFrequent(words, k)
        self.assertEqual(result, expected_result)

    def test_leetcode_2(self):
        words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
        k = 4
        expected_result = ["the", "is", "sunny", "day"]
        result = Solution().topKFrequent(words, k)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main(verbosity=2)