from heapq import *

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        
        for i in range(len(nums)):
            heappush(self.heap, nums[i])
            if len(self.heap) > k:
                heappop(self.heap)


    def add(self, val: int) -> int:

        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]
        
