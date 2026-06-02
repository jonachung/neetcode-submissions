class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # left = 0, right = len(matrix) - 1, middle = (left + right) // 2
        # find the "middle row". in middle row check if target is middle[0] <= target <= middle[len(middle)]
        # if it is, then binary search through the middle row
        # if target < middle[0] -> right = middle - 1
        # if target > middle[len(middle)] -> left = middle + 1

        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middleRowIndex = (top + bottom) // 2
            middleRow = matrix[middleRowIndex]

            if middleRow[0] <= target <= middleRow[len(middleRow) - 1]:
                # binary search that middle row
                left = 0
                right = len(middleRow) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if middleRow[mid] == target:
                        return True
                    elif target < middleRow[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1

                return False

            elif target < middleRow[0]:
                bottom = middleRowIndex - 1
            else:
                top = middleRowIndex + 1

        return False
