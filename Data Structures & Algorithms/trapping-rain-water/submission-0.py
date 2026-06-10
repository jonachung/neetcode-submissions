class Solution:
    def trap(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        maxHeightLeft = height[0]
        maxHeightRight = height[right]
        answer = 0

        while left < right:
            if maxHeightLeft < maxHeightRight:
                left += 1
                maxHeightLeft = max(maxHeightLeft, height[left])
                answer += maxHeightLeft - height[left]
            else:
                right -= 1
                maxHeightRight = max(maxHeightRight, height[right])
                answer += maxHeightRight - height[right]
        return answer