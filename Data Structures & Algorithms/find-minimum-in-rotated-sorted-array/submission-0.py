class Solution:
    def findMin(self, nums: List[int]) -> int:
        # use binary search
        # find where one number is greater than another number next to it

        # while left < right
        # mid = (left + right) // 2
        # if nums[mid] > nums[right]: left = mid + 1
        # else: right = mid

        # return nums[left]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]