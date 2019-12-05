class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        dp = [[1] * len(s), ([1] * len(s))]
        
        for i in range(2, len(s)+1):
            row = [0] * len(s)
            for j in range(len(s) - i + 1):
                row[j] = 1 if s[j] == s[j+i-1] and dp[i-2][j+1] else 0
                
            dp.append(row)
        
        for l in range(len(s),0,-1):
            try:
                i = dp[l].index(1)
                return s[i:i+l]
            except ValueError:
                pass
