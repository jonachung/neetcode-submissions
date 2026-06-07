class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals
        # answer = []
        # for interval in intervals
        # start = interval[0]
        # end = interval[1]

        # if start <= answer[-1][1]
        # answer[-1][1] = end or answer[-1][1]
        # else
        # answer.append(start, end)
        intervals.sort()
        answer = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if len(answer) > 0 and start <= answer[-1][1]:
                answer[-1][1] = max(end, answer[-1][1])
            else:
                answer.append(interval)

        return answer