"""
Accepted
3517 [Medium]
Runtime: 618 ms, faster than 8.76% of Python3 online submissions for Smallest Palindromic Rearrangement I.
Memory Usage: 21.64 MB, less than 16.13% of Python3 online submissions for Smallest Palindromic Rearrangement I.
"""
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        freq = Counter(s)

        res = [0] * len(s)
        i = 0
        for char in string.ascii_lowercase:
            while freq[char] > 1:
                res[i] = res[-1 - i] = char
                freq[char] -= 2
                i += 1
            if freq[char] == 1:
                res[n // 2] = char
        return "".join(res)