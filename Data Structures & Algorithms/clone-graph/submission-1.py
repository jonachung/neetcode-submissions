"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # dfs is used to traverse through connected components of graph

        if node is None:
            return None

        graph = defaultdict(Node) # prevent cycles

        def dfs(node):
            if node in graph:
                return graph[node]

            currentNode = Node(node.val)
            graph[node] = currentNode
            for neighbor in node.neighbors:
                currentNode.neighbors.append(dfs(neighbor))
            return currentNode

        return dfs(node)
