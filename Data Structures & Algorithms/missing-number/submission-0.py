class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumOfAllNumbers = 0
        for i in range(0, len(nums) + 1):
            sumOfAllNumbers += i

        for j in range(len(nums)):
            sumOfAllNumbers -= nums[j]

        return sumOfAllNumbers