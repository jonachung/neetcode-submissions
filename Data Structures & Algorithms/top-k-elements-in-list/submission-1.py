from heapq import *

class Solution:
    # get frequency dict of nums
    # heap ds to maintain k amount of elements
    # if length exceeds k then pop least frequent element
    # return the num values from the heap
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = defaultdict(int)
        for num in nums:
            frequencyDict[num] += 1

        heap = []
        for key, value in frequencyDict.items():
            heappush(heap, (value, key))
            if len(heap) > k:
                heappop(heap)

        answer = []
        for x, y in heap:
            answer.append(y)

        return answer