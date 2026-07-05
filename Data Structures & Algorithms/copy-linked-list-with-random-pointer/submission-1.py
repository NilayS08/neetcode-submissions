"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap,pointer = {}, head
        if head:
            while pointer:
                copy = Node(pointer.val)
                hmap[pointer] = copy
                pointer = pointer.next
            pointer = head
            while pointer:
                copy = hmap[pointer]
                if pointer.next == None:
                    copy.next = None
                else:
                    copy.next = hmap[pointer.next]
                if pointer.random == None:
                    copy.random = None
                else:
                    copy.random = hmap[pointer.random]
                pointer = pointer.next
            return hmap[head]
        else:
            return head
        