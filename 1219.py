class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        paths = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                paths.append(self.DFS(grid, i, j, set()))
        
        return max(paths)
        
    def DFS(self, grid, i, j, seen):
        if grid[i][j] == 0:
            return 0
        
        seen.add((i,j))
        gold = grid[i][j]
        
        if i != 0 and (i-1,j) not in seen:
            gold = max(gold, grid[i][j] + self.DFS(grid, i-1, j, seen.copy()))
        if j != 0 and (i,j-1) not in seen:
            gold = max(gold, grid[i][j] + self.DFS(grid, i, j-1, seen.copy()))
        if i != len(grid)-1 and (i+1,j) not in seen:
            gold = max(gold, grid[i][j] + self.DFS(grid, i+1, j, seen.copy()))
        if j != len(grid[0]) - 1 and (i,j+1) not in seen:
            gold = max(gold, grid[i][j] + self.DFS(grid, i, j+1, seen.copy()))
            
        return gold