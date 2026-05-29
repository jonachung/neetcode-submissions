class Solution:
    # left = [] <- prefix products in left to right order
    # right = [] <- prefix products in right to left order
    # multiply left[i] * right[i] to get answer[i]
    # return answer
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1 for _ in range(len(nums))]
        right = [1 for _ in range(len(nums))]
        

        for i in range(1, len(nums)): # [1, 1, 2, 8]
            left[i] = left[i - 1] * nums[i - 1]

        for j in range(len(nums) - 2, -1, -1): # [1, 6, ]
            right[j] = right[j + 1] * nums[j + 1]

        answer = []
        for k in range(len(nums)):
            answer.append(left[k] * right[k])

        return answer