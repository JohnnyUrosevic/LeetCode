class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        if (grid.empty()) return 0;
        
        int cost[grid.size()][grid[0].size()] = {0};
        
        cost[0][0] = grid[0][0];
        
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (!i && !j) continue;
                
                int left =  (j > 0) ? cost[i][j - 1] : INT_MAX;
                int up = (i > 0) ? cost[i - 1][j] : INT_MAX;
                
                cost[i][j] = grid[i][j] + min(left, up);                
            }
        }
        return cost[grid.size() - 1][grid[0].size() - 1];
    }
};
