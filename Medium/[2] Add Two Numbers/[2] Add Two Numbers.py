"""
Accepted
2 [Medium]
Runtime: 4 ms, faster than 53.85% of Python3 online submissions for Add Two Numbers.
Memory Usage: 17.49 MB, less than 11.03% of Python3 online submissions for Add Two Numbers.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num = l1.val + l2.val
        carry = True if num // 10 else False

        head = ListNode(num % 10)

        left, right = l1.next, l2.next
        ptr = head
        while carry or left or right:
            num = 1 if carry else 0
            if left:
                num += left.val
                left = left.next
            if right:
                num += right.val
                right = right.next
            
            newNode = ListNode(num % 10)
            ptr.next = newNode
            ptr = ptr.next

            carry = True if num // 10 else False
        return head