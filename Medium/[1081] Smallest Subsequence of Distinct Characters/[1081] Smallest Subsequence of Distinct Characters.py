"""
Accepted
1081 [Medium]
Runtime: 4 ms, faster than 14.71% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
Memory Usage: 19.22 MB, less than 75.23% of Python3 online submissions for Smallest Subsequence of Distinct Characters.
"""
# Greedy + Monotonic Stack Solution
# TC: O(n), SC: O(1)
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        n = len(s)

        last_idx = [0] * 26
        for i, char in enumerate(s):
            last_idx[ord(char) - ord('a')] = i + 1

        taken = [False] * 26

        stack = []
        for i, char in enumerate(s):
            if taken[ord(char) - ord('a')]:
                continue

            # Append it later
            while stack and stack[-1] > char and last_idx[ord(stack[-1]) - ord('a')] > i:
                taken[ord(stack[-1]) - ord('a')] = False
                stack.pop()

            stack.append(char)
            taken[ord(char) - ord('a')] = True

        return "".join(stack)