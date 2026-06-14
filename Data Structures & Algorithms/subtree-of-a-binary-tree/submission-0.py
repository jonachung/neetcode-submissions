# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # have a function isSameTree to check if tree is the same tree or not.
        # if root is None -> return false
        # if subRoot is None -> return True
        # if root, subRoot isSameTree -> return True
        # recursively call isSubtree for root.left and root.right

        # isSameTree(root, subRoot) -> if root is None and subRoot is none -> return true
        # if root and subRoot and root.value == subroot.value -> check root.left subroot.left and root.right subroot.right isSameTree
        # return False

        def isSameTree(root, subRoot):
            if root is None and subRoot is None:
                return True
            if root and subRoot and (root.val == subRoot.val):
                return isSameTree(root.left, subRoot.left) and isSameTree(root.right, subRoot.right)

            return False

        if root is None:
            return False
        if subRoot is None:
            return True

        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)