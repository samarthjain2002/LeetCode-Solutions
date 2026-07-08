"""
Accepted
3756 [Medium]
Runtime: 554 ms, faster than 27.16% of Python3 online submissions for Concatenate Non-Zero Digits and Multiply by Sum II.
Memory Usage: 57.78 MB less than 23.46% of Python3 online submissions for Concatenate Non-Zero Digits and Multiply by Sum II.
"""
# Math + Prefix Solution
# TC: O(n + q), SC: O(n)
class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        q = len(queries)
        MOD = 10**9 + 7

        prefixDigits = [0] * n
        prefixSum = [0] * n
        digitCount = [0] * n
        pow10 = [0] * (n + 1)

        prefixDigits[0] = int(s[0])
        prefixSum[0] = int(s[0])
        digitCount[0] = 0 if s[0] == '0' else 1
        pow10[0] = 1
        for i in range(1, n):
            prefixDigits[i] = (prefixDigits[i - 1] * 10 + int(s[i])) % MOD if s[i] != '0' else prefixDigits[i - 1]
            prefixSum[i] = prefixSum[i - 1] + int(s[i])
            digitCount[i] = digitCount[i - 1] + (0 if s[i] == '0' else 1)
            pow10[i] = (pow10[i - 1] * 10) % MOD
        pow10[n] = (pow10[n - 1] * 10) % MOD
        
        res = [0] * q
        for i in range(q):
            left, right = queries[i]
            S = prefixSum[right] - (prefixSum[left - 1] if left > 0 else 0)

            prevDigits = prefixDigits[left - 1] if left > 0 else 0
            k = digitCount[right] - (digitCount[left - 1] if left > 0 else 0)
            x = (prefixDigits[right] - (prevDigits * pow10[k])) % MOD

            res[i] = (x * S) % MOD
        return res