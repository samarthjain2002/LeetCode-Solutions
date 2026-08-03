"""
Accepted
4008 [Medium]
Runtime: 80 ms, faster than 100.00% of Python3 online submissions for Minimum Initial Strength to Defeat All Monsters.
Memory Usage: 48.40 MB, less than -% of Python3 online submissions for Minimum Initial Strength to Defeat All Monsters.
"""
class Solution:
    def minInitialStrength(self, monsters: list[int], boosts: list[list[int]]) -> int:
        n = len(monsters)

        boost_diff = [0] * n
        for l, r, v in boosts:
            boost_diff[l] += v
            if r + 1 < n:
                boost_diff[r + 1] -= v

        boost = 0
        req = 0
        last_req = 0
        for i, m in enumerate(monsters):
            boost += boost_diff[i]
            if boost < m:
                req = m - boost
                last_req = i

        return sum(monsters[ : last_req]) + req