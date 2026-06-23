# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs to get the nodes left to right by level
        if root is None:
            return []

        answer = []
        queue = deque([root])

        while queue:
            level = []
            levelLength = len(queue)
            for _ in range(levelLength):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            answer.append(level)

        return answer