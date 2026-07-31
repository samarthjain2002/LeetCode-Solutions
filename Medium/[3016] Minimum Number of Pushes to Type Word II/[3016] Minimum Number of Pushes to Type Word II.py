"""
Accepted
3016 [Medium]
Runtime: 97 ms, faster than 74.25% of Python3 online submissions for Minimum Number of Pushes to Type Word II.
Memory Usage: 20.03 MB, less than 48.16% of Python3 online submissions for Minimum Number of Pushes to Type Word II.
"""
# Counting + Greedy Solution
# TC: O(n), SC: O(1)
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)

        cost = 0
        unique = 0
        for letter, cnt in sorted(freq.items(), key=lambda item: item[1], reverse=True):
            unique += 1
            if unique > 24:
                cost += cnt * 4
            elif unique > 16:
                cost += cnt * 3
            elif unique > 8:
                cost += cnt * 2
            else:
                cost += cnt
        return cost