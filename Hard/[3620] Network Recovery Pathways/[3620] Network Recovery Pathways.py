"""
Accepted
3620 [Hard]
Runtime: 792 ms, faster than 61.36% of Python3 online submissions for Network Recovery Pathways.
Memory Usage: 58.68 MB, less than 62.50% of Python3 online submissions for Network Recovery Pathways.
"""
# Binary Search on Answer + Dijkstra's Algorithm Solution
# TC: O(log(V) (V+E)log(V)), SC: O(V+E)
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        edgeMap = [[] for _ in range(n)]
        low, high = float("inf"), float("-inf")
        for edge in edges:
            u, v, cost = edge
            if online[u] and online[v]:
                edgeMap[u].append((v, cost))
                low, high = min(low, cost), max(high, cost)

        def isPossible(mid):
            minHeap = [(0, 0)]
            visited = set()
            while minHeap:
                dist, node = heapq.heappop(minHeap)
                if node in visited:
                    continue
                visited.add(node)

                if dist > k:
                    return False
                
                if node == n - 1:
                    return True

                for nei, edge_cost in edgeMap[node]:
                    if edge_cost < mid:
                        continue
                    heapq.heappush(minHeap, (dist + edge_cost, nei))
            return False

        res = -1
        while low <= high:
            mid = low + ((high - low) // 2)
            if isPossible(mid):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res