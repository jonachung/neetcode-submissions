class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(curr, currSum, i):
            if currSum == target:
                answer.append(curr[:])
                return

            if i > len(nums) or currSum > target:
                return

            for j in range(i, len(nums)):
                if currSum + nums[j] <= target:
                    curr.append(nums[j])
                    backtrack(curr, currSum + nums[j], j)
                    curr.pop()

        backtrack([], 0, 0)
        return answer

            