class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        target = len(grid) * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start_i = i
                    start_j = j
                elif grid[i][j] == -1:
                    target -= 1

        #grid[start_i][start_j] = -1
        return self.DFS(start_i, start_j, grid, 1, target, 0) 
    
    def DFS(self, i, j, grid, l, target, count):
        dirs = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0],
        ]
        
        if grid[i][j] == 2:
            if l == target:
                count += 1
                
            return count
        
        grid[i][j] = -1
        
        for dir in dirs:
            di = i + dir[0]
            dj = j + dir[1]
            if di < 0 or dj < 0 or \
                di == len(grid) or dj == len(grid[0]) or \
                grid[di][dj] == -1:
                continue
            
            count = self.DFS(di, dj, grid, l + 1, target, count)
        
        grid[i][j] = 0
        return count
