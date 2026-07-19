"""
Accepted
3996 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Even Number of Knight Moves.
Memory Usage: 19.23 MB, less than 58.26% of Python3 online submissions for Even Number of Knight Moves.
"""
class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        # black_tile -> (even, even) or (odd, odd)
        # white_tile -> (even, odd) or (odd, even)

        # In even moves, knight moves to the same colored tile

        if start[0] % 2 == start[1] % 2 and target[0] % 2 == target[1] % 2:
            return True
        elif start[0] % 2 != start[1] % 2 and target[0] % 2 != target[1] % 2:
            return True
        else:
            return False