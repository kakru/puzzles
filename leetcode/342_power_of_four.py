from math import log
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # return num>0 and round(log(num, 4))==log(num, 4)
        if num <= 0: return False
        v = log(num, 4)
        return round(v)==v




for x in range(0, 18):
    print(Solution().isPowerOfFour(x))