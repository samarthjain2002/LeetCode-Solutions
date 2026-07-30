"""
Accepted
3518 [Hard]
Runtime: 344 ms, faster than 76.99% of Python3 online submissions for Smallest Palindromic Rearrangement II.
Memory Usage: 19.58 MB, less than 97.35% of Python3 online submissions for Smallest Palindromic Rearrangement II.
"""
# Combinatorics + Greedy Solution
# SC: O(n), TC: O(n^2)
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)

        mid_ele = s[n // 2] if n % 2 else ''
        freq = Counter(s[ : n // 2])

        def nCr(n, r, k):
            # nCr = nC(n-r)
            r = min(r, n - r)

            prod = 1
            for i in range(1, r + 1):
                prod = prod * (n - r + i) // i      # O(log2(k))
                if prod >= k:                       # Since prod is approx doubling until it reaches >= k
                    break
            return prod

        def possible_permutations(k):
            positions = sum(freq.values())
            ways = 1
            for count in freq.values():
                if count:
                    ways *= nCr(positions, count, k)
                    if ways >= k:
                        break
                    positions -= count
            return ways

        arr = []
        for i in range(n // 2):
            for char in string.ascii_lowercase:
                if freq[char]:
                    arr.append(char)
                    freq[char] -= 1

                    ways = possible_permutations(k)
                    if k <= ways:
                        break
                    else:
                        arr.pop()
                        freq[char] += 1
                        k -= ways
            else:
                return ""

        return "".join(arr) + mid_ele + "".join(arr[::-1])



"""
Runtime: 377 ms, faster than 73.24% of Python3 online submissions for Smallest Palindromic Rearrangement II.
Memory Usage: 21.64 MB, less than 16.90% of Python3 online submissions for Smallest Palindromic Rearrangement II.
"""
# Combinatorics + Backtracking Solution
# SC: O(n), TC: O(n^2)
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)

        mid_ele = s[n // 2] if n % 2 else ''
        freq = Counter(s[ : n // 2])

        def nCr(n, r, k):
            # nCr = nC(n-r)
            r = min(r, n - r)

            prod = 1
            for i in range(1, r + 1):
                prod = prod * (n - r + i) // i
                if prod >= k:
                    break
            return prod

        def possible_permutations(k):
            positions = sum(freq.values())
            ways = 1
            for count in freq.values():
                if count:
                    ways *= nCr(positions, count, k)
                    if ways >= k:
                        break
                    positions -= count
            return ways

        def build(arr, k, n, cnt):
            if cnt == n:
                return "".join(arr) + mid_ele + "".join(arr[::-1])

            for char in string.ascii_lowercase:
                if freq[char]:
                    arr.append(char)
                    freq[char] -= 1

                    ways = possible_permutations(k)
                    if k <= ways:
                        cnt += 1
                        return build(arr, k, n, cnt)
                    else:
                        arr.pop()
                        freq[char] += 1
                        k -= ways

            return ""

        return build([], k, n // 2, 0)