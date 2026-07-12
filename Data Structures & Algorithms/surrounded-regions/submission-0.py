class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # dfs to figure out what the connected components are.
        # surrounded -> the "O" cells do not touch the edge of board
        # dfs to get the coordinates of a current Island
        # -> check coordinates to see if they touch edge of the board
        # -> if they do, then we don't do anything
        # -> if they all don't then we change them all to be X cells

        # Time = O(MN) with M as num rows and N as num columns because worst case you would have to traverse through whole board to find islands
        # as well as do dfs to find the whole connected component
        # Space = O(MN) because at worst case the seen set could hold all cells in the board

        seen = set()
        m = len(board)
        n = len(board[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def isValid(row, column):
            if 0 <= row < m and 0 <= column < n and board[row][column] == 'O':
                return True
            return False

        def isOnEdge(row, column):
            if row == 0 or row == m - 1 or column == 0 or column == n - 1:
                return True
            return False

        def dfs(row, column):
            nonlocal isSurroundedIsland
            for direction in directions:
                dx, dy = direction
                newRow, newColumn = row + dx, column + dy
                if isValid(newRow, newColumn) and (newRow, newColumn) not in seen:
                    if isOnEdge(newRow, newColumn):
                        isSurroundedIsland = False
                    seen.add((newRow, newColumn))
                    currentIsland.add((newRow, newColumn))
                    dfs(newRow, newColumn)

        for row in range(m):
            for col in range(n):
                currentIsland = set()
                isSurroundedIsland = True
                if isValid(row, col) and (row, col) not in seen:
                    if isOnEdge(row, col):
                        isSurroundedIsland = False
                    seen.add((row, col))
                    currentIsland.add((row, col))
                    dfs(row, col)

                    # loop through all parts of current island to replace with X cells
                    if isSurroundedIsland:
                        for r, c in currentIsland:
                            board[r][c] = 'X'