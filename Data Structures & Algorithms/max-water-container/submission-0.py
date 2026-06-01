class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer approach -> left, right for indexes
        # area = 0
        # while left < right:
        #.    currentArea = (right - left) * min(height[left], height[right])
        #.    area = max(area, currentArea)
        #.    if height[left] < height[right]:
        #.          left += 1
        #.    else
        #.          right -= 1

        # return area

        left = 0
        right = len(heights) - 1
        area = 0
        while left < right:
            currentArea = min(heights[left], heights[right]) * (right - left)
            area = max(area, currentArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return area