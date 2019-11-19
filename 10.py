class Solution:
    def matchChars(self, sc: str, pc: str) -> bool:
        return pc == '.' or pc == sc
    
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*":
            return True
        
        while p:
            if len(p) > 1 and p[1] == '*':
                l = 0
                while l < len(s) and self.isMatch(s[l], p[0]):
                    l+=1
                
                for i in range(l, 0, -1):
                    result = self.isMatch(s[i:], p[2:])
                    
                    if result:
                        return True
                
                return self.isMatch(s, p[2:])
            
            if not self.matchChars(s[0], p[0]):
                return False
            
            s = s[1:]
            p = p[1:]
            
        return not s
