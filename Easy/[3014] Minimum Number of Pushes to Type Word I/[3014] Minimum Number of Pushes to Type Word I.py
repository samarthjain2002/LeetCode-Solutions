"""
Accepted
3014 [Easy]
Runtime: 1 ms, faster than 18.47% of Python3 online submissions for Minimum Number of Pushes to Type Word I.
Memory Usage: 19.13 MB, less than 83.76% of Python3 online submissions for Minimum Number of Pushes to Type Word I.
"""
# Greedy Solution
# TC: O(n), SC: O(1)
class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(i // 8 + 1 for i in range(len(word)))