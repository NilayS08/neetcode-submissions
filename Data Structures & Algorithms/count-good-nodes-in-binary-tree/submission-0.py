# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        path_max = root.val
        stack = [(root,path_max)]
        res = []
        while stack:
            node,path_max_val = stack.pop()
            if node.val >= path_max_val:
                path_max_val = node.val
                res.append(node.val)
            if node.left:
                stack.append((node.left, path_max_val))
            if node.right:
                stack.append((node.right, path_max_val))
        return len(res)