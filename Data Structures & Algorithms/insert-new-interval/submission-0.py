class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        index = 0
        
        while index < len(intervals) and newInterval[0] > intervals[index][1]:
            answer.append(intervals[index])
            index += 1
            
        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            newInterval[0] = min(intervals[index][0], newInterval[0])
            newInterval[1] = max(intervals[index][1], newInterval[1])
            index += 1
            
        answer.append(newInterval)
        
        while index < len(intervals) and intervals[index][0] > newInterval[1]:
            answer.append(intervals[index])
            index += 1
            
        return answer