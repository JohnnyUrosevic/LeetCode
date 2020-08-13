class Solution:
    def maxScore(self, s: str) -> int:
        scores = [0] * len(s)
        
        one_count = len([bit for bit in s if bit == "1"])
        scores[0] = one_count + 1 if s[0] == "0" else one_count - 1
        
        for i in range(1, len(s)-1):
            if s[i] == "0":
                scores[i] = scores[i-1] + 1
            else:
                scores[i] = scores[i-1] - 1
       
        return max(scores)
