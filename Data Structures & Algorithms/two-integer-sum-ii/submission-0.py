class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers for left and right of numbers array
        # while left < right
        #.   left + right = target -> return [left, right]
        #.   if left + right > target -> right -= 1
        #    if left + right < target -> left += 1

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total > target:
                right -= 1
            else:
                left += 1

        return [-1,-1]