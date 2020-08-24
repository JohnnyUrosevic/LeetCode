class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # the ith bit flips after every 2**i numbers, meaning it will be 0 at some point if it flips
        diff = n - m
        
        count = 0
        while diff:
            count += 1
            diff >>= 1
        
        mask = -(2 ** (count)) 
        return m & n & mask
