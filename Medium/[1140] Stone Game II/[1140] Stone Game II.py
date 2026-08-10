"""
Accepted
1140 [Medium]
Runtime: 425 ms, faster than 25.08% of Python3 online submissions for Stone Game II.
Memory Usage: 34.05 MB, less than 15.45% of Python3 online submissions for Stone Game II.
"""
# Top-down Dynamic Programming + Memoization Solution
# TC: O(n^3), SC: O(n^2)
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        cache = {}
        def rec(i, M, Alice):
            if i == n:
                return 0

            if (i, M, Alice) in cache:
                return cache[(i, M, Alice)]

            total = 0
            res = 0 if Alice else float("inf")
            for X in range(1, 2*M + 1):
                if i + X - 1 == n:
                    break

                total += piles[i + X - 1]
                if Alice:
                    res = max(res, total + rec(i + X, max(M, X), False))
                else:
                    res = min(res, rec(i + X, max(M, X), True))

            cache[(i, M, Alice)] = res
            return res

        return rec(0, 1, True)