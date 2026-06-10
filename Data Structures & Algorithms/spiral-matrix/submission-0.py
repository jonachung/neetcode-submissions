class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        m = len(matrix)
        n = len(matrix[0])
        leftColumnBound = 0
        rightColumnBound = n
        topRowBound = 0
        bottomRowBound = m

        while leftColumnBound < rightColumnBound and topRowBound < bottomRowBound:
            for i in range(leftColumnBound, rightColumnBound):
                answer.append(matrix[topRowBound][i])
            topRowBound += 1
            for i in range(topRowBound, bottomRowBound):
                answer.append(matrix[i][rightColumnBound - 1])
            rightColumnBound -= 1
            if not (leftColumnBound < rightColumnBound and topRowBound < bottomRowBound):
                break
            for i in range(rightColumnBound - 1, leftColumnBound - 1, -1):
                answer.append(matrix[bottomRowBound - 1][i])
            bottomRowBound -= 1
            for i in range(bottomRowBound - 1, topRowBound - 1, -1):
                answer.append(matrix[i][leftColumnBound])
            leftColumnBound += 1

        return answer