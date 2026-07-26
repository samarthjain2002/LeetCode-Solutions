"""
Accepted
4000 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Largest Integer With Given Digit Sum.
Memory Usage: 19.32 MB, less than 23.00% of Python3 online submissions for Largest Integer With Given Digit Sum.
"""
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > n * 9:
            return -1
        elif s == 0:
            return 0

        num = 0
        while s >= 9:
            num *= 10
            num += 9
            s -= 9
            n -= 1

        if s:
            num *= 10
            num += s
            n -= 1

        num *= 10**n

        return num