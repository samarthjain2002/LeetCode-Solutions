"""
Accepted
3499 [Medium]
Runtime: 714 ms, faster than 50.47% of Python3 online submissions for Maximize Active Section with Trade I.
Memory Usage: 20.65 MB, less than 78.50% of Python3 online submissions for Maximize Active Section with Trade I.
"""
# TC: O(n), SC: O(1)
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        ones = s.count('1')
        res = ones

        i = 0
        prev_zero = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
                
            if s[i] == '0':
                if prev_zero > 0:
                    gain = prev_zero + j - i
                    res = max(res, ones + gain)
                prev_zero = j - i

            i = j

        return res



"""
Runtime: 656 ms, faster than 61.82% of Python3 online submissions for Maximize Active Section with Trade I.
Memory Usage: 21.11 MB, less than 55.45% of Python3 online submissions for Maximize Active Section with Trade I.
"""
# TC: O(n), SC: O(n)
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        ones = s.count('1')

        i = 0
        zero_blocks = []
        while i < n:
            # Start of a 1-block
            while i < n and s[i] == '1':
                i += 1

            j = i
            # Start of a 0-block
            while j < n and s[j] == '0':
                j += 1

            # Append only if 0-block is encountered
            if i < n and s[i] == '0':
                zero_blocks.append(j - i)
                
            i = j
            
        res = ones
        for i in range(1, len(zero_blocks)):
            res = max(res, zero_blocks[i - 1] + zero_blocks[i] + ones)
        return res



"""
Runtime: 993 ms, faster than 30.84% of Python3 online submissions for Maximize Active Section with Trade I.
Memory Usage: 27.66 MB, less than 9.35% of Python3 online submissions for Maximize Active Section with Trade I.
"""
# TC: O(n), SC: O(n)
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        ones = s.count('1')
        res = ones

        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            runs.append((s[i], j - i))
            i = j

        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1':
                gain = runs[i - 1][1] + runs[i + 1][1]
                res = max(res, gain + ones)
        return res



"""
Runtime: 2151 ms, faster than 5.61% of Python3 online submissions for Maximize Active Section with Trade I.
Memory Usage: 364.34 MB, less than 5.61% of Python3 online submissions for Maximize Active Section with Trade I.
"""
# TC: O(n), SC: O(n)
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        res = s.count('1')
        if '0' not in s:
            return res

        prefixSum = [0] * n
        prefixSum[0] = int(s[0])
        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + int(s[i])

        left = s.index('0')
        s += '1'

        def solve(pos):
            nonlocal res

            flag_zero = flag_one = False
            for i in range(pos, n + 1):
                if s[i] == '0':
                    if flag_one:
                        if not flag_zero:
                            solve(i)
                        flag_zero = True
                else:
                    if not flag_one:
                        flag_one = True
                    elif flag_zero:
                        prev_window = prefixSum[pos - 1] if pos > 0 else 0
                        nxt_window = prefixSum[-1] - prefixSum[i - 1] if i < n else 0
                        cur = prev_window + (i - pos) + nxt_window
                        res = max(res, cur)
                        return

        solve(left)

        return res