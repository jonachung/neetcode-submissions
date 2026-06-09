class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # bfs with topological sort
        # create graph object to hold graph[prerequisite] = [courses]
        # indegree of [# courses]
        # indegree[course] += 1

        # create queue object, add courses with indegree 0 into the queue
        # global set() coursesTaken
        # while queue
        #    process node in the queue
        #.   add node to coursesTaken
        #.   get all the neighbors for node
        #.   decrement neighbors indegrees by 1
        #.   if an indegree becomes 0 -> add to the queue
        
        # if len(coursesTaken) == numCourses return true else return false


        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()
        coursesTaken = 0
        courses = []

        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            coursesTaken += 1
            courses.append(node)

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if coursesTaken == numCourses:
            return courses
        return []