class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        def backTrack(curr, currentIndex):
            if currentIndex > len(nums):
                return

            answer.append(curr[:])
            for i in range(currentIndex, len(nums)):
                if i > currentIndex and nums[i] == nums[i - 1]:
                    continue # skip duplicate numbers
                curr.append(nums[i])
                backTrack(curr, i + 1)
                curr.pop()

        backTrack([], 0)
        return answer