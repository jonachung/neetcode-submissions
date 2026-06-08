from heapq import *

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create a graph
        # use dijkstra's to determine the path with least weight

        graph = defaultdict(list)
        for time in times:
            graph[time[0] - 1].append([time[1] - 1, time[2]])

        distances = [math.inf] * n
        distances[k - 1] = 0
        heap = [(0, k - 1)]
        while heap:
            currDist, node = heappop(heap)
            if currDist > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                dist = currDist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heappush(heap, (dist, neighbor))

        answer = max(distances)
        if answer == math.inf:
            return -1
        return answer