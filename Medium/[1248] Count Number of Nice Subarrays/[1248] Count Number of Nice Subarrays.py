"""
Accepted
1248 [Medium]
Runtime: 578 ms, faster than 83.66% of Python3 online submissions for Count Number of Nice Subarrays.
Memory Usage: 23.65 MB, less than 42.15% of Python3 online submissions for Count Number of Nice Subarrays.
"""
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        oddCount = 0
        left, middle = 0, 0
        res = 0
        for right in range(N):
            if nums[right] % 2 != 0:
                oddCount += 1
            while oddCount == k + 1:
                if nums[left] % 2 != 0:
                    oddCount -= 1
                left += 1
                middle = left
            if oddCount == k:
                while nums[middle] % 2 == 0:
                    middle += 1
                res += middle - left + 1
        return res