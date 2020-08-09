class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count = 0
       
        while a or b or c:
            # % 2 gets the least significant bit
            if not (c % 2):
                if a % 2:
                    count += 1
                if b % 2:
                    count += 1
            else:
                if not a % 2 and not b % 2:
                    count += 1
            a = a >> 1
            b = b >> 1
            c = c >> 1
            
        return count
