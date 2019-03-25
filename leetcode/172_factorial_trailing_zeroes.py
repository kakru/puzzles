class Solution:
    def trailingZeroes(self, n: int) -> int:
        # n! = 1*2*3*4*5*6*7...
        #        ^   ^   ^  the crutial are only 5s
        # so let's just count 5s in the factorial
        return 0 if n == 0 else n // 5 + self.trailingZeroes(n // 5)

print(Solution().trailingZeroes(100))