"""
Accepted
3986 [Medium]
Runtime: 6 ms, faster than -% of Python3 online submissions for Number of Elapsed Seconds Between Two Times.
Memory Usage: 19.44 MB less than -% of Python3 online submissions for Number of Elapsed Seconds Between Two Times.
"""
class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        startTime = [int(s) for s in startTime.split(':')]
        endTime = [int(s) for s in endTime.split(':')]

        start_in_sec = (startTime[0] * 60 * 60) + (startTime[1] * 60) + startTime[2]
        end_in_sec = (endTime[0] * 60 * 60) + (endTime[1] * 60) + endTime[2]

        return end_in_sec - start_in_sec