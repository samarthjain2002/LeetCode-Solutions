"""
Accepted
4001 [Medium]
Runtime: 137 ms, faster than 71.21% of Python3 online submissions for Aggregate Two Time Series.
Memory Usage: 67.90 MB, less than 54.18% of Python3 online submissions for Aggregate Two Time Series.
"""
class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        m, n = len(series1), len(series2)

        left = right = 0
        agg_series = []
        while left < m and right < n:
            if series1[left][0] < series2[right][0]:
                agg_series.append([series1[left][0], series1[left][1] + series2[right][1]])
                left += 1
            elif series1[left][0] > series2[right][0]:
                agg_series.append([series2[right][0], series2[right][1] + series1[left][1]])
                right += 1
            else:
                agg_series.append([series1[left][0], series1[left][1] + series2[right][1]])
                left, right = left + 1, right + 1

        while left < m:
            agg_series.append(series1[left])
            left += 1
        while right < n:
            agg_series.append(series2[right])
            right += 1

        return agg_series