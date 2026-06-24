class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # bfs with topological sort
        # create the direct graph as adjaceny list dictionary
        # keep track of indegrees

        graph = defaultdict(list)
        indegrees = [0 for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1

        queue = deque()

        for i in range(len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        taken = 0
        while queue:
            node = queue.popleft()
            taken += 1
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return (taken == numCourses)