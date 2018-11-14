#!/usr/bin/env python3
import unittest

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d1 = dict()
        d2 = dict()
        # fill the dicts with index on the list as a value
        for i, v in enumerate(list1):
            d1[v] = i
        for i, v in enumerate(list2):
            d2[v] = i
        merged = dict()
        # print(d1.values())
        # print(d2)
        for resto in set(d1.keys()) & set(d2.keys()):  # common restos only
            merged[resto] = d1.get(resto, 0) + d2.get(resto, 0)
        pairs = sorted(merged.items(), key=lambda x: x[1])
        max_index_sum = pairs[0][1]
        return [x[0] for x in pairs if x[1] == max_index_sum]
                   
        

class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = ["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        expected_output = ["Shogun"]
        output = Solution().findRestaurant(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = ["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"]
        expected_output = ["Shogun"]
        output = Solution().findRestaurant(*input_)
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main(verbosity=2)