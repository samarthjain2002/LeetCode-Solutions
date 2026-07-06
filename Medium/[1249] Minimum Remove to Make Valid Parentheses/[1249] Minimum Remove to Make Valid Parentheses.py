"""
Accepted
1249 [Medium]
Runtime: 71 ms, faster than 72.25% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
Memory Usage: 19.73 MB, less than 7.06% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        for char in s:
            if char == '(':
                res.append(char)
                count += 1
            elif char == ')' and count > 0:
                res.append(char)
                count -= 1
            elif char != ')':
                res.append(char)

        filtered = []
        for char in res[::-1]:
            if char == '(' and count > 0:
                count -= 1
            else:
                filtered.append(char)
        
        return "".join(filtered[::-1])