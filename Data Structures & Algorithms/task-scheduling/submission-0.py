from heapq import *

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create max heap to store (-frequency, task)
        # have a deque to store cooldown events
        # time = 0
        # while queue or heap:
        #      time += 1
        #      if queue and time == queue[0][1]:
        #         heappush(heap, queue[0])
        #         queue.popleft()

        #      if heap:
        #         f, task = heappop(heap)
        #         queue.append([(f + 1, task), time + n])
        #      
        # return time

        taskFrequency = defaultdict(int)
        queue = deque()
        for task in tasks:
            taskFrequency[task] += 1

        heap = []
        for key, value in taskFrequency.items():
            heappush(heap, (-value, key))

        time = 0
        while (heap or queue):
            time += 1
            if heap:
                frequency, task = heappop(heap)
                if frequency + 1 != 0:
                    queue.append([(frequency + 1, task), time + n])

            if queue and time == queue[0][1]:
                heappush(heap, queue[0][0])
                queue.popleft()

            print(heap)
            print(queue)

        return time
