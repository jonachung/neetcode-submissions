from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a frequency dictionary of key = number, value = frequency
        # create tuple of (frequency, number) and add to a min heap.
        # keep the heap to be of length k.
        # if length > k: heappop()

        # get the numbers from the heap at end and that is answer

        frequencyDict = defaultdict(int)
        for num in nums:
            frequencyDict[num] += 1

        heap = []
        for key, value in frequencyDict.items():
            heappush(heap, (value,  key))
            if len(heap) > k:
                heappop(heap)

        answer = []
        for key, value in heap:
            answer.append(value)
        return answer
