"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from heapq import *
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort meetings by start time
        # have a min heap []
        # for interval in intervals:
        # check if interval.start < stack[-1].end
        #   -> add interval.end to stack
        # else
        #.  -> stack.pop() and add interval.end

        # len(stack) is the answer

        intervals.sort(key=lambda x : x.start)
        heap = []
        for interval in intervals:
            if not heap:
                heappush(heap, interval.end)
            elif heap and interval.start < heap[0]:
                heappush(heap, interval.end)
            else:
                heappop(heap)
                heappush(heap, interval.end)
            

        return len(heap)
    