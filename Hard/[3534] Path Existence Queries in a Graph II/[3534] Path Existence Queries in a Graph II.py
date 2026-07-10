"""
Accepted
3534 [Hard]
Runtime: 2629 ms, faster than 13.63% of Python3 online submissions for Path Existence Queries in a Graph II.
Memory Usage: 85.57 MB, less than 57.57% of Python3 online submissions for Path Existence Queries in a Graph II.
"""
# Sorting + Binary Search + Binary Lifting/Jumping Solution
# TC: O(nlog(n) + qlog(n)), SC: O(nlog(n))
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_nums = sorted([(num, i) for i, num in enumerate(nums)])

        num_index = [0] * n
        for idx, (num, i) in enumerate(sorted_nums):
            num_index[i] = idx

        def binary_search(val):
            low, high = 0, n
            while low < high:
                mid = low + ((high - low) // 2)
                if sorted_nums[mid][0] <= val:
                    low = mid + 1
                else:
                    high = mid
            return low - 1

        ROWS, COLS = n, n.bit_length()
        jump_table = [[0] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            farthest_one_hop = binary_search(nums[i] + maxDiff)
            jump_table[i][0] = sorted_nums[farthest_one_hop][1]

        for j in range(1, COLS):
            for i in range(ROWS):
                jump_table[i][j] = jump_table[jump_table[i][j - 1]][j - 1]

        res = [0] * len(queries)
        for i in range(len(queries)):
            u, v = queries[i]
            if num_index[u] > num_index[v]:
                u, v = v, u

            if u == v:
                res[i] = 0
                continue

            ans = 0
            for j in range(COLS - 1, -1, -1):
                nxt = jump_table[u][j]

                if num_index[nxt] < num_index[v]:
                    u = nxt
                    ans += 1 << j

            # now u is the furthest node still before v
            if num_index[jump_table[u][0]] >= num_index[v]:
                res[i] = ans + 1
            else:
                res[i] = -1

        return res