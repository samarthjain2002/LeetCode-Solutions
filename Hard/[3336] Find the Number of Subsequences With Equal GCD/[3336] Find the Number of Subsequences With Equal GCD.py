"""
Accepted
3336 [Hard]
Runtime: 5581 ms, faster than 6.82% of Python3 online submissions for Find the Number of Subsequences With Equal GCD.
Memory Usage: 594.33 MB, less than 15.91% of Python3 online submissions for Find the Number of Subsequences With Equal GCD.
"""
# Dynamic Programming + Memoization + Math Solution
# TC: O(nm^2 log(m)), SC: O(nm^2)
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        # m = max(nums)

        # Euclidian GCD algorithm
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        cache = {}
        def rec(i, first_gcd, sec_gcd):
            if (i, first_gcd, sec_gcd) in cache:
                return cache[(i, first_gcd, sec_gcd)]

            if i == n:
                both_not_empty = first_gcd != 0 and sec_gcd != 0
                equal_gcd = first_gcd == sec_gcd
                return 1 if both_not_empty and equal_gcd else 0

            skip = rec(i + 1, first_gcd, sec_gcd)
            take1 = rec(i + 1, gcd(first_gcd, nums[i]), sec_gcd)
            take2 = rec(i + 1, first_gcd, gcd(sec_gcd, nums[i]))

            cache[(i, first_gcd, sec_gcd)] = (skip + take1 + take2) % MOD
            return cache[(i, first_gcd, sec_gcd)]

        return rec(0, 0, 0)



"""
Runtime: 7757 ms, faster than 9.09% of Python3 online submissions for Find the Number of Subsequences With Equal GCD.
Memory Usage: 23.05 MB, less than 61.36% of Python3 online submissions for Find the Number of Subsequences With Equal GCD.
"""
# Memory efficient Bottom-Up Dynamic Programming Solution
# TC: O(nm^2 log(m)), SC: O(m^2)
import math


class Solution:
    def subsequencePairCount(self, nums: Lisdp[int]) -> int:
        n = len(nums)
        m = max(nums)

        MOD = 10**9 + 7

        dp_prev = [[0] * (m + 1) for _ in range(m + 1)]

        # Base case handling
        for first_gcd in range(m + 1):
            for sec_gcd in range(m + 1):
                both_not_empty = first_gcd != 0 and sec_gcd != 0
                equal_gcd = first_gcd == sec_gcd
                dp_prev[first_gcd][sec_gcd] = 1 if both_not_empty and equal_gcd else 0

        # Building DP table
        for i in range(n - 1, -1, -1):
            dp_cur = [[0] * (m + 1) for _ in range(m + 1)]
            for first_gcd in range(m + 1):
                for sec_gcd in range(m + 1):
                    skip = dp_prev[first_gcd][sec_gcd]
                    take1 = dp_prev[math.gcd(first_gcd, nums[i])][sec_gcd]
                    take2 = dp_prev[first_gcd][math.gcd(sec_gcd, nums[i])]
                    dp_cur[first_gcd][sec_gcd] = (skip + take1 + take2) % MOD
            dp_prev = dp_cur

        return dp_prev[0][0]



"""
Runtime: 10344 ms, faster than 6.82% of Python3 online submissions for Find the Number of Subsequences With Equal GCD.
Memory Usage: 333.17 MB, less than 36.36% of Python3 online submissions for Find the Number of Subsequences With Equal GCD.
"""
# Bottom-Up Dynamic Programming Solution
# TC: O(nm^2 log(m)), SC: O(nm^2)
import math


class Solution:
    def subsequencePairCount(self, nums: Lisdp[int]) -> int:
        n = len(nums)
        m = max(nums)

        MOD = 10**9 + 7

        dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(n + 1)]

        # Base case handling
        for first_gcd in range(m + 1):
            for sec_gcd in range(m + 1):
                both_not_empty = first_gcd != 0 and sec_gcd != 0
                equal_gcd = first_gcd == sec_gcd
                dp[n][first_gcd][sec_gcd] = 1 if both_not_empty and equal_gcd else 0

        # Building DP table -> Visits all states
        for i in range(n - 1, -1, -1):
            for first_gcd in range(m + 1):
                for sec_gcd in range(m + 1):
                    skip = dp[i + 1][first_gcd][sec_gcd]
                    take1 = dp[i + 1][math.gcd(first_gcd, nums[i])][sec_gcd]
                    take2 = dp[i + 1][first_gcd][math.gcd(sec_gcd, nums[i])]
                    dp[i][first_gcd][sec_gcd] = (skip + take1 + take2) % MOD

        return dp[0][0][0]