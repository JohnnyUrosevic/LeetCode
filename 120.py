class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [triangle[-1]]
        
        num_rows = len(triangle)
        for i in range(num_rows-2,-1,-1):
            dp.append([])
            for j in range(i+1):
                dp[num_rows-i-1].append(triangle[i][j] + min(dp[num_rows-i-2][j], dp[num_rows-i-2][j+1]))
        
        return dp[-1][0]