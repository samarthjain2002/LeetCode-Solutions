"""
Accepted
3658 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for GCD of Odd and Even Sums.
Memory Usage: 19.33 MB, less than 21.29% of Python3 online submissions for GCD of Odd and Even Sums.
"""
# Math Solution
# TC: (1), SC: O(1)
class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # gcd(n^2, n(n+1)) = n⋅gcd(n, n+1) = n
        # because consecutive numbers are alsways coprime
        return n



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for GCD of Odd and Even Sums.
Memory Usage: 19.23 MB, less than 53.03% of Python3 online submissions for GCD of Odd and Even Sums.
"""
# TC: O(log(n)), SC: O(1)
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = n * n
        sumEven = n * (n + 1)

        return self.gcd(sumOdd, sumEven)



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for GCD of Odd and Even Sums.
Memory Usage: 19.15 MB, less than 85.77% of Python3 online submissions for GCD of Odd and Even Sums.
"""
# TC: O(log(n)), SC: O(1)
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdOfOddEvenSums(self, n: int) -> int:
        maxOdd, maxEven = 2 * n - 1, 2 * n

        sumOdd = (1 + maxOdd) * n // 2
        sumEven = (2 + maxEven) * n // 2

        return self.gcd(sumOdd, sumEven)