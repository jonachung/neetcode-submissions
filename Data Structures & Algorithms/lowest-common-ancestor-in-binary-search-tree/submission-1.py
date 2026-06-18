# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursion to basically check what lowest common ancestor is
        # if both p and q values are less than root.val -> move to left subtree
        # if both p and q values are greater than root.val -> move to right subtree
        # else (root is between p and q or root is equal to either p or q) -> return root.
        if root is None or p is None or q is None:
            return None
        if (p.val < root.val and q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val and q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        