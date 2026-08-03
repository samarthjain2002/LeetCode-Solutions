"""
Accepted
4006 [Easy]
Runtime: 4 ms, faster than 80.00% of Python3 online submissions for Count Valid Prefixes.
Memory Usage: 19.20 MB, less than 40.00% of Python3 online submissions for Count Valid Prefixes.
"""
class Solution:
    def countValidPrefixes(self, s: str) -> int:
        zero, one = 0, 0
        res = 0
        for bit in s:
            if bit == '1':
                one += 1
            else:
                zero += 1

            if abs(zero - one) in [1, 0]:
                res += 1
        return res