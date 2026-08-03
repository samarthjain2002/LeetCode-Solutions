"""
Accepted
4007 [Medium]
Runtime: 19.05 ms, faster than 100.00% of Python3 online submissions for Widest Possible Fence.
Memory Usage: 75.73 MB, less than -% of Python3 online submissions for Widest Possible Fence.
"""
# Hash Table Solution
# TC: O(n^2), SC: O(n^2)
class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        freq = Counter(planks)
        vals = list(freq.keys())    # Unique single plank heights

        # Height of plank pairs
        pairs = defaultdict(int)
        for i in range(len(vals)):
            for j in range(i, len(vals)):
                h = vals[i] + vals[j]
                if i == j:
                    pairs[h] += freq[vals[i]] // 2
                else:
                    pairs[h] += min(freq[vals[i]], freq[vals[j]])

        res = 0
        for h, width in freq.items():
            res = max(res, width)

        # Width of plank fence with pairs that add up to height
        for h, width in pairs.items():
            res = max(res, width + freq[h])

        return res