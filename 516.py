class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [x[:] for x in [[0] * len(s)] * len(s)]
        
        for i in range(len(s)-1, -1, -1):
            dp[i][i] = 1
            
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j == i+1:
                        pal_len = 2
                    else:
                        pal_len = (2 + dp[i+1][j-1])
                else:
                    pal_len = max(dp[i][j-1], dp[i+1][j])
            
                dp[i][j] = pal_len
        return dp[0][-1]
