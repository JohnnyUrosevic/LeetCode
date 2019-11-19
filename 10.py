class Solution:
    def matchChars(self, sc: str, pc: str) -> bool:
        return pc == '.' or pc == sc
    
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True
        
        while p:
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:]) or s and \
                    self.matchChars(s[0], p[0]) and self.isMatch(s[1:], p)
            
            if not s:
                return False
            
            if not self.matchChars(s[0], p[0]):
                return False
            
            s = s[1:]
            p = p[1:]
            
        return not s
