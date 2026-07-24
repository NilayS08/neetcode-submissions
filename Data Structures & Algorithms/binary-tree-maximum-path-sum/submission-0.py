# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        def dfs(node):
            nonlocal ans
            if node == None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            leftContri = max(0, left)
            rightContri = max(0, right)
            nodeVal = leftContri + node.val + rightContri
            ans = max(ans, nodeVal)
            parent = node.val + max(leftContri,rightContri)
            return parent
        dfs(root)
        return ans

