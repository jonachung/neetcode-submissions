# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recursion using dfs to find the tree height
        # height = 1 + (max(dfs(root.left), dfs(root.right)))

        def dfs(root):
            if root is None:
                return 0

            return 1 + (max(dfs(root.left), dfs(root.right)))

        if root is None:
            return True

        left = dfs(root.left)
        right = dfs(root.right)

        if abs(left - right) > 1:
            return False

        
        return self.isBalanced(root.left) and self.isBalanced(root.right)