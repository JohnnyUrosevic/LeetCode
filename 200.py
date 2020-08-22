class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        nodes = [[(i,j) for j in range(len(grid[0]))] for i in range(len(grid))]
        group_sizes = [[1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        num_groups = len(grid) * len(grid[0])
        
        # find root of a nodes group
        def find(i, j):
            root_i, root_j = i, j
            while nodes[root_i][root_j] != (root_i, root_j):
                root_i, root_j = nodes[root_i][root_j]
                
            # path compression
            while (i, j) != (root_i, root_j):
                temp_i, temp_j = nodes[i][j]
                nodes[i][j] = (root_i, root_j)
                i, j = temp_i, temp_j
                
            return (i,j)
        
        # unify two groups
        def union(i, j, k, l):
            i,j = find(i, j)
            k,l = find(k, l)
            
            if (i,j) == (k,l):
                return
            
            if (group_sizes[i][j] >= group_sizes[k][l]):
                nodes[k][l] = nodes[i][j]
                group_sizes[i][j] += group_sizes[k][l]
            else:
                nodes[i][j] = nodes[k][l]
                group_sizes[k][l] += group_sizes[i][j]
            
            nonlocal num_groups
            num_groups -= 1
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not int(grid[i][j]):
                    num_groups -= 1
                    continue
                
                if j > 0 and int(grid[i][j-1]):
                    union(i, j, i, j-1)
                
                if i > 0 and int(grid[i-1][j]):
                    union(i, j, i-1, j)
                   
        return num_groups
