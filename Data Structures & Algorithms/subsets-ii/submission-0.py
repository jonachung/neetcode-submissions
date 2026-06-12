class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()

        def backTrack(curr, currentIndex):
            if currentIndex > len(nums):
                return

            answer.add(tuple(curr))
            for i in range(currentIndex, len(nums)):
                curr.append(nums[i])
                backTrack(curr, i + 1)
                curr.pop()

        backTrack([], 0)
        return [list(combination) for combination in answer]