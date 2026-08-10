"""
Accepted
3345 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Smallest Divisible Digit Product I.
Memory Usage: 19.18 MB, less than 95.94% of Python3 online submissions for Smallest Divisible Digit Product I.
"""
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        num = n
        while True:
            prod = 1
            for dig in str(num):
                prod *= int(dig)

            if (prod // t) * t == prod:
                return num

            num += 1