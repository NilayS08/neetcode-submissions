# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        carry = 0
        sumResult = ListNode()
        current = sumResult
        while p1 or p2 or carry:
            p1Val = p1.val if p1 else 0
            p2Val = p2.val if p2 else 0
            result = p1Val + p2Val + carry
            digit = result % 10
            carry = result // 10
            current.next = ListNode(digit)
            current = current.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        return sumResult.next