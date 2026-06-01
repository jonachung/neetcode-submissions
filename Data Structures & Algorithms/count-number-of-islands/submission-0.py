class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we can use dfs to find the connected components
        # use a set() seen to track land components already seen to prevent cycles
        # O(M * N) space, O(M * N) time

        answer = 0
        seen = set()
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def isValid(row, column):
            if 0 <= row < m and 0 <= column < n and grid[row][column] == "1":
                return True
            return False

        def dfs(row, column):
            for dx, dy in directions:
                newRow, newColumn = row + dx, column + dy
                if isValid(newRow, newColumn) and (newRow, newColumn) not in seen:
                    seen.add((newRow, newColumn))
                    dfs(newRow, newColumn)

        for i in range(m):
            for j in range(n):
                if isValid(i, j) and (i, j) not in seen:
                    answer += 1
                    dfs(i, j)

        return answer