# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        stack_r = [root]

        while stack_r :
            node_r = stack_r.pop()

            if node_r.val == subRoot.val:
                if self.isSameTree(node_r, subRoot):
                    return True
            
            if node_r.left: stack_r.append(node_r.left)
            if node_r.right: stack_r.append(node_r.right)
        return False

    def isSameTree(self, node1, node2):
        stack1 = [node1]
        stack2 = [node2]
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            
            if node1.val == node2.val:
                if node1.left or not node1.left : stack1.append(node1.left)
                if node1.right or not node1.right : stack1.append(node1.right)
                if node2.left or not node2.left : stack2.append(node2.left)
                if node2.right or not node2.right : stack2.append(node2.right)
            else:
                return False
        if stack1 == stack2: return True
        else: return False