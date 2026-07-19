"""
Accepted
3997 [Medium]
Runtime: 255 ms, faster than 75.05% of Python3 online submissions for Count Dominant Nodes in a Binary Tree.
Memory Usage: 49.59 MB, less than 49.70% of Python3 online submissions for Count Dominant Nodes in a Binary Tree.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        res = 0
        def rec(node):
            nonlocal res

            if not node:
                return -inf

            left = rec(node.left)
            right = rec(node.right)

            if node.val >= max(left, right):
                res += 1

            return max(left, right, node.val)

        rec(root)
        return res