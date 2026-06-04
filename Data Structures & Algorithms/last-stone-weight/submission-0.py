from heapq import *

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use a max heap (min heap but with neg numbers)
        # add all the stones into the max heap
        # run simulation
        # -> heap pop two heaviest stones and "smash"
        # ---> if two stones are same weight -> do nothing
        # ---> if stone1 heavier than stone2 -> heappush stone1-stone2 into heap
        # do this until len(heap) < 2

        maxHeap = []
        for i in range(len(stones)):
            heappush(maxHeap, -stones[i])

        while len(maxHeap) > 1:
            stone1 = -heappop(maxHeap)
            stone2 = -heappop(maxHeap)
            if stone1 != stone2:
                heappush(maxHeap, -abs(stone1 - stone2))

        if maxHeap:
            return -maxHeap[0]
        return 0
