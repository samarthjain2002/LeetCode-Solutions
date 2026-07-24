"""
Accepted
3514 [Medium]
Runtime: 9246 ms, faster than 25.92% of Python3 online submissions for Number of Unique XOR Triplets II.
Memory Usage: 19.69 MB, less than 46.30% of Python3 online submissions for Number of Unique XOR Triplets II.
"""
# Bit-Manipulation Solution
# TC: O(n^2 + nm), SC: O(m)
class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        # m = max(nums)
        
        xor_doublets = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                xor_doublets.add(nums[i] ^ nums[j])

        xor_triplets = set()
        for i in range(len(nums)):
            for xor in xor_doublets:
                xor_triplets.add(nums[i] ^ xor)

        return len(xor_triplets)