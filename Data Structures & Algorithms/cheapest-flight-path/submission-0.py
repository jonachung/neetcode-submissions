from heapq import *

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for x, y, z in flights:
            graph[x].append([y, z])

        distances = [math.inf] * n
        distances[src] = 0
        heap = [(0, src, 0)]

        while heap:
            stops, node, currDist = heappop(heap)
            if stops > k:
                continue

            for neighbor, weight in graph[node]:
                dist = currDist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heappush(heap, (stops + 1, neighbor, dist))

        if distances[dst] == math.inf:
            return -1
        return distances[dst]



