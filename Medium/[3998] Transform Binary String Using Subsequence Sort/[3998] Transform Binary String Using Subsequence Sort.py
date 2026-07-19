"""
Accepted
3998 [Medium]
Runtime: 562 ms, faster than 78.31% of Python3 online submissions for Transform Binary String Using Subsequence Sort.
Memory Usage: 33.48 MB, less than 32.17% of Python3 online submissions for Transform Binary String Using Subsequence Sort.
"""
class Solution:
    def transformStr(self, s: str, strs: List[str]) -> List[bool]:
        zero_count = s.count('0')
        one_count = s.count('1')

        res = []
        for i, st in enumerate(strs):
            if st.count('0') > zero_count or st.count('1') > one_count:
                res.append(False)
                continue

            req_zero = zero_count - st.count('0')
            running_one_count = 0
            for i, bit in enumerate(st):
                if s[i] == '1':
                    running_one_count += 1

                if bit == '0':
                    pass
                elif bit == '?':
                    if req_zero:
                        req_zero -= 1
                    elif running_one_count == 0:
                        res.append(False)
                        break
                    else:
                        running_one_count -= 1
                elif bit == '1':
                    if running_one_count == 0:
                        res.append(False)
                        break
                    else:
                        running_one_count -= 1
            else:
                res.append(True)

        return res