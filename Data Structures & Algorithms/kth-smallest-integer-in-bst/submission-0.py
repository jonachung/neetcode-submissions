# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # perform in order traversal and add node.val to a list
        # list is already sorted
        # return list[k - 1]

        bstList = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)
            bstList.append(node.val)
            dfs(node.right)

        dfs(root)
        return bstList[k - 1]