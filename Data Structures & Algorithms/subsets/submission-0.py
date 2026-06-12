class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backTrack(curr, currentIndex):
            if currentIndex > len(nums):
                return

            answer.append(curr[:])
            for i in range(currentIndex, len(nums)):
                curr.append(nums[i])
                backTrack(curr, i + 1)
                curr.pop()

        backTrack([], 0)
        return answer