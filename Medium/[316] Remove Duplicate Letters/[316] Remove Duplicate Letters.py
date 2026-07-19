"""
Accepted
316 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Remove Duplicate Letters.
Memory Usage: 19.28 MB, less than 81.44% of Python3 online submissions for Remove Duplicate Letters.
"""
# Greedy + Monotonic Stack Solution
# TC: O(n), SC: O(1)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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