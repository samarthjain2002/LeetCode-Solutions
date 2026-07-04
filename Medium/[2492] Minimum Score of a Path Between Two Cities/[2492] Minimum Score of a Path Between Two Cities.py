"""
Accepted
2492 [Medium]
Runtime: 118 ms, faster than 89.26% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
Memory Usage: 52.56 MB, less than 91.85% of Python3 online submissions for Minimum Score of a Path Between Two Cities.
"""
# Union-Find Solution
# TC: O(E.α(V)), SC: O(V)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.rank = [1] * (n + 1)

    def find(self, node):
        while self.par[node] != node:
            self.par[node] = self.par[self.par[node]]
            node = self.par[node]
        return self.par[node]

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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)

        for road in roads:
            a, b, dist = road
            uf.union(a, b)

        res = float("inf")
        par1 = uf.find(1)
        for road in roads:
            a, b, dist = road
            if par1 == uf.find(a):
                res = min(res, dist)
        return res