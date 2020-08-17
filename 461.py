class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        difference = x ^ y
        count = 0
        while difference:
            count += difference % 2
            difference //= 2
            
        return count
