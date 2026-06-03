class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        # loop through nums
        # if num > 0, skip
        # else: we get the two sum of numIndex + 1 to len(num) - 1

        def twoSum(nums, index, answer):
            low = index + 1
            high = len(nums) - 1

            while low < high:
                total = nums[index] + nums[low] + nums[high]
                if total < 0:
                    low += 1
                elif total > 0:
                    high -= 1
                else:
                    answer.append([nums[index], nums[low], nums[high]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]: # avoid duplicates
                        low += 1

        answer = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            elif i == 0 or nums[i] != nums[i - 1]: # no point to find sum for duplicate numbers
                twoSum(nums, i, answer)

        return answer