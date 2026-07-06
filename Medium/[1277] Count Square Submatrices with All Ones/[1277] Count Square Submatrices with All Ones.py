"""
Accepted
1277 [Medium]
Runtime: 67 ms, faster than 44.93% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage: 19.19 MB, less than 23.45% of Python3 online submissions for Count Square Submatrices with All Ones.
"""
# Dynamic Programming solution
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, -1, -1):
                if row == ROWS - 1 or col == COLS - 1:
                    pass
                elif matrix[row][col] == 1:
                    matrix[row][col] = 1 + min(
                        matrix[row + 1][col],
                        matrix[row][col + 1],
                        matrix[row + 1][col + 1]
                    )

        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res += matrix[row][col]
        return res
    


"""
Runtime: 191 ms, faster than 17.39% of Python3 online submissions for Count Square Submatrices with All Ones.
Memory Usage:  37.34 MB, less than 5.14% of Python3 online submissions for Count Square Submatrices with All Ones.
"""
# Depth-First Search Recursion, Memoization solution
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}

        def dfs(row, col):
            if row == ROWS or col == COLS or not matrix[row][col]:
                return 0

            if (row, col) in cache:
                return cache[(row, col)]

            cache[(row, col)] = 1 + min(
                dfs(row + 1, col),
                dfs(row, col + 1),
                dfs(row + 1, col + 1)
            )

            return cache[(row, col)]
        
        res = 0
        for row in range(ROWS):
            for col in range(COLS):
                res += dfs(row, col)
        return res