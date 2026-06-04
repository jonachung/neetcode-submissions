from heapq import *

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # u want the closest point, so u want to remove the furthest point
        # use max heap to be able to heappop furthest point
        # maintain maxHeap of length k
        # loop through points to determine distance and add the distance to maxHeap
        # if maxHeap > k -> heappop from maxHeap

        maxHeap = []
        answer = []

        for point in points:
            pointX = point[0]
            pointY = point[1]
            distance = pointX**2 + pointY**2
            heappush(maxHeap, (-distance, (pointX, pointY)))
            if len(maxHeap) > k:
                heappop(maxHeap)

        for i in range(len(maxHeap)):
            distance, point = maxHeap[i]
            answer.append([point[0], point[1]])

        return answer
