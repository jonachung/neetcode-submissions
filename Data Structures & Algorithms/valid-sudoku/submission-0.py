class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row to see if 1-9 with no duplicates
        # check each column to see if 1-9 with no duplicates
        # check each "3 x 3 sub-box" to see if 1-9 with no duplicates

        boardLength = 9
        squareLength = 3
        numbersSet = set(["1","2","3","4","5","6","7","8","9"])
        for row in range(boardLength):
            seen = set()
            for column in range(boardLength):
                if board[row][column] in seen:
                    return False
                elif board[row][column] in numbersSet:
                    seen.add(board[row][column])

        for column in range(boardLength):
            seen = set()
            for row in range(boardLength):
                if board[row][column] in seen:
                    return False
                elif board[row][column] in numbersSet:
                    seen.add(board[row][column])

        for square in range(9):
            seen = set()
            for i in range(squareLength):
                for j in range(squareLength):
                    r = (square // 3) * 3 + i
                    c = (square % 3) * 3 + j
                    if board[r][c] in seen:
                        return False
                    elif board[r][c] in numbersSet:
                        seen.add(board[r][c])


        return True
