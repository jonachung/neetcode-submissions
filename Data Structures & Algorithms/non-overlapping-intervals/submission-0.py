class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by start time
        # loop through intervals
        # store prevEnd -> end of prev
        # if end of prev interval > start of curr interval:
        # increment answer
        # end of prev becomes min(end of prev, end of curr interval)

        intervals.sort()
        answer = -1
        prevEnd = intervals[0][1]
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if prevEnd > start:
                answer += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return answer