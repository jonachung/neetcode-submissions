# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # dfs to compute left subtree height and right subtree height
        # max subtree (left & right) would be longest diameter
        diameter = 0

        def dfs(root): # track the height of the subtree
            nonlocal diameter

            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            diameter = max(diameter, left + right) # update diameter by getting left + right

            return 1 + max(left, right)

        dfs(root)
        return diameter