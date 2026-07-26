"""
Accepted
4003 [Hard]
Runtime: 6383 ms, faster than 5.08% of Python3 online submissions for Minimum Cost Path with Alternating Directions III.
Memory Usage: 69.82 MB, less than 18.77% of Python3 online submissions for Minimum Cost Path with Alternating Directions III.
"""
# Dijkstra's Algorithm Solution
# TC: O(mnlog(mn)), SC: O(mn)
class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        minHeap = [(1, 0, 0, 0)]     # cost, parity, row, col
        visited = set()              # (row, col, parity)
        while minHeap:
            cost, par, r, c = heapq.heappop(minHeap)

            if r == m - 1 and c == n - 1:
                return cost

            if (r, c, par) in visited:
                continue
            visited.add((r, c, par))

            # Next move's parity
            par = (par + 1) % 2
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    # Entrance cost
                    new_cost = (nr + 1) * (nc + 1)

                    # Violation of parity rule
                    if dr + dc > 0 and par == 0:
                        new_cost += penalty[r][c]
                    elif dr + dc < 0 and par == 1:
                        new_cost += penalty[r][c]

                    heapq.heappush(minHeap, (cost + new_cost, par, nr, nc))

            # Wait in cell and attract penalty
            heapq.heappush(minHeap, (cost + penalty[r][c], par, r, c))