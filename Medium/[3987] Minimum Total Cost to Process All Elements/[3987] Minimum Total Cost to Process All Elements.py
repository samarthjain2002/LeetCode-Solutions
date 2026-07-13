"""
Accepted
3987 [Medium]
Runtime: 14 ms, faster than 100.00% of Python3 online submissions for Minimum Total Cost to Process All Elements.
Memory Usage: 33.72 MB less than -% of Python3 online submissions for Minimum Total Cost to Process All Elements.
"""
class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        
        total = sum(nums)
        req = total - k
        ops = ceil(req / k)
        
        return (ops * (ops + 1) // 2) % MOD