class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        result = set()
        for i in range(len(s) - 9):
            sub = s[i:i+10]
            if sub in seen:
                result.add(sub)
            else:
                seen.add(sub)
                
        return list(result)
