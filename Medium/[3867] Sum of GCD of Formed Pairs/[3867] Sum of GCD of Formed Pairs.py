"""
Accepted
3849 [Medium]
Runtime: 194 ms, faster than 63.47% of Python3 online submissions for Maximum Bitwise XOR After Rearrangement.
Memory Usage: 33.79 MB less than 44.91% of Python3 online submissions for Maximum Bitwise XOR After Rearrangement.
"""
# Simulation Solution
# TC: O(nlog(n) + nlog(m)), SC: O(n)
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        # m = max(nums)

        prefixGCD = [0] * n
        mx = nums[0]
        for i in range(n):
            mx = max(mx, nums[i])
            prefixGCD[i] = gcd(nums[i], mx)

        prefixGCD.sort()

        left, right = 0, n - 1
        res = 0
        while left < right:
            res += gcd(prefixGCD[left], prefixGCD[right])
            left, right = left + 1, right - 1
        return res