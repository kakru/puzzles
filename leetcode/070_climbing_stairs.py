class Solution:
    # recursive solution; would need caching (!)
    # O(2^n), space: O(n)

    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n <= 0: return 0
    #     elif n == 1: return 1
    #     elif n == 2: return 2
    #     return (
    #         self.climbStairs(n-2) +  # after first jumping 2 steps
    #         self.climbStairs(n-1)    # after first jumping 1 step
    #     )

    # dynamic programming
    # O(n), space: O(n)
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = [0, 1, 2]
        i = n  # used for n <= 2
        for i in range(3, n+1):
            r.append(r[max(0, i-2)] + r[max(0, i-1)])
        return r[i]
    
    # but there are even better solutions

    # O(n), space: O(1) - just calculating Fibonacci Number which we realize it is..

    # O(log(n)), space: O(1) - with Binets Method to calculate n-th Fibonacci Number
    # https://leetcode.com/articles/climbing-stairs/

    # or:
    # O(log(n)), space: O(1) - with Fibonacci Formula
    # https://leetcode.com/articles/climbing-stairs/