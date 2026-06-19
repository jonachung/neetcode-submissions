from collections import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # have a deque that will be of length k
        # when going through elements in nums list
        # add elements to deque
        # if length is greater than k -> pop from front
        # when length is equal to k -> find max and add to answer array

        # O(n) run since max() is only for constantly k elements, O(n) linear
        # scan to traverse the nums array

        queue = deque()
        answer = []

        for right in range(len(nums)):
            queue.append(nums[right])

            while len(queue) > k:
                queue.popleft()
            
            if len(queue) == k:
                answer.append(max(queue))

        return answer
            


        
        

