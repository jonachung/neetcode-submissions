# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs traversal to get nodes in level
        # the right side view is the last node in that level

        if root is None:
            return []

        answer = []
        queue = deque([root])

        while queue:
            queueLength = len(queue)
            level = []
            for _ in range(queueLength):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            answer.append(level[queueLength - 1])

        return answer