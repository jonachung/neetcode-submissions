# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # dfs to check if node values are the same
        # dfs(p, q)
        # if p and q are both None -> return True
        # if p is None and q not None OR p is not None and q is None -> return false
        # if p.val != q.val -> return False
        # return dfs(p.left, q.left) and dfs(p.right, q.right)

        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)