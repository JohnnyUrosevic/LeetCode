class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        pre = ""
        min_len = min([len(s) for s in strs])
        
        for i in range(min_len):
            curr_char = strs[0][i]
            
            add_char = True
            for word in strs[1:]:
                if word[i] != curr_char:
                    add_char = False
                    break
            
            if not add_char:
                break
            pre += curr_char
        return pre
