class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs from the treasure chest(s) to the rotten fruit cells
        # 
        # check all directions and add in the queue and seen set
        
        seen = set()
        numFreshOranges = 0
        answer = 0
        directions = [(1,0),(0,1),(0,-1),(-1,0)]

        def isValid(row, column):
            if 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] == 1:
                return True
            return False

        queue = deque()

        # add rotten oranges to queue. count num fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0)) # row, col, numMin
                    seen.add((i,j))
                elif grid[i][j] == 1:
                    numFreshOranges += 1

        while queue:
            row, column, minute = queue.popleft()

            for dx, dy in directions:
                newRow, newColumn = row + dx, column + dy
                if isValid(newRow, newColumn) and (newRow, newColumn) not in seen:
                    numFreshOranges -= 1
                    queue.append((newRow, newColumn, minute + 1))
                    seen.add((newRow, newColumn))
                    answer = minute + 1

        if numFreshOranges > 0:
            return -1
        else:
            return answer