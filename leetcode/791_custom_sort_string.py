from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c_T = Counter(T)
        return "".join(
            x[0] * x[1] for x in sorted(c_T.items(), key=lambda s: S.find(s[0]))
        )
