class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create the adjaceny list using the edges and then
        # do dfs

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        answer = 0

        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        for node in range(n):
            if node not in seen:
                answer += 1
                seen.add(node)
                dfs(node)

        return answer
