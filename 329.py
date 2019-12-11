from collections import defaultdict
from heapq import heapify, heappop

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        indices = defaultdict(list)
        seen = []
        for i in range(num_rows):
            for j in range(num_cols):
                indices[matrix[i][j]].append((i, j))
                seen.append(-matrix[i][j])
        
        dp = [x[:] for x in [[1] * num_cols] * num_rows]
        heapify(seen)
        
        while seen:
            n = -heappop(seen)
            if n in indices:
                for i, j in indices[n]:
                    if i > 0 and matrix[i-1][j] > n:
                        dp[i][j] = max(dp[i-1][j]+1, dp[i][j])
                    if j > 0 and matrix[i][j-1] > n:
                        dp[i][j] = max(dp[i][j-1]+1, dp[i][j])
                    if i < num_rows-1 and matrix[i+1][j] > n:
                        dp[i][j] = max(dp[i+1][j]+1, dp[i][j])
                    if j < num_cols-1 and matrix[i][j+1] > n:
                        dp[i][j] = max(dp[i][j+1]+1, dp[i][j])
        
        return max([max(row) for row in dp])
