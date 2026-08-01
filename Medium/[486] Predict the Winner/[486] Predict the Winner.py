"""
Accepted
486 [Medium]
Runtime: 3032 ms, faster than 5.04% of Python3 online submissions for Predict The Winner.
Memory Usage: 19.61 MB, less than 36.36% of Python3 online submissions for Predict The Winner.
"""
# Dynamic Programming + Memoization Solution
# TC: O(n^2), SC:O(n^2)
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        cache = {}

        def rec(left, right):
            # No moves left to be made
            if left > right:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            p1_ch1 = nums[left]
            # Player 2 chooses if there is at least one move left
            if left < right:
                p2_ch1 = -nums[left + 1] + rec(left + 2, right)
                p2_ch2 = -nums[right] + rec(left + 1, right - 1)
                # Player 2 plays it optimally so that player 1's next choice is minimal
                p1_ch1 += min(p2_ch1, p2_ch2)

            p1_ch2 = nums[right]
            # Player 2 chooses if there is at least one move left
            if left + 1 <= right:
                p2_ch1 = -nums[left] + rec(left + 1, right - 1)
                p2_ch2 = -nums[right - 1] + rec(left, right - 2)
                p1_ch2 += min(p2_ch1, p2_ch2)

            cache[(left, right)] = max(p1_ch1, p1_ch2)
            return cache[(left, right)]

        # Player 2's score is deducted from player 1's score
        return rec(0, len(nums) - 1) >= 0



"""
Runtime: 3032 ms, faster than 5.04% of Python3 online submissions for Predict The Winner.
Memory Usage: 19.28 MB, less than 79.49% of Python3 online submissions for Predict The Winner.
"""
# Recursion Solution
# TC: O(2^n), SC: O(n)
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def rec(left, right):
            if left > right:
                return 0

            p1_ch1 = nums[left]
            if left + 1 <= right:
                p2_ch1 = -nums[left + 1] + rec(left + 2, right)
                p2_ch2 = -nums[right] + rec(left + 1, right - 1)
                p1_ch1 += min(p2_ch1, p2_ch2)

            p1_ch2 = nums[right]
            if left + 1 <= right:
                p2_ch1 = -nums[left] + rec(left + 1, right - 1)
                p2_ch2 = -nums[right - 1] + rec(left, right - 2)
                p1_ch2 += min(p2_ch1, p2_ch2)

            return max(p1_ch1, p1_ch2)

        return rec(0, len(nums) - 1) >= 0