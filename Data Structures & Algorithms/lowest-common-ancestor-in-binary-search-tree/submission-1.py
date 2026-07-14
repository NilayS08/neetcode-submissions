# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            node = stack.pop()

            if p.val < node.val < q.val or q.val < node.val < p.val :
                return node
            if node.val == p.val or node.val == q.val:
                return node
            if p.val < node.val and q.val < node.val:
                if node.left : stack.append(node.left)
            if p.val > node.val and q.val > node.val:
                if node.right: stack.append(node.right)
            