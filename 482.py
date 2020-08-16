class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "")
        
        start = 0
        split_index = len(S) % K
        
        parts = []
        
        while start < len(S):
            parts.append(S[start:split_index])
            start = split_index
            split_index += K
        
        parts = [part for part in parts if part]
        return "-".join(parts).upper()
