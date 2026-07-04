# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Two pass Solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pointer = head
        listLen = 1
        while pointer.next != None:
            pointer = pointer.next
            listLen += 1
        if listLen == n:
            return head.next
        current = head
        for i in range(listLen - n - 1):
            current = current.next
        current.next = current.next.next
        return head