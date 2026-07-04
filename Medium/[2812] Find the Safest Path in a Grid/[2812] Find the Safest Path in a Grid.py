"""
Accepted
2812 [Medium]
Runtime: 3729 ms, faster than 36.76% of Python3 online submissions for Find the Safest Path in a Grid.
Memory Usage: 56.88 MB, less than 9.49% of Python3 online submissions for Find the Safest Path in a Grid.
"""
# Multi-source BFS + Sorting + Union-Find Solution
# TC: O(n^2.log(n)), SC: O(n^2)
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]      # Path halving
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return

        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.parent[par1] = par2
        else:
            self.parent[par2] = par1
            self.rank[par1] += 1


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Multi-source Breadth-First Search
        queue = deque([(row, col, 0) for row in range(n) for col in range(n) if grid[row][col]])
        man_dist = {}
        while queue:
            r, c, dist = queue.popleft()

            if (r, c) in man_dist:
                continue
            man_dist[(r, c)] = dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in man_dist:
                    queue.append((nr, nc, dist + 1))

        # Active greedily cells with highest manhattan distance
        cells = sorted(man_dist, key=man_dist.get, reverse=True)

        active = [[False] * n for _ in range(n)]
        uf = UnionFind(n*n)

        for r, c in cells:
            active[r][c] = True
            node = r * n + c

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and active[nr][nc]:
                    uf.union(node, nr * n + nc)

            if uf.find(0) == uf.find(n * n - 1):
                return man_dist[(r, c)]



"""
Runtime: 5360 ms, faster than 9.54% of Python3 online submissions for Find the Safest Path in a Grid.
Memory Usage: 77.23 MB, less than 5.20% of Python3 online submissions for Find the Safest Path in a Grid.
"""
# Multi-source Breadth-First Search + Dijkstra's Solution
# TC: O(n^2 log(n)), SC: O(n^2)
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Multi-source Breadth-First Search
        queue = deque([(row, col, 0) for row in range(n) for col in range(n) if grid[row][col]])
        man_dist = {}
        while queue:
            for i in range(len(queue)):
                x, y, dist = queue.popleft()
                if (x, y) in man_dist:
                    continue
                
                man_dist[(x, y)] = dist
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in man_dist:
                        queue.append((nx, ny, dist + 1))

        # Dijkstra's algorithm
        maxHeap = [(-man_dist[(0, 0)], 0, 0)]
        visited = set()
        while maxHeap:
            safeness, r, c = heapq.heappop(maxHeap)
            if r == c == n - 1:
                return -safeness

            if (r, c) in visited:
                continue
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    # Multiply by -1 to trick the minHeap into working like a maxHeap
                    new_safeness = -1 * (min(-1 * safeness, man_dist[(nr, nc)]))
                    heapq.heappush(maxHeap, (new_safeness, nr, nc))



"""
Runtime: 7596 ms, faster than 5.23% of Python3 online submissions for Find the Safest Path in a Grid.
Memory Usage: 41.63 MB, less than 51.16% of Python3 online submissions for Find the Safest Path in a Grid.
"""
# Multi-source BFS + Binary Search on Answer + Union-Find Solution
# TC: O(n^2 log(n)), SC: O(n^2)
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]      # Path halving
            node = self.parent[node]
        return self.parent[node]

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return

        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        elif self.rank[par2] > self.rank[par1]:
            self.parent[par1] = par2
        else:
            self.parent[par2] = par1
            self.rank[par1] += 1


class Solution:
    def isPossible(self, safeness, n, man_dist):
        uf = UnionFind(n*n)

        directions = [(1, 0), (0, 1)]   # Enough for adjacent nodes

        for r in range(n):
            for c in range(n):
                if man_dist[r][c] < safeness:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and man_dist[nr][nc] >= safeness:
                        uf.union(r * n + c, nr * n + nc)

        return uf.find(0) == uf.find(n * n - 1)
        
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        # Multi-source Breadth-First Search
        queue = deque([(row, col, 0) for row in range(n) for col in range(n) if grid[row][col]])
        man_dist = [[-1] * n for _ in range(n)]
        while queue:
            r, c, dist = queue.popleft()

            if man_dist[r][c] != -1:
                continue
            
            man_dist[r][c] = dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and man_dist[nr][nc] == -1:
                    queue.append((nr, nc, dist + 1))

        # Binary Search on Answer
        low, high = 0, max(map(max, man_dist))
        res = 0
        while low <= high:
            mid = low + ((high - low) // 2)
            if self.isPossible(mid, n, man_dist):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res