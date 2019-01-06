#/usr/bin/env python3
import unittest

class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num == 0: return ["0:00"]
        bh = {0: [], 1: [], 2: [], 3: [], 4: []}
        for h in range(12):
            bh[bin(h).count("1")].append(str(h))
        bm = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6:[]}
        for m in range(60):
            bm[bin(m).count("1")].append(str(m).zfill(2))
        ans = []
        for bit_hour in (0, 1, 2, 3, 4):
            bit_min = num - bit_hour
            if bit_min < 0: continue
            elif bit_min > 6: continue
            for h in bh[bit_hour]:
                for m in bm[bit_min]:
                    ans.append(h + ":" + m)
        return ans



class BasicTest(unittest.TestCase):
    def test_1(self):
        input_ = 1
        expected_output = ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
        output = Solution().readBinaryWatch(input_)
        self.assertEqual(sorted(output), sorted(expected_output))

    def test_7(self):
        input_ = 7
        expected_output = ["3:31","3:47","3:55","3:59","5:31","5:47","5:55","5:59","6:31","6:47","6:55","6:59","7:15","7:23","7:27","7:29","7:30","7:39","7:43","7:45","7:46","7:51","7:53","7:54","7:57","7:58","9:31","9:47","9:55","9:59","10:31","10:47","10:55","10:59","11:15","11:23","11:27","11:29","11:30","11:39","11:43","11:45","11:46","11:51","11:53","11:54","11:57","11:58"]
        output = Solution().readBinaryWatch(input_)
        self.assertEqual(sorted(output), sorted(expected_output))


if __name__ == '__main__':
    unittest.main(verbosity=2)