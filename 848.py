class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        ALPHA = "abcdefghijklmnopqrstuvwxyz"
        
        newS = ""
        
        for i in range(len(shifts)-2,-1,-1):
            shifts[i]+=shifts[i+1]
            
        for j in range(len(shifts)):
            newS += ALPHA[(ALPHA.find(S[j]) + shifts[j]) % 26]
        
        return newS
