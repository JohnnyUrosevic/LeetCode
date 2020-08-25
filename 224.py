class Solution:
    def calculate(self, s: str) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv,
        }
        
        pemdas = {
            "*": 1,
            "/": 1,
            "-": 2,
            "+": 2,
        }
        
        # convert to post
        current_num = ""
        stack = []
        terms = []
        for c in s:
            if c.isnumeric():
                current_num += c
            else:
                if current_num:
                    terms.append(int(current_num))
                    current_num = ""
                
                if c == "(":
                    stack.append(c)
                elif c == ")":
                    while stack[-1] != "(":
                        terms.append(stack.pop())
                    stack.pop() 
                elif c in ops:
                    while stack and stack[-1] != "(" and pemdas[c] >= pemdas[stack[-1]]:
                        terms.append(stack.pop())
                    stack.append(c)
                    
        if current_num: 
            terms.append(int(current_num))       
        while stack:
            terms.append(stack.pop())
        
        # evaluate postfix
        for term in terms:
            if term in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[term](b, a))
            else:
                stack.append(term)
        
        return stack[-1]
