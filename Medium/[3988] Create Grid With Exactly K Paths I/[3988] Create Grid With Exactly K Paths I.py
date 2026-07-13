"""
Accepted
3988 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Create Grid With Exactly K Paths I.
Memory Usage: 19.40 MB less than 100.00% of Python3 online submissions for Create Grid With Exactly K Paths I.
"""
class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        templates = {
            1: [["."]],
            2: [["..", ".."]],
            3: [["...", "..."], ["..", "..", ".."]],
            4: [["....", "...."], ["..", "..", "..", ".."], ["..#", "...", "#.."]]
        }

        grid = [['#'] * n for _ in range(m)]
        for t in templates[k]:
            rows, cols = len(t), len(t[0])
            if rows <= m and cols <= n:

                for r in range(rows):
                    for c in range(cols):
                        grid[r][c] = t[r][c]

                for r in range(rows, m):
                    grid[r][cols - 1] = '.'
                for c in range(cols, n):
                    grid[m - 1][c] = '.'

                return ["".join(row) for row in grid]
        
        return []



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Create Grid With Exactly K Paths I.
Memory Usage: 19.37 MB less than 74.57% of Python3 online submissions for Create Grid With Exactly K Paths I.
"""
class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        if k == 1:
            for col in range(n):
                grid[0][col] = '.'
            for row in range(m):
                grid[row][-1] = '.'

        elif k == 2:
            if m == 1 or n == 1:
                return []

            for col in range(n):
                grid[0][col] = '.'
            for row in range(m):
                grid[row][-1] = '.'

            grid[1][-2] = '.'

        elif k == 3:
            if m == 1 or n == 1 or m*n <= 4:
                return []

            for col in range(n):
                grid[0][col] = '.'
            for row in range(m):
                grid[row][-1] = '.'
            
            if m >= 3:
                grid[1][-2] = grid[2][-2] = '.'
            else:
                grid[1][-2] = grid[1][-3] = '.'

        else:
            if m == 1 or n == 1 or m*n <= 6:
                return []

            if m == 2:
                for col in range(n):
                    grid[0][col] = '.'
                grid[1][-1] = grid[1][-2] = grid[1][-3] = grid[1][-4] = '.'
            elif n == 2:
                for row in range(m):
                    grid[row][1] = '.'
                grid[0][0] = grid[1][0] = grid[2][0] = grid[3][0] = '.'
            else:
                grid[0][0] = grid[0][1] = '.'
                grid[1][0] = grid[1][1] = '.'

                grid[m - 1][n - 1] = grid[m - 1][n - 2] = '.'
                grid[m - 2][n - 1] = grid[m - 2][n - 2] = '.'

                for col in range(1, n - 1):
                    grid[1][col] = '.'
                for row in range(1, m - 1):
                    grid[row][n - 2] = '.'

        return ["".join(row) for row in grid]