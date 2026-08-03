"""
Accepted
1406 [Hard]
Runtime: 394 ms, faster than 95.46% of Python3 online submissions for Stone Game III.
Memory Usage: 23.99 MB, less than 71.59% of Python3 online submissions for Stone Game III.
"""
# Dynamic Programming + Memoization Solution
# TC: O(n), SC: O(1)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp = [0] * (3 + 1)
        for i in range(n - 1, -1, -1):
            dp[0] = stoneValue[i] - dp[1]
            if i + 1 < n:
                dp[0] = max(
                    dp[0], 
                    stoneValue[i] + stoneValue[i + 1] - dp[2]
                )
            if i + 2 < n:
                dp[0] = max(
                    dp[0], 
                    stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[3]
                )

            dp[1], dp[2], dp[3] = dp[0], dp[1], dp[2]

        score = dp[1]
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"



"""
Runtime: 427 ms, faster than 93.51% of Python3 online submissions for Stone Game III.
Memory Usage: 23.82 MB, less than 88.31% of Python3 online submissions for Stone Game III.
"""
# Dynamic Programming + Memoization Solution
# TC: O(n), SC: O(n)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = stoneValue[i] - dp[i + 1]
            if i + 1 < n:
                dp[i] = max(
                    dp[i], 
                    stoneValue[i] + stoneValue[i + 1] - dp[i + 2]
                )
            if i + 2 < n:
                dp[i] = max(
                    dp[i], 
                    stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - dp[i + 3]
                )

        score = dp[0]
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"



"""
Runtime: 895 ms, faster than 52.12% of Python3 online submissions for Stone Game III.
Memory Usage: 161.96 MB, less than 37.34% of Python3 online submissions for Stone Game III.
"""
# Recursion + Dynamic Programming + Memoization Solution
# TC: O(n), SC: O(n)
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        print(n)

        cache = {}
        def rec(i):
            if i == n:
                return 0

            if i in cache:
                return cache[i]

            take1 = stoneValue[i] - rec(i + 1)
            take2 = take3 = -inf
            if i + 1 < n:
                take2 = stoneValue[i] + stoneValue[i + 1] - rec(i + 2)
            if i + 2 < n:
                take3 = stoneValue[i] + stoneValue[i + 1] + stoneValue[i + 2] - rec(i + 3)
            
            cache[i] = max(take1, take2, take3)
            return cache[i]

        score = rec(0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"