"""
Accepted
3310 [Medium]
Runtime: 597 ms, faster than 17.42% of Python3 online submissions for Remove Methods From Project.
Memory Usage: 166.95 MB, less than 14.39% of Python3 online submissions for Remove Methods From Project.
"""
# Depth-First Search + Union-Find Solution
# TC: O((V+E) α(V)), SC: O(V+E)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
        self.remove = [False] * n

    def find(self, node):
        while node != self.par[node]:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return node

    def union(self, node1, node2):
        par1, par2 = self.find(node1), self.find(node2)
        if par1 == par2:
            return

        if self.rank[par1] > self.rank[par2]:
            self.par[par2] = par1
        elif self.rank[par1] < self.rank[par2]:
            self.par[par1] = par2
        else:
            self.par[par2] = par1
            self.rank[par1] += 1


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        uf = UnionFind(n)

        sus = set([k])
        edgeMap = defaultdict(list)
        for a, b in invocations:
            edgeMap[a].append(b)

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            sus.add(node)

            uf.remove[node] = True

            for nei in edgeMap[node]:
                uf.union(node, nei)
                dfs(nei)

        dfs(k)

        for a, b in invocations:
            if a not in sus and b in sus:
                uf.remove[uf.find(b)] = False

        res = []
        for i in range(n):
            if not uf.remove[uf.find(i)]:
                res.append(i)
        return res