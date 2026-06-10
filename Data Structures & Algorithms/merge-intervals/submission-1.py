class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        # answer = []
        # add the first interval into answer

        # for start, end in intervals[1:]
        # if start <= answer[-1][1]:
        #.   answer[-1][1] = max(end, answer[-1][1])
        # else
        #    answer.append([start, end])

        # return answer

        intervals.sort()
        answer = []
        answer.append(intervals[0])

        for start, end in intervals[1:]:
            if start <= answer[-1][1]:
                answer[-1][1] = max(answer[-1][1], end)
            else:
                answer.append([start, end])

        return answer