# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 1
        stack = [(root,depth)]
        if root:
            while stack:
                node, current_depth = stack.pop()
                if node.left:
                    stack.append((node.left, current_depth + 1))
                if node.right:
                    stack.append((node.right, current_depth + 1))
                depth = max(depth,current_depth)   
            return depth
        else:
            return 0