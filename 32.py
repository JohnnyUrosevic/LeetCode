class Solution:
    def longestValidParentheses(self, s: str) -> int:
        run = 0
        max_run = 0
        stack = []
        
        s = list(s)
        
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                s[i] = "*"
                run = 0
                continue
            
            run += 1
            max_run = max(max_run, run)
        
        if not stack:
            return max_run
        
        for i in stack:
            s[i] = "*"
        s = "".join(s)
        
        return max([len(run) for run in s.split("*")])
