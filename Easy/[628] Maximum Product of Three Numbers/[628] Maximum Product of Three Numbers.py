"""
Accepted
628 [Easy]
Runtime: 12 ms, faster than 83.06% of Python3 online submissions for Maximum Product of Three Numbers.
Memory Usage: 20.47 MB, less than 17.11% of Python3 online submissions for Maximum Product of Three Numbers.
"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        a = nums[-1] * nums[-2] * nums[-3]
        b = nums[0] * nums[1] * nums[-1]

        return max(a, b)