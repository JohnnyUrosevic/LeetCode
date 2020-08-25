class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ops = {
            "+": operator.add,
            "*": operator.mul,
            "-": operator.sub
        }
        
        # turn string into list of numbers and operators
        input_arr = []
        anchor = 0
        for i in range(len(input)):
            if input[i] in ops:
                input_arr.append(int(input[anchor:i]))
                input_arr.append(input[i])
                anchor = i+1
        
        input_arr.append(int(input[anchor:]))
                  
        def helper(input) -> List[int]:
            # base case: just a number
            if len(input) == 1:
                return [input[0]]
            
            result = []
            # i is the index of the operator that is evaluated last
            for i in range(1, len(input), 2):
                # generate all sub groupings of each operand
                left = helper(input[:i])
                right = helper(input[i+1:])

                for l in left:
                    for r in right:
                        result.append(ops[input[i]](l,r))

            return result
        return helper(input_arr)
