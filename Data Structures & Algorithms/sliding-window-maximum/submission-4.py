from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # maintain a max-heap of nums. heap have (value, index)
        # add elements to heap
        # when exceed window size, only pop the max if it is out of window range.
        # else just keep using same max value

        answer = []
        heap = []

        for i in range(len(nums)):
            heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap[0][1] < (i - k + 1):
                    heappop(heap)
                answer.append(-heap[0][0])

        return answer
