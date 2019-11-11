class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapping = {}
        used = set()

        for c, d in zip(s, t):
            if c in mapping:
                if mapping[c] != d:
                    return False
            else:
                if d in used:
                    return False
                mapping[c] = d
                used.add(d)
        
        return True
