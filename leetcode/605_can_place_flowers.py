#/usr/bin/env python3
import unittest

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed_len = len(flowerbed)
        if flowerbed[0] == 0 and (flowerbed_len < 2 or flowerbed[1] == 0):
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and (flowerbed_len < 2 or flowerbed[-2] == 0):
            flowerbed[-1] = 1
            n -= 1
        for i in range(1, flowerbed_len - 1):
            if ((flowerbed[i-1] == 0) and (flowerbed[i] == 0) and (flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                n -= 1
                i += 1
        return n <= 0


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #TODO: can be simplified into one if statement
        flowerbed_len = len(flowerbed)
        if flowerbed[0] == 0 and (flowerbed_len < 2 or flowerbed[1] == 0):
            flowerbed[0] = 1
            n -= 1
        if flowerbed[-1] == 0 and (flowerbed_len < 2 or flowerbed[-2] == 0):
            flowerbed[-1] = 1
            n -= 1
        for i in range(1, flowerbed_len - 1):
            if ((flowerbed[i-1] == 0) and (flowerbed[i] == 0) and (flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                n -= 1
                i += 1
        return n <= 0

        


class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = [1,0,0,0,1], 1
        expected_output = True
        output = Solution().canPlaceFlowers(*input_)
        self.assertEqual(output, expected_output)

    def test_2(self):
        input_ = [1,0,0,0,1], 2
        expected_output = False
        output = Solution().canPlaceFlowers(*input_)
        self.assertEqual(output, expected_output)

    def test_3(self):
        input_ = [0,0,1,0,1], 1
        expected_output = True
        output = Solution().canPlaceFlowers(*input_)
        self.assertEqual(output, expected_output)

    def test_4(self):
        input_ = [0,0,1,0,0], 2
        expected_output = True
        output = Solution().canPlaceFlowers(*input_)
        self.assertEqual(output, expected_output)

    def test_5(self):
        input_ = [0,0], 1
        expected_output = True
        output = Solution().canPlaceFlowers(*input_)
        self.assertEqual(output, expected_output)

    def test_6(self):
        input_ = [0,1], 1
        expected_output = False
        output = Solution().canPlaceFlowers(*input_)
        self.assertEqual(output, expected_output)

    def test_7(self):
        input_ = [0], 1
        expected_output = True
        output = Solution().canPlaceFlowers(*input_)
        self.assertEqual(output, expected_output)



if __name__ == '__main__':
    unittest.main(verbosity=2)