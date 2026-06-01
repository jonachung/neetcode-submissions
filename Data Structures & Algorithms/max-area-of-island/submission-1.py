class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs to deal with and expand the connected component
        # dfs -> calculate what the area is
        # keep track of max area of connected components

        maxArea = 0
        seen = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(grid)
        n = len(grid[0])

        def isValid(row, column):
            if 0 <= row < m and 0 <= column < n and grid[row][column] == 1:
                return True
            return False

        def dfs(row, column):
            area = 0
            for dx, dy in directions:
                newRow, newColumn = row + dx, column + dy
                if isValid(newRow, newColumn) and (newRow, newColumn) not in seen:
                    seen.add((newRow, newColumn))
                    area += 1
                    area += dfs(newRow, newColumn)

            return area

        for i in range(m):
            for j in range(n):
                if isValid(i, j) and (i, j) not in seen:
                    currentArea = max(1, dfs(i, j))
                    maxArea = max(maxArea, currentArea)

        return maxArea