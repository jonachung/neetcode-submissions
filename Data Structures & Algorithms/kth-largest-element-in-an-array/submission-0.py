from heapq import *

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # have a min heap that will be of length k
        # loop through nums and heappush to heap
        # if len(heap) > k -> heappop
        # return heap[0]

        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)

        return heap[0]