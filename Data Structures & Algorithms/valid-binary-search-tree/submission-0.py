# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # recursive (node, low, high)
        # if root is None: return true
        # if not low < root.val < high: return false
        # return (node.left,low,node) and (node.right,node,high)

        def helper(node, low, high):
            if node is None:
                return True

            if not low < node.val < high:
                return False

            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, -math.inf, math.inf)