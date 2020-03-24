class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return True
        
        stack = []
        stack_set = set()
        
        pushed_i = 0
        popped_i = 0
        
        while pushed_i < len(pushed):
            stack.append(pushed[pushed_i])
            stack_set.add(pushed[pushed_i])
            
            while popped_i < len(popped) and popped[popped_i] in stack_set:
                pop = stack.pop()
                if pop != popped[popped_i]:
                    return False
                stack_set.remove(pop)
                popped_i += 1
            
            pushed_i += 1
        
        
        return True