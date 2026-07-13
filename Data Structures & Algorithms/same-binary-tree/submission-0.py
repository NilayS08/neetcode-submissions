# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()

            if not node_p and not node_q:
                continue

            if not node_p or not node_q:
                return False

            if node_p.val == node_q.val:
                if node_p.left or not node_p.left: stack_p.append(node_p.left)
                if node_p.right or not node_p.right: stack_p.append(node_p.right)
                if node_q.left or not node_q.left: stack_q.append(node_q.left)
                if node_q.right or not node_q.right: stack_q.append(node_q.right)
            else:
                return False
        if stack_p == stack_q: return True
        else: return False