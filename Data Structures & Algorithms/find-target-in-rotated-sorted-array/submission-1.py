class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # determine the two sorted halves
        # check which half target is in then binary search that half
        # while left <= right
        # mid = left + right // 2
        # if nums[mid] == target: return mid
        # if nums[left] > nums[mid]: (where rotation splits)
        # if nums[mid] < target <= nums[right]: left = mid + 1
        # else: right = mid - 1
        # else:
        # if nums[low] <= target < nums[mid]: right = mid - 1 else left = mid + 1


        # return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1
