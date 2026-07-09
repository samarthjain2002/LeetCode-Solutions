"""
Accepted
3532 [Medium]
Runtime: 364 ms, faster than 13.49% of Python3 online submissions for Path Existence Queries in a Graph I.
Memory Usage: 51.13 MB, less than 26.19% of Python3 online submissions for Path Existence Queries in a Graph I.
"""
# Union-Find Solution
# TC: O(nα(n) + qα(n)), SC: O(n)
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * (10**5 + 1)

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
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        uf = UnionFind(n)

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                uf.union(i, i - 1)

        res = [False] * len(queries)
        for i in range(len(queries)):
            u, v = queries[i]
            res[i] =  uf.find(u) == uf.find(v)
        return res