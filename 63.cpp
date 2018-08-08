class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int xMax = obstacleGrid[0].size() - 1;
        int yMax = obstacleGrid.size() - 1;
        
        //Grid of the number of unique paths from each grid space
        int numPaths[yMax + 1][xMax + 1];
        
        numPaths[yMax][xMax] = !obstacleGrid[yMax][xMax];
        
        for (int i = yMax; i >= 0; i--) {
            for (int j = xMax; j >= 0; j--) {
                if (i == yMax && j == xMax) continue;
                
                if (obstacleGrid[i][j] == 1) { //there are no vald paths from an obstacle
                    numPaths[i][j] = 0;
                } 
                else {
                    numPaths[i][j] = ((i == yMax) ? 0 : numPaths[i + 1][j]) + ((j == xMax) ? 0 : numPaths[i][j + 1]); 
                }
            }
        }     
        
        return numPaths[0][0];
    }
};


class NaiveSolution {
public:
    struct Point {
        int x;
        int y;
        Point(int x, int y) {this->x = x; this->y = y;}
    };
    
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid.size() == 0) {return 0;}
        stack<Point> paths;
        paths.push(Point(0, 0));
        
        int xMax = obstacleGrid[0].size() - 1;
        int yMax = obstacleGrid.size() - 1;
        
        int validPaths = 0;
        
        if (obstacleGrid[yMax][xMax] == 1 || obstacleGrid[0][0] == 1) {
            return 0;
        }
        
        while (!paths.empty()) {
            Point curr = paths.top();
            paths.pop();
            
            if (curr.x == xMax && curr.y == yMax) {
                validPaths++;
                continue;
            }
            
            if (curr.x != xMax && obstacleGrid[curr.y][curr.x + 1] == 0) {
                paths.push(Point(curr.x + 1, curr.y));
            }
            if (curr.y != yMax && obstacleGrid[curr.y + 1][curr.x] == 0) {
                paths.push(Point(curr.x, curr.y + 1));
            }
        }
        
        return validPaths;
    }
};
