"""
Accepted
1260 [Easy]
Runtime: 11 ms, faster than 39.09% of Python3 online submissions for Shift 2D Grid.
Memory Usage: 19.61 MB, less than 48.15% of Python3 online submissions for Shift 2D Grid.
"""
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                k = k % (m * n)

                cell = i * n + j
                target_cell = (cell + k) % (m * n)

                res[target_cell // n][target_cell % n] = grid[i][j]

        return res