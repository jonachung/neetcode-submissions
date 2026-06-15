class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from the treasure chest(s) to the INF land cells
        # directly update grid row column in queue with distance variable
        # check all directions and add in the queue and seen set
        # directions = [(0,1),(1,0),(0,-1),(-1,0)]
        numRows = len(grid)
        numColumns = len(grid[0])
        
        def isValid(row, column):
            if 0 <= row < numRows and 0 <= column < numColumns and grid[row][column] != -1:
                return True
            return False

        queue = deque()
        seen = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(numRows):
            for j in range(numColumns):
                if grid[i][j] == 0:
                    queue.append((i,j))
                    seen.add((i,j))

        distance = 0
        while queue:
            for _ in range(len(queue)):
                row, column = queue.popleft()
                grid[row][column] = distance
                for dx, dy in directions:
                    newRow, newColumn = row + dx, column + dy
                    if isValid(newRow, newColumn) and (newRow, newColumn) not in seen:
                        queue.append((newRow, newColumn))
                        seen.add((newRow, newColumn))

            distance += 1
