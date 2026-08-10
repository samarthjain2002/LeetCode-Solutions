"""
Accepted
1510 [Hard]
Runtime: 700 ms, faster than 45.46% of Python3 online submissions for Stone Game IV.
Memory Usage: 19.90 MB, less than 96.67% of Python3 online submissions for Stone Game IV.
"""
# Bottom-up Dynamic Programming + Memoization Solution
# TC: O(n*sqrt(n)), SC: O(n)
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        dp[0] = False

        for stones in range(1, n + 1):
            i = 1
            while stones - i * i >= 0:
                if not dp[stones - i * i]:
                    dp[stones] = True
                    break
                i += 1
            else: 
                dp[stones] = False

        return dp[n]



"""
Runtime: 1865 ms, faster than 15.46% of Python3 online submissions for Stone Game IV.
Memory Usage: 50.31 MB, less than 26.36% of Python3 online submissions for Stone Game IV.
"""
# Top-down Dynamic Programming + Memoization Solution
# TC: O(n*sqrt(n)), SC: O(n)
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        cache = {}
        def rec(n):
            if n == 0:
                return False

            if n in cache:
                return cache[n]

            i = 1
            while i * i <= n:
                # If the opponent cannot force a win, I win
                if not rec(n - i**2):
                    cache[n] = True
                    return True
                i += 1
            
            cache[n] = False
            return False

        return rec(n)