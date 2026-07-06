"""
Accepted
1288 [Medium]
Runtime: 1 ms, faster than 87.99% of Python3 online submissions for Remove Covered Intervals.
Memory Usage: 19.44 MB, less than 96.95% of Python3 online submissions for Remove Covered Intervals.
"""
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        left = 0
        res = 1
        for right in range(1, len(intervals)):
            c, d = intervals[left]
            a, b = intervals[right]

            if c <= a and b <= d:
                continue
            else:
                left = right
                res += 1

        return res