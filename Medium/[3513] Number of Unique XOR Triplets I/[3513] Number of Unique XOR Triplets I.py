"""
Accepted
3513 [Medium]
Runtime: 4 ms, faster than 14.29% of Python3 online submissions for Number of Unique XOR Triplets I.
Memory Usage: 34.01 MB, less than 25.40% of Python3 online submissions for Number of Unique XOR Triplets I.
"""
# Bit-Manipulation Solution
# TC: O(1), SC: O(1)
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1    # [1]
        elif n == 2:
            return 2    # [1,2]
        else:
            return 2**((len(bin(n)) - 3) + 1)   # Range [0, 2^(msb(n) + 1) - 1]