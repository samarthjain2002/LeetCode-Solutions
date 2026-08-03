"""
Accepted
4009 [Hard]
Runtime: 271 ms, faster than 50.00% of Python3 online submissions for Minimum Possible Maximum Waiting Time.
Memory Usage: 99.17 MB, less than -% of Python3 online submissions for Minimum Possible Maximum Waiting Time.
"""
# Top-down Dynamic Programming + Memoization
# TC: O(n.F^2.S^2), SC: O(n.F^2.S^2)  
class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        n = len(demand)

        if fuel[0] < demand[0] and fuel[1] < demand[0]:
            return -1

        cache = {}
        def rec(i, f1, f2, wt1, wt2):
            if i == n:
                return (0, 0)

            if (i, f1, f2, wt1, wt2) in cache:
                return cache[(i, f1, f2, wt1, wt2)]

            served1 = served2 = w1 = w2 = 0
            if demand[i] <= f1:
                served1, w1 = rec(i + 1, f1 - demand[i], f2, demand[i], max(0, wt2 - wt1))
                w1 = max(wt1, w1)
                served1 += 1
            if demand[i] <= f2:
                served2, w2 = rec(i + 1, f1, f2 - demand[i], max(0, wt1 - wt2), demand[i])
                w2 = max(wt2, w2)
                served2 += 1

            if served1 > served2:
                cache[(i, f1, f2, wt1, wt2)] = (served1, w1)
            elif served1 < served2:
                cache[(i, f1, f2, wt1, wt2)] = (served2, w2)
            else:
                cache[(i, f1, f2, wt1, wt2)] = (served1, min(w1, w2))

            return cache[(i, f1, f2, wt1, wt2)]

        cars_served, minimized_max_wait_time = rec(0, fuel[0], fuel[1], 0, 0)
        return minimized_max_wait_time