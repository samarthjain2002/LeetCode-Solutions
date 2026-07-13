"""
Accepted
1291 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Sequential Digits.
Memory Usage: 19.12 MB, less than 88.24% of Python3 online submissions for Sequential Digits.
"""
# Sliding Window Solution
# TC: O(1), SC: O(1)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        M, N = len(str(low)), len(str(high))

        for i in range(M, N + 1):
            for j in range(0, 9 - i + 1):
                sub_string = s[j : j + i]
                sub_string_int = int(sub_string)
                if low <= sub_string_int <= high:
                    res.append(sub_string_int)
        return res



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Sequential Digits.
Memory Usage: 19.38 MB, less than 30.59% of Python3 online submissions for Sequential Digits.
"""
# Recursion + Sorting Solution
# TC: O(1), SC: O(1)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        def rec(s):
            if not s:
                for dig in "12345678":
                    rec(dig)
                return
                
            if int(s) > high:
                return

            if low <= int(s):
                res.append(int(s))

            dig = s[-1]
            if dig != '9':
                rec(s + str(int(dig) + 1))

        rec("")
        return sorted(res)